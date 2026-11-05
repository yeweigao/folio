#!/usr/bin/env python3
"""Native, editable 900 × 1200 Culture Monsters poster.

All geometry and layout are authored here. The supplied neutral helper only
embeds glyph subsets after this script writes raw.svg.
"""
from pathlib import Path
from math import cos, sin, pi
from html import escape
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent
OUT = Path(__file__).resolve().parent
C = dict(paper="#FFFFFF", ink="#030303", red="#FF354A", pink="#FD8CE5", yellow="#FFE42C", blue="#1768F6")
parts = []

def add(s):
    parts.append(s)

def rect(x, y, w, h, color, **attrs):
    extra = " ".join(f'{k.replace("_", "-")}="{v}"' for k, v in attrs.items())
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{C.get(color, color)}" {extra}/>')

def circle(x, y, r, color):
    add(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{C.get(color, color)}"/>')

def path(d, color):
    add(f'<path d="{d}" fill="{C.get(color, color)}"/>')

def txt(content, x, y, size, weight=900, family="Study Sans, Study CJK, sans-serif", lang="en"):
    add(f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" fill="{C["ink"]}" xml:lang="{lang}">{escape(content)}</text>')

add('<svg xmlns="http://www.w3.org/2000/svg" width="900" height="1200" viewBox="0 0 900 1200" role="img" aria-labelledby="title description">')
add('<title id="title">TTXC 2027 — 城市游乐场 / City Play!</title>')
add('<desc id="description">ART × SOUND × TECHNOLOGY. 一起把城市玩出新花样. 2027.09.10–12. 海岸文化中心. Coast Culture Center.</desc>')
add('<!-- FONTS -->')
add('<defs>')
for ident, x, y, w, h in [
    ('large', 0, 0, 450, 450),
    ('petals', 450, 0, 225, 225),
    ('scallops', 675, 0, 225, 112.5),
    ('tentacles', 675, 112.5, 225, 225),
    ('squat', 450, 225, 225, 225),
    ('burst', 675, 337.5, 112.5, 112.5),
    ('bars', 787.5, 337.5, 112.5, 112.5),
    ('lower-body', 675, 775, 225, 225),
    ('lower-ring', 675, 1000, 225, 200),
]:
    add(f'<clipPath id="clip-{ident}"><rect x="{x}" y="{y}" width="{w}" height="{h}"/></clipPath>')
add('</defs>')

# The red reading field also joins every exposed module edge.
rect(0, 0, 900, 1200, 'red')

# Dominant two-lobed body, with broad integral feet, bleeds at the top and left.
add('<g id="large-single-eye-body" clip-path="url(#clip-large)">')
rect(0, 0, 450, 450, 'blue')
path('M182 -62 C280 -74 367 -34 378 46 C429 67 452 124 424 178 C415 198 399 210 380 222 C428 258 435 319 396 357 C372 380 341 391 310 390 L315 451 H236 L225 396 C188 410 147 409 117 389 L92 450 H15 L49 364 C9 339 -10 302 11 265 C22 244 37 234 59 222 C9 183 1 141 26 101 C42 75 67 62 95 59 C98 -6 127 -52 182 -62 Z', 'pink')
circle(227, 145, 76.5, 'paper')
circle(245, 153, 45.5, 'ink')
for x in [177, 207, 237, 267]:
    circle(x, 270, 10, 'ink')
add('</g>')

# Six broad petals fill their square, without a surrounding inset frame.
add('<g id="petal-pattern" clip-path="url(#clip-petals)">')
rect(450, 0, 225, 225, 'yellow')
for a in range(0, 360, 60):
    add(f'<ellipse cx="610.5" cy="112.5" rx="65" ry="27" fill="{C["red"]}" transform="rotate({a} 562.5 112.5)"/>')
add('</g>')

# A shallow tile of opposing, deep solid scallops.
add('<g id="deep-scallop-pattern" clip-path="url(#clip-scallops)">')
rect(675, 0, 225, 112.5, 'ink')
for x in [675, 787.5, 900]:
    circle(x, 0, 56.25, 'pink')
for x in [731.25, 843.75]:
    circle(x, 112.5, 56.25, 'pink')
add('</g>')

# Compact companion: a broad head and a few blunt, continuous tentacles.
add('<g id="blue-tentacled-body" clip-path="url(#clip-tentacles)">')
rect(675, 112.5, 225, 225, 'pink')
path('M704 246 C679 213 692 152 734 140 C764 125 810 131 827 157 C862 158 885 179 884 213 C883 231 876 246 864 255 L881 305 C887 323 869 334 855 321 L833 286 L828 323 C826 343 802 342 800 323 L797 286 L775 326 C767 343 745 334 751 316 L760 278 L729 305 C713 320 695 303 709 286 L726 263 C715 260 708 254 704 246 Z', 'blue')
for x in [751, 802]:
    circle(x, 204, 18, 'paper')
    circle(x - 4, 207, 10, 'ink')
for x in [771, 786, 801]:
    circle(x, 248, 4.2, 'ink')
add('</g>')

# Squat paired-eye body: three swollen upper lobes and short heavy feet.
add('<g id="yellow-squat-body" clip-path="url(#clip-squat)">')
rect(450, 225, 225, 225, 'red')
path('M480 320 C462 294 473 260 508 256 C525 233 559 232 579 252 C614 242 652 260 653 293 C683 315 673 349 647 362 L651 411 Q652 432 633 432 Q614 432 614 413 L611 390 L585 389 L584 420 Q584 438 566 438 Q548 438 548 420 L548 389 L523 386 L510 417 Q499 435 483 423 Q471 413 481 397 L496 368 C466 362 458 337 480 320 Z', 'yellow')
for x in [531, 592]:
    circle(x, 309, 21, 'paper')
    circle(x + 3, 307, 12, 'ink')
for x in [542, 561, 580]:
    circle(x, 358, 4.7, 'ink')
add('</g>')

# Half-module bursts and blunt bars create a small scale below the companions.
add('<g id="coarse-cut-pattern" clip-path="url(#clip-burst)">')
rect(675, 337.5, 112.5, 112.5, 'yellow')
points = []
for i in range(16):
    angle = -pi / 2 + i * pi / 8
    radius = 76 if i % 2 == 0 else 29
    points.append(f'{731.25 + radius * cos(angle):.3f},{393.75 + radius * sin(angle):.3f}')
add(f'<polygon points="{" ".join(points)}" fill="{C["ink"]}"/>')
add('</g>')
add('<g id="radial-bar-pattern" clip-path="url(#clip-bars)">')
rect(787.5, 337.5, 112.5, 112.5, 'blue')
for a in range(0, 360, 45):
    rect(870.75, 389.25, 38, 9, 'pink', rx=4.5, transform=f'rotate({a} 843.75 393.75)')
add('</g>')

# Paper crossing: one lead and two deliberate, equally ranked theme lines.
rect(0, 450, 900, 325, 'paper')
add('<g id="title-crossing">')
txt('TTXC 2027', 22, 550, 105.3)
txt('城市游乐场', 22, 646, 86.4, family='Study CJK, Study Sans, sans-serif', lang='zh-Hans')
txt('City Play!', 22, 735, 86.4)
add('</g>')

# Lower return: a small upright body beside the reading region, then a disc ring.
add('<g id="lower-single-eye-body" clip-path="url(#clip-lower-body)">')
rect(675, 775, 225, 225, 'yellow')
path('M776 760 C817 755 849 784 846 820 C878 833 887 866 868 892 C886 914 881 947 857 960 L862 1004 H815 L810 972 C790 982 769 978 756 969 L739 1005 H692 L719 950 C696 927 700 896 721 879 C700 855 707 822 731 809 C730 782 749 766 776 760 Z', 'ink')
circle(788, 844, 32, 'paper')
circle(780, 848, 18.5, 'ink')
for x in [769, 785, 801]:
    circle(x, 910, 4.3, 'paper')
add('</g>')
add('<g id="lower-disc-ring" clip-path="url(#clip-lower-ring)">')
rect(675, 1000, 225, 200, 'blue')
for i in range(8):
    angle = -pi / 2 + i * pi / 4
    circle(round(787.5 + 78 * cos(angle), 4), round(1100 + 78 * sin(angle), 4), 18, 'yellow')
add('</g>')

# Every fixed fact stays live and uses the role sizes supplied in DESIGN.md.
add('<g id="event-facts">')
txt('ART × SOUND × TECHNOLOGY', 22, 821, 27, 700)
txt('2027.09.10–12', 22, 905, 54)
txt('海岸文化中心', 22, 995, 54, family='Study CJK, Study Sans, sans-serif', lang='zh-Hans')
txt('Coast Culture Center', 22, 1068, 54)
txt('一起把城市玩出新花样', 22, 1152, 27, 700, family='Study CJK, Study Sans, sans-serif', lang='zh-Hans')
add('</g>')
add('</svg>')

OUT.mkdir(parents=True, exist_ok=True)
(OUT / 'raw.svg').write_text('\n'.join(parts), encoding='utf-8')
subprocess.run([sys.executable, str(ROOT / 'input-v2' / 'embed_fonts.py'), str(ROOT / 'input-v2' / 'fonts'), str(OUT / 'raw.svg'), str(OUT / 'poster.svg')], check=True)
