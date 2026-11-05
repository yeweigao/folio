#!/usr/bin/env python3
"""Draw the original 900 × 1200 character collage as editable SVG."""
from pathlib import Path
import math
import xml.sax.saxutils as xml

OUT = Path(__file__).resolve().parent
WHITE, BLACK, RED, PINK, YELLOW, BLUE = (
    '#FFFFFF', '#030303', '#FF354A', '#FD8CE5', '#FFE42C', '#1768F6'
)
art = []

def add(s):
    art.append(s)

def rect(x, y, w, h, color, **attrs):
    a = ' '.join(f'{k.replace("_", "-")}="{v}"' for k,v in attrs.items())
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{color}" {a}/>')

def path(d, fill, **attrs):
    a = ' '.join(f'{k.replace("_", "-")}="{v}"' for k,v in attrs.items())
    add(f'<path d="{d}" fill="{fill}" {a}/>')

def ellipse(cx, cy, rx, ry, color, **attrs):
    a = ' '.join(f'{k.replace("_", "-")}="{v}"' for k,v in attrs.items())
    add(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{color}" {a}/>')

def text(x, y, value, size, weight=900, family='Study Sans', **attrs):
    a = ' '.join(f'{k.replace("_", "-")}="{v}"' for k,v in attrs.items())
    add(f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" fill="{BLACK}" {a}>{xml.escape(value)}</text>')

def burst(cx, cy, inner, outer, n, rotation=0):
    pts = []
    for i in range(n*2):
        angle = rotation + math.pi*i/n
        r = outer if i % 2 == 0 else inner
        pts.append((cx+math.cos(angle)*r, cy+math.sin(angle)*r))
    return 'M'+' L'.join(f'{x:.2f},{y:.2f}' for x,y in pts)+' Z'

add('<svg xmlns="http://www.w3.org/2000/svg" width="900" height="1200" viewBox="0 0 900 1200" role="img" aria-labelledby="poster-title poster-description">')
add('<title id="poster-title">TTXC 2027 — 城市游乐场 · City Play!</title>')
add('<desc id="poster-description">A culture and technology event poster with three original monster characters, striped and radiating pattern tiles, a white bilingual theme band, and red event information panel.</desc>')
add('<!-- FONTS -->')
add('<defs>')
for name, x,y,w,h in [('bend',0,0,340,300),('rays',340,0,335,200),('teeth',675,0,225,305),('stripes',0,300,340,200),('jelly',340,200,335,300),('facets',675,305,225,195)]:
    add(f'<clipPath id="clip-{name}"><rect x="{x}" y="{y}" width="{w}" height="{h}"/></clipPath>')
add('</defs>')
rect(0,0,900,1200,WHITE)

# A single-eyed, bent soft body. Its winding silhouette reaches four tile edges.
add('<g clip-path="url(#clip-bend)">')
rect(0,0,340,300,BLUE)
path('M-27 264 C-11 237 13 210 42 197 C76 180 67 140 64 106 C59 59 94 15 148 16 C199 17 211 56 233 83 C255 110 283 95 314 111 C350 129 363 168 337 194 C308 224 283 199 260 204 C226 211 239 254 203 275 C161 302 132 276 112 249 C89 219 76 225 59 245 C34 274 2 292-27 264 Z',PINK)
ellipse(158,110,45,56,WHITE,transform='rotate(-17 158 110)')
ellipse(171,113,20,31,BLACK,transform='rotate(-17 171 113)')
ellipse(177,103,5,8,WHITE,transform='rotate(-17 177 103)')
path('M141 191 C157 207 184 206 199 188','none',stroke=BLACK,stroke_width=12,stroke_linecap='round')
add('</g>')

# Fine rods, separate from the figurative tiles.
add('<g clip-path="url(#clip-rays)">')
rect(340,0,335,200,YELLOW)
for i in range(44):
    a = i*math.tau/44 + .014
    x1,y1=507.5+math.cos(a)*23,100+math.sin(a)*23
    x2,y2=507.5+math.cos(a)*235,100+math.sin(a)*235
    path(f'M{x1:.2f} {y1:.2f} L{x2:.2f} {y2:.2f}','none',stroke=BLACK,stroke_width=3.3)
path(burst(507.5,100,23,76,11,-math.pi/2),PINK)
ellipse(507.5,100,10,10,BLACK)
add('</g>')

# The second creature is black, angular and toothy, with unequal eyes.
add('<g clip-path="url(#clip-teeth)">')
rect(675,0,225,305,PINK)
path('M673 299 L690 266 C680 245 671 236 677 219 L692 197 C678 177 684 161 699 148 L690 123 L711 111 C703 87 705 65 723 44 L737 58 C741 20 762 2 780-12 L792 32 C811 17 830 22 842 45 L861 23 C872 39 878 60 873 80 L902 75 L896 115 C919 133 921 160 909 184 L925 210 L905 228 C911 251 903 269 888 279 L905 310 L852 316 L825 288 L801 312 L766 296 L735 320 Z',BLACK)
ellipse(745,108,19,30,WHITE,transform='rotate(-11 745 108)')
ellipse(745,115,9,15,BLACK)
ellipse(840,119,28,22,WHITE,transform='rotate(13 840 119)')
ellipse(830,123,12,12,BLACK)
path('M711 179 Q789 151 872 185 L863 241 Q785 269 718 233 Z',RED)
path('M716 178 L744 171 L742 199 L725 201 Z M759 168 L786 166 L784 198 L764 197 Z M804 168 L830 172 L823 202 L805 200 Z M847 176 L870 184 L862 208 L844 202 Z',WHITE)
path('M726 239 L747 246 L751 222 L735 218 Z M771 251 L796 253 L793 224 L775 223 Z M817 250 L840 245 L834 219 L818 222 Z M852 242 L865 237 L864 220 L852 223 Z',WHITE)
add('</g>')

# Closely spaced diagonal strokes form the lower-left pattern module.
add('<g clip-path="url(#clip-stripes)">')
rect(0,300,340,200,RED)
for x in range(-230,400,24):
    path(f'M{x} 504 L{x+210} 294','none',stroke=BLACK,stroke_width=9)
add('</g>')

# A low-domed jellyfish with a circular mouth and five independent tentacles.
add('<g clip-path="url(#clip-jelly)">')
rect(340,200,335,300,YELLOW)
for d in [
    'M389 352 C379 391 409 405 389 438 C371 469 381 488 398 511',
    'M439 365 C457 396 417 420 439 448 C459 473 442 492 435 514',
    'M501 367 C488 403 519 419 500 448 C483 473 504 489 505 514',
    'M558 363 C576 396 541 416 561 448 C581 478 565 489 554 513',
    'M611 350 C598 390 626 409 607 440 C587 471 621 493 622 511',
]:
    path(d,'none',stroke=BLUE,stroke_width=24,stroke_linecap='round')
path('M362 360 C366 292 408 228 483 222 C560 214 629 260 653 356 C639 376 622 379 605 363 C585 384 567 385 548 368 C530 386 510 386 492 368 C472 385 451 383 434 365 C411 381 392 379 376 363 Z',BLUE)
ellipse(440,292,13,25,WHITE,transform='rotate(12 440 292)')
ellipse(439,296,5,17,BLACK,transform='rotate(12 439 296)')
ellipse(559,293,13,25,WHITE,transform='rotate(-12 559 293)')
ellipse(560,297,5,17,BLACK,transform='rotate(-12 560 297)')
ellipse(500,329,31,39,BLACK)
ellipse(500,338,13,20,PINK)
add('</g>')

# Cut hexagonal sectors fill the small remaining module without becoming a face.
add('<g clip-path="url(#clip-facets)">')
rect(675,305,225,195,BLUE)
path('M784 312 L875 359 L875 448 L784 496 L693 448 L693 359 Z',PINK)
path('M784 312 L784 404 L875 359 Z',BLACK)
path('M784 404 L875 448 L784 496 Z',BLACK)
path('M784 404 L693 448 L693 359 Z',BLACK)
path('M784 337 L850 371 L850 434 L784 470 L718 434 L718 371 Z','none',stroke=BLUE,stroke_width=8)
ellipse(784,404,18,18,YELLOW)
add('</g>')

# A clean white recognition band separates the collage from event information.
rect(0,500,900,240,WHITE)
text(26,610,'城市游乐场',112,family='Study CJK')
text(26,717,'City Play!',100,letter_spacing='-3')
add(f'<text x="626" y="665" font-family="Study Sans" font-size="24" font-weight="700" fill="{BLACK}"><tspan x="626" y="665">ART × SOUND × </tspan><tspan x="626" y="698">TECHNOLOGY</tspan></text>')

# Information is aligned on one generous axis over a continuous red field.
rect(0,740,900,460,RED)
text(25,876,'TTXC 2027',150,letter_spacing='-1.2')
text(30,935,'一起把城市玩出新花样',35,700,family='Study CJK',letter_spacing='1')
text(26,1062,'2027.09.10–12',110,letter_spacing='-2')
text(30,1132,'海岸文化中心',43,900,family='Study CJK')
text(31,1173,'Coast Culture Center',29,700,letter_spacing='-.3')
add('</svg>')

OUT.mkdir(parents=True,exist_ok=True)
(OUT/'raw.svg').write_text('\n'.join(art),encoding='utf-8')
print(OUT/'raw.svg')
