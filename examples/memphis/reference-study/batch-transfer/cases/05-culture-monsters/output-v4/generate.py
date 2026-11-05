#!/usr/bin/env python3
"""Compose the new Culture Monsters brief as editable SVG primitives and type."""
from pathlib import Path
import math
import subprocess
import sys
import xml.etree.ElementTree as ET

OUT = Path(__file__).resolve().parent
CASE = OUT.parent
PAPER = "#FFFFFF"
INK = "#030303"
RED = "#FF354A"
PINK = "#FD8CE5"
YELLOW = "#FFE42C"
BLUE = "#1768F6"
FONT = "Study Sans, Study CJK, sans-serif"

parts = [
    '<svg xmlns="http://www.w3.org/2000/svg" width="900" height="1200" '
    'viewBox="0 0 900 1200" role="img" aria-labelledby="poster-title poster-desc">',
    '<title id="poster-title">TTXC 2027 — 城市游乐场 / City Play!</title>',
    '<desc id="poster-desc">文化科技活动测试海报；以不等大的平面独眼身体、长触手身体及粗实纹样，围绕白色标题横带与红色活动信息排布。</desc>',
    '<!-- FONTS -->',
    '<defs>',
    '<clipPath id="hero-tile"><rect width="450" height="450"/></clipPath>',
    '<clipPath id="petal-tile"><rect x="450" width="450" height="225"/></clipPath>',
    '<clipPath id="cut-tile"><rect x="675" y="225" width="112.5" height="112.5"/></clipPath>',
    '<clipPath id="tentacle-tile"><rect x="675" y="585" width="225" height="337.5"/></clipPath>',
    '<clipPath id="return-tile"><rect x="675" y="922.5" width="225" height="277.5"/></clipPath>',
    '</defs>',
]


def add(markup):
    parts.append(markup)


def rect(x, y, w, h, fill):
    add(f'<rect x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" fill="{fill}"/>')


def circle(cx, cy, radius, fill):
    add(f'<circle cx="{cx:g}" cy="{cy:g}" r="{radius:g}" fill="{fill}"/>')


def point(cx, cy, radius, angle):
    a = math.radians(angle)
    return cx + radius * math.cos(a), cy + radius * math.sin(a)


def text_line(content, x, baseline, size, weight, ident):
    add(f'<text id="{ident}" x="{x:g}" y="{baseline:g}" fill="{INK}" '
        f'font-family="{FONT}" font-size="{size:g}" font-weight="{weight}">{content}</text>')


# The information ground remains one continuous red field.
rect(0, 0, 900, 1200, RED)

# Double-module lead: three blunt, joined lobes; only the upper lobe bleeds.
add('<g id="stacked-cyclops" clip-path="url(#hero-tile)">')
rect(0, 0, 450, 450, BLUE)
circle(225, 55, 97.2, YELLOW)
circle(225, 181, 101.25, YELLOW)
circle(225, 315, 135, YELLOW)
circle(225, 326, 60, PAPER)
circle(225, 326, 33, INK)
add('</g>')

# Broad top pattern, deliberately clipped by its shallow rectangular tile.
add('<g id="wide-petals" clip-path="url(#petal-tile)">')
rect(450, 0, 450, 225, PINK)
for angle in range(0, 360, 60):
    px, py = point(675, 112.5, 110, angle)
    add(f'<ellipse cx="{px:.4f}" cy="{py:.4f}" rx="85" ry="35" '
        f'transform="rotate({angle} {px:.4f} {py:.4f})" fill="{INK}"/>')
add('</g>')

# A single-module ring and two half-module tiles turn the upper collage.
add('<g id="disc-ring">')
rect(450, 225, 225, 225, YELLOW)
for angle in range(0, 360, 45):
    px, py = point(562.5, 337.5, 74, angle)
    circle(px, py, 17.5, BLUE)
add('</g>')

add('<g id="white-cuts" clip-path="url(#cut-tile)">')
rect(675, 225, 112.5, 112.5, INK)
for angle in range(0, 360, 60):
    pts = [point(731.25, 281.25, 13, angle),
           point(731.25, 281.25, 69, angle - 13),
           point(731.25, 281.25, 69, angle + 13)]
    data = ' '.join(f'{x:.4f},{y:.4f}' for x, y in pts)
    add(f'<polygon points="{data}" fill="{PAPER}"/>')
add('</g>')

add('<g id="small-disc-ring">')
rect(787.5, 225, 112.5, 112.5, PINK)
for angle in range(0, 360, 60):
    px, py = point(843.75, 281.25, 38, angle)
    circle(px, py, 9, RED)
add('</g>')

add('<g id="deep-scallops">')
rect(675, 337.5, 225, 112.5, BLUE)
add(f'<path d="M675 337.5 H900 V342 '
    'C900 389 889 423 862.5 423 C836 423 825 389 825 342 '
    'C825 389 814 423 787.5 423 C761 423 750 389 750 342 '
    f'C750 389 739 423 712.5 423 C686 423 675 389 675 342 Z" fill="{YELLOW}"/>')
