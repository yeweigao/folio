"""Shared stdlib-only helpers for Folio scripts: a small DESIGN.md parser
(the YAML subset of the skeleton's Tokens block) and WCAG contrast math."""
import re

TOKENS = re.compile(r"^## Tokens\s*\n.*?```ya?ml\n(.*?)\n```[^\n]*\n?", re.S | re.M)


def parse_tokens(text):
    """Return (tokens, prose). Tokens come from the ```yaml block under
    ## Tokens; prose is the file without that section. The title (# ...)
    and the paragraph under it become tokens['name'] and ['description']."""
    m = TOKENS.search(text)
    if m:
        tokens = _parse_yaml(m.group(1))
        prose = text[:m.start()] + text[m.end():]
    else:
        tokens, prose = {}, text
    title = re.match(r"^# (.+)\n+([^#\n][^\n]*)?", prose)
    if title:
        tokens.setdefault("name", title.group(1).strip())
        if title.group(2):
            tokens.setdefault("description", title.group(2).strip())
    return tokens, prose


def _parse_yaml(body):
    tokens, section = {}, None
    for line in body.split("\n"):
        if not line.strip() or line.strip().startswith("#"):
            continue
        top = re.match(r"^([A-Za-z][\w-]*):\s*(.*)$", line)
        sub = re.match(r"^\s{2}([\w-]+):\s*(.*)$", line)
        if top and not line.startswith(" "):
            section, val = top.group(1), top.group(2).strip()
            tokens[section] = _scalar(val) if val else {}
        elif sub and section:
            k, val = sub.group(1), sub.group(2).strip()
            tokens[section][k] = _inline_map(val) if val.startswith("{") else _scalar(val)
    return tokens

def _scalar(v):
    v = v.strip().strip('"').strip("'")
    return v

def _inline_map(v):
    inner = v.strip()[1:-1]
    out = {}
    for part in re.split(r",\s*(?=[A-Za-z]+\s*:)", inner):
        if ":" in part:
            k, val = part.split(":", 1)
            out[k.strip()] = val.strip().strip('"').strip("'")
    return out

def resolve(ref, tokens):
    m = re.fullmatch(r"\{(colors|typography|spacing|rounded)\.([\w-]+)\}", str(ref))
    if m:
        return tokens.get(m.group(1), {}).get(m.group(2))
    return ref

def _lum(hexcolor):
    h = hexcolor.lstrip("#")
    if len(h) != 6:
        return None
    r, g, b = (int(h[i:i+2], 16) / 255 for i in (0, 2, 4))
    f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = f(r), f(g), f(b)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def contrast(a, b):
    la, lb = _lum(a), _lum(b)
    if la is None or lb is None:
        return None
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)

HEX = re.compile(r"#[0-9A-Fa-f]{6}\b")
