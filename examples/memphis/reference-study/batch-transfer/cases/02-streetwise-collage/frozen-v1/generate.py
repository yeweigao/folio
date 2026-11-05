from pathlib import Path
from html import escape

HERE = Path(__file__).resolve().parent
W, H = 900, 1200
C = dict(paper='#EAE8E6', ink='#19191D', blue='#008BCD', green='#087C4A', pink='#F68CBC', yellow='#FFDE00', red='#F52B20', purple='#76258D')
p = []
def add(s): p.append(s)
def rect(x,y,w,h,color):
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{C.get(color,color)}"/>')
def path(d,color,**attrs):
    a=' '.join(f'{k.replace("_","-")}="{v}"' for k,v in attrs.items())
    add(f'<path d="{d}" fill="{C.get(color,color)}" {a}/>')
def poly(points,color):
    add(f'<polygon points="{points}" fill="{C.get(color,color)}"/>')
def circle(x,y,r,color):
    add(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{C.get(color,color)}"/>')
def line(x1,y1,x2,y2,color,width):
    add(f'<path d="M{x1} {y1}L{x2} {y2}" fill="none" stroke="{C.get(color,color)}" stroke-width="{width}"/>')
def text(s,x,y,size,family='Study CJK',weight=900,spacing=None):
    a=f' letter-spacing="{spacing}"' if spacing is not None else ''
    add(f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" fill="{C["ink"]}"{a}>{escape(s)}</text>')
def clip(name,x,y,w,h):
    add(f'<clipPath id="{name}"><rect x="{x}" y="{y}" width="{w}" height="{h}"/></clipPath>')
def begin(name): add(f'<g clip-path="url(#{name})">')
def end(): add('</g>')

add('<svg xmlns="http://www.w3.org/2000/svg" width="900" height="1200" viewBox="0 0 900 1200" role="img" aria-labelledby="poster-title poster-description">')
add('<title id="poster-title">集合散步 — CITY WALKS</title>')
add('<desc id="poster-description">在城里发现。Small discoveries, shared streets. 2027.05.14–05.16，河岸街区，一起走进街角的日常。</desc>')
add('<!-- FONTS -->')
add('<metadata>Native editable SVG. Text pairs: #19191D on #EAE8E6; #19191D on #FFDE00. Canvas 900 × 1200.</metadata>')
add('<defs>')
clip('top-bars',300,0,150,150)
clip('top-grid',450,0,450,150)
clip('slants',150,150,300,150)
clip('right-bars',750,600,150,300)
clip('bottom-slants',0,900,150,300)
clip('lower-semis',600,1050,300,150)
add('</defs>')
rect(0,0,W,H,'paper')

# Upper horizontal block, narrow upright, and long fine grid.
rect(0,0,300,150,'yellow')
for x in (24,150):
    poly(f'{x},28 {x+43},28 {x+99},75 {x+43},122 {x},122 {x+56},75','ink')
rect(300,0,150,150,'ink')
begin('top-bars')
for x in range(311,450,30): rect(x,0,14,150,'paper')
end()
rect(450,0,450,150,'blue')
begin('top-grid')
for x in range(450,901,30): line(x,0,x,150,'ink',1.5)
for y in range(0,151,30): line(450,y,900,y,'ink',1.5)
end()

# Short square, merged horizontal slants, and a two-storey diamond strip.
rect(0,150,150,150,'purple')
path('M75 168 C75 207 57 225 18 225 C57 225 75 243 75 282 C75 243 93 225 132 225 C93 225 75 207 75 168Z','yellow')
rect(150,150,300,150,'pink')
begin('slants')
for x in range(65,485,64):
    poly(f'{x},300 {x+37},300 {x+137},150 {x+100},150','ink')
end()
rect(450,150,150,300,'green')
for cy in (225,375):
    poly(f'525,{cy-57} 582,{cy} 525,{cy+57} 468,{cy}','yellow')

# One large disk crosses a single color boundary.
rect(600,150,300,150,'red')
rect(600,300,300,150,'purple')
circle(750,300,123,'paper')

# The principal intersection is a complete solid module.
rect(0,300,450,300,'paper')
text('集合散步',24,411,100)
text('在城里发现',26,468,41,weight=700)
text('CITY WALKS',27,542,68,'Study Condensed',700,1.0)
text('Small discoveries, shared streets.',27,577,21,'Study Sans',400)

rect(450,450,450,150,'green')
for x in (478,616,754):
    poly(f'{x+102},478 {x+59},478 {x+3},525 {x+59},572 {x+102},572 {x+46},525','pink')

# Lower blocks alternate square, strip and double-height spans.
rect(0,600,150,300,'red')
path('M18 675 A57 57 0 0 1 132 675Z','paper')
path('M18 825 A57 57 0 0 1 132 825Z','paper')
rect(150,600,300,150,'yellow')
for cx in (225,375):
    poly(f'{cx},618 {cx+57},675 {cx},732 {cx-57},675','ink')
rect(150,750,300,150,'blue')
circle(300,825,57,'paper')
rect(450,600,300,300,'pink')
for x in range(450,751,25): line(x,600,x,900,'ink',1.25)
for y in range(600,901,25): line(450,y,750,y,'ink',1.25)
rect(750,600,150,300,'paper')
begin('right-bars')
for x in range(750,901,38): rect(x,600,20,300,'ink')
end()

rect(0,900,150,300,'purple')
begin('bottom-slants')
for y in range(774,1250,66):
    poly(f'0,{y} 0,{y+35} 150,{y+135} 150,{y+100}','yellow')
end()
rect(150,900,300,300,'green')
circle(300,1050,132,'pink')

# Event facts share an axis and one reading size.
rect(450,900,450,150,'yellow')
text('2027.05.14–05.16',477,939,25,'Study Sans',700)
text('河岸街区',477,978,25,weight=700)
text('一起走进街角的日常',477,1017,25,weight=700)

rect(450,1050,150,150,'red')
path('M525 1068 C525 1107 507 1125 468 1125 C507 1125 525 1143 525 1182 C525 1143 543 1125 582 1125 C543 1125 525 1107 525 1068Z','paper')
rect(600,1050,300,150,'ink')
begin('lower-semis')
path('M600 1050 A150 150 0 0 0 900 1050Z','paper')
end()
add('</svg>')
(HERE/'raw.svg').write_text('\n'.join(p)+'\n')