add('</g>')

# Paper crossing spans the whole red field and does not cut required type.
rect(0, 450, 900, 135, PAPER)
text_line('TTXC 2027', 22, 558, 105.3, 900, 'event')

# Narrow continuation beside the lower reading field: a second silhouette
# family and a large coarse cut pattern, both running to the right trim.
add('<g id="long-tentacled-body" clip-path="url(#tentacle-tile)">')
rect(675, 585, 225, 337.5, PINK)
strands = [
    'M706 685 C701 718 728 729 715 762 C697 794 710 813 713 845 C716 868 703 881 708 899',
    'M736 693 C744 723 726 742 733 773 C744 805 726 824 735 856 C741 873 736 886 733 902',
    'M768 697 C751 727 778 746 766 777 C754 810 777 831 766 860 C759 879 765 891 766 906',
    'M801 697 C818 725 789 748 803 779 C817 809 796 832 805 861 C812 878 807 892 807 907',
    'M834 693 C824 724 845 744 836 775 C824 805 844 827 836 856 C829 873 838 887 836 902',
    'M867 685 C875 718 848 738 862 769 C880 798 860 819 867 848 C875 870 869 885 873 899',
]
for d in strands:
    add(f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="9.5" stroke-linecap="round"/>')
add(f'<path d="M692.5 687 C692.5 633 729 603 787.5 603 '
    'C846 603 882.5 633 882.5 687 '
    'Q867 710 851 694 Q835 714 819 697 Q803 716 787.5 698 '
    f'Q772 716 756 697 Q740 714 724 694 Q708 710 692.5 687 Z" fill="{INK}"/>')
circle(787.5, 643, 16, PAPER)
circle(787.5, 643, 8.8, INK)
for row in range(3):
    for col in range(10):
        circle(741.6 + col * 10.2, 675 + row * 10.2, 3.4, PAPER)
add('</g>')

add('<g id="lower-cut-pattern" clip-path="url(#return-tile)">')
rect(675, 922.5, 225, 277.5, YELLOW)
for angle in range(0, 360, 45):
    pts = [point(787.5, 1061.25, 25, angle),
           point(787.5, 1061.25, 172, angle - 13),
           point(787.5, 1061.25, 172, angle + 13)]
    data = ' '.join(f'{x:.4f},{y:.4f}' for x, y in pts)
    add(f'<polygon points="{data}" fill="{BLUE}"/>')
add('</g>')

# All eight required strings remain one native text element each.
add('<g id="lower-information">')
text_line('城市游乐场', 22, 682, 86.4, 900, 'theme-zh')
text_line('City Play!', 22, 782, 86.4, 900, 'theme-en')
text_line('ART × SOUND × TECHNOLOGY', 22, 859, 27, 700, 'program-description')
text_line('一起把城市玩出新花样', 22, 913, 21.6, 400, 'slogan')
text_line('2027.09.10–12', 22, 1008, 54, 900, 'dates')
text_line('海岸文化中心', 22, 1092, 54, 900, 'venue-zh')
text_line('Coast Culture Center', 22, 1175, 54, 900, 'venue-en')
add('</g>')
add('</svg>')

raw = '\n'.join(parts) + '\n'
OUT.mkdir(parents=True, exist_ok=True)
(OUT / 'raw.svg').write_text(raw, encoding='utf-8')
subprocess.run([
    sys.executable, str(CASE / 'input-v4' / 'embed_fonts.py'),
    str(CASE / 'input-v4' / 'fonts'), str(OUT / 'raw.svg'),
    str(OUT / 'poster.svg'),
], check=True)

# Small, content-specific structural checks; rendering is a separate step.
expected = [
    'TTXC 2027', '城市游乐场', 'City Play!', 'ART × SOUND × TECHNOLOGY',
    '一起把城市玩出新花样', '2027.09.10–12', '海岸文化中心', 'Coast Culture Center',
]
ns = {'s': 'http://www.w3.org/2000/svg'}
for filename in ['raw.svg', 'poster.svg']:
    root = ET.fromstring((OUT / filename).read_text(encoding='utf-8'))
    assert root.attrib['viewBox'] == '0 0 900 1200'
    actual = [''.join(node.itertext()) for node in root.findall('.//s:text', ns)]
    assert actual == expected, (filename, actual)
    assert not root.findall('.//s:image', ns)
    assert not root.findall('.//s:foreignObject', ns)
embedded = (OUT / 'poster.svg').read_text(encoding='utf-8')
assert embedded.count('data:font/woff2;base64,') == 4
print('Verified: both SVGs parse; 900 × 1200; 8 exact editable text strings; 4 embedded font faces; no image/foreignObject.')
