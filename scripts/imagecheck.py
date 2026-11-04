#!/usr/bin/env python3
"""Check native PPTX raster pictures for unequal X/Y scale after cropping.

Usage: imagecheck.py file.pptx [--tolerance 0.5] [--json report.json]

Tolerance is percentage deviation from equal scale. PNG, JPEG and GIF use
their embedded pixel dimensions. Unsupported media, non-default fill modes,
EXIF orientation and grouped transforms require visual review. A flagged
picture may be intentional: inspect it against its source. This audit does
not replace checking the rendered export. Stdlib only; exit 1 for flags.
"""
import argparse
import json
import posixpath
import re
import struct
import sys
import zipfile
import xml.etree.ElementTree as ET

NS = {
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
}


def dimensions(data):
    if data.startswith(b"\x89PNG\r\n\x1a\n") and len(data) >= 24:
        return struct.unpack(">II", data[16:24])
    if data[:6] in (b"GIF87a", b"GIF89a") and len(data) >= 10:
        return struct.unpack("<HH", data[6:10])
    if data.startswith(b"\xff\xd8"):
        i, size = 2, None
        while i < len(data):
            if data[i] != 0xFF:
                break
            while i < len(data) and data[i] == 0xFF:
                i += 1
            if i >= len(data):
                break
            marker = data[i]
            i += 1
            if marker in (0xD9, 0xDA):
                break
            if marker == 0x01 or 0xD0 <= marker <= 0xD8:
                continue
            if i + 2 > len(data):
                break
            length = int.from_bytes(data[i:i + 2], "big")
            if length < 2 or i + length > len(data):
                break
            segment = data[i + 2:i + length]
            # Orientation handling differs between renderers; do not assume it.
            if marker == 0xE1 and segment.startswith(b"Exif\x00\x00"):
                raise ValueError("EXIF-bearing JPEG: inspect orientation in the export")
            if marker in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7,
                          0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF) and len(segment) >= 5:
                h, w = struct.unpack(">HH", segment[1:5])
                size = (w, h)
            i += length
        if size:
            return size
    raise ValueError("unsupported or unreadable raster dimensions")


def fraction(value):
    return float(value[:-1]) / 100 if value.endswith("%") else float(value) / 100000


def audit(path, tolerance):
    rows = []
    with zipfile.ZipFile(path) as archive:
        slides = sorted((n for n in archive.namelist()
                         if re.fullmatch(r"ppt/slides/slide\d+\.xml", n)),
                        key=lambda n: int(re.search(r"slide(\d+)", n).group(1)))
        for slide in slides:
            relpath = posixpath.join(posixpath.dirname(slide), "_rels",
                                    posixpath.basename(slide) + ".rels")
            links = {r.attrib["Id"]: r.attrib for r in ET.fromstring(archive.read(relpath))}
            tree = ET.fromstring(archive.read(slide))
            grouped = {id(p) for g in tree.findall(".//p:grpSp", NS)
                       for p in g.findall(".//p:pic", NS)}
            for pic in tree.findall(".//p:pic", NS):
                name = pic.find("./p:nvPicPr/p:cNvPr", NS)
                row = {"slide": slide, "picture": name.get("name", "") if name is not None else ""}
                rows.append(row)
                try:
                    if id(pic) in grouped:
                        raise ValueError("grouped picture: inspect composite transforms")
                    fill = pic.find("./p:blipFill", NS)
                    blip = fill.find("a:blip", NS) if fill is not None else None
                    if blip is None:
                        raise ValueError("no raster blip")
                    if any(e.tag.endswith("}svgBlip") for e in blip.iter()):
                        raise ValueError("SVG with raster fallback: inspect vector fit")
                    rel = links.get(blip.get("{" + NS["r"] + "}embed"), {})
                    if not rel.get("Target") or rel.get("TargetMode") == "External":
                        raise ValueError("external or missing image relationship")
                    media = posixpath.normpath(posixpath.join(posixpath.dirname(slide), rel["Target"])).lstrip("/")
                    row["source"] = media
                    if fill.find("a:stretch", NS) is None:
                        raise ValueError("non-stretch fill: inspect tiling or fit")
                    dest = fill.find("a:stretch/a:fillRect", NS)
                    if dest is not None and any(fraction(v) for v in dest.attrib.values()):
                        raise ValueError("non-default destination fill rectangle")
                    sw, sh = dimensions(archive.read(media))
                    ext = pic.find("./p:spPr/a:xfrm/a:ext", NS)
                    if ext is None:
                        raise ValueError("missing picture frame")
                    crop = fill.find("a:srcRect", NS)
                    c = {k: fraction(crop.get(k, "0")) if crop is not None else 0
                         for k in ("l", "r", "t", "b")}
                    vw, vh = sw * (1 - c["l"] - c["r"]), sh * (1 - c["t"] - c["b"])
                    fw, fh = float(ext.get("cx", "0")), float(ext.get("cy", "0"))
                    if min(vw, vh, fw, fh) <= 0:
                        raise ValueError("empty source crop or frame")
                    ratio = (fw / fh) / (vw / vh)
                    error = abs(ratio - 1) * 100
                    row.update(sourcePixels=[sw, sh], crop=c, relativeXYScale=ratio,
                               anisotropyPercent=error,
                               status="flag" if error > tolerance else "ok")
                except (ValueError, KeyError, struct.error) as exc:
                    row.update(status="review", reason=str(exc))
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pptx")
    parser.add_argument("--tolerance", type=float, default=0.5, help="percentage deviation (default: 0.5)")
    parser.add_argument("--json", metavar="PATH", help="write detailed rows to this path")
    args = parser.parse_args()
    if not 0 <= args.tolerance < 100:
        parser.error("tolerance must be between 0 and 100 percent")
    try:
        rows = audit(args.pptx, args.tolerance)
    except (OSError, KeyError, zipfile.BadZipFile, ET.ParseError) as exc:
        print(f"ERROR  {exc}", file=sys.stderr)
        return 2
    for row in rows:
        if row["status"] != "ok":
            detail = row.get("reason") or f'unequal X/Y scale {row["anisotropyPercent"]:.3f}%'
            print(f'{row["status"].upper()}  {row["slide"]} · {row["picture"]}: {detail}')
    flags = sum(r["status"] == "flag" for r in rows)
    reviews = sum(r["status"] == "review" for r in rows)
    print(f"{len(rows) - reviews} pictures checked · {flags} unequal-scale flags · {reviews} need visual review")
    if not rows:
        print("No native slide pictures found; flattened pages and other image fills are not audited.")
    if args.json:
        with open(args.json, "w", encoding="utf-8") as out:
            json.dump(rows, out, ensure_ascii=False, indent=2)
            out.write("\n")
    return 1 if flags else 0


if __name__ == "__main__":
    sys.exit(main())
