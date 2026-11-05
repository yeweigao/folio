#!/usr/bin/env python3
"""Vector reconstruction studies from the three user-supplied reference boards.

No reference pixels are used in the generated artwork. Coordinates are reconstruction
decisions, not a proposed design system. DESIGN.md is extracted only after review.
"""
from pathlib import Path
from html import escape
import json, math, re

ROOT = Path(__file__).resolve().parent
UNITS = []
FONTS = '''
@font-face{font-family:Study Sans;src:url(../assets/sans-400.woff2);font-weight:400}
@font-face{font-family:Study Sans;src:url(../assets/sans-700.woff2);font-weight:700}
@font-face{font-family:Study Sans;src:url(../assets/sans-900.woff2);font-weight:900}
@font-face{font-family:Study Light;src:url(../assets/light.woff2);font-weight:100 900}
@font-face{font-family:Study CJK;src:url(../assets/cjk.woff2);font-weight:100 900}
@font-face{font-family:Study Condensed;src:url(../assets/condensed.woff2);font-weight:700}
@font-face{font-family:Study Pixel;src:url(../assets/pixel.woff2);font-weight:400}
text{font-family:'Study Sans','Study CJK',sans-serif}
'''

class SVG:
    def __init__(self,w,h,bg):
        self.w,self.h,self.a,self.n=w,h,[],0
        self.rect(0,0,w,h,bg)
    def add(self,s): self.a.append(s)
    def rect(self,x,y,w,h,c,stroke=None,sw=1,rx=0):
        self.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{c}"'+(f' stroke="{stroke}" stroke-width="{sw}"' if stroke else '')+'/>')
    def circle(self,x,y,r,c,stroke=None,sw=1):
        self.add(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}"'+(f' stroke="{stroke}" stroke-width="{sw}"' if stroke else '')+'/>')
    def ellipse(self,x,y,rx,ry,c,stroke=None,sw=1):
        self.add(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{c}"'+(f' stroke="{stroke}" stroke-width="{sw}"' if stroke else '')+'/>')
    def path(self,d,c,stroke=None,sw=1):
        self.add(f'<path d="{d}" fill="{c}"'+(f' stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"' if stroke else '')+'/>')
    def poly(self,points,c,stroke=None,sw=1):
        self.path('M'+'L'.join(f'{x},{y}' for x,y in points)+'Z',c,stroke,sw)
    def line(self,x1,y1,x2,y2,c,sw=1):
        self.add(f'<path d="M{x1},{y1}L{x2},{y2}" fill="none" stroke="{c}" stroke-width="{sw}"/>')
    def text(self,x,y,s,size=28,c='#111111',weight=400,family=None,anchor=None,width=None,transform=None,spacing=None):
        attrs = f' x="{x}" y="{y}" fill="{c}" font-size="{size}" font-weight="{weight}"'
        if family: attrs+=f' style="font-family:\'{family}\',\'Study CJK\',sans-serif"'
        if anchor: attrs+=f' text-anchor="{anchor}"'
        if width: attrs+=f' textLength="{width}" lengthAdjust="spacingAndGlyphs"'
        if transform: attrs+=f' transform="{transform}"'
        if spacing is not None: attrs+=f' letter-spacing="{spacing}"'
        self.add(f'<text{attrs}>{escape(s)}</text>')
    def lines(self,x,y,ls,size=24,c='#111111',weight=400,leading=1.2,**kw):
        for i,s in enumerate(ls): self.text(x,y+i*size*leading,s,size,c,weight,**kw)
    def group(self,x=0,y=0,scale=1,rotate=0): self.add(f'<g transform="translate({x} {y}) scale({scale}) rotate({rotate})">')
    def end(self): self.add('</g>')
    def clip(self,x,y,w,h):
        self.n+=1; key=f'c{self.n}'
        self.add(f'<defs><clipPath id="{key}"><rect x="{x}" y="{y}" width="{w}" height="{h}"/></clipPath></defs><g clip-path="url(#{key})">')
    def save(self,group,name,title):
        p=ROOT/group/(name+'.svg');p.parent.mkdir(parents=True,exist_ok=True)
        p.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}" height="{self.h}" viewBox="0 0 {self.w} {self.h}" role="img" aria-label="{escape(title)}"><title>{escape(title)}</title><style>{FONTS}</style>'+''.join(self.a)+'</svg>')
        UNITS.append(dict(group=group,name=name,title=title,width=self.w,height=self.h,file=f'{group}/{name}.svg'))

def flower(s,x,y,r,c,n=6,inner=.44):
    # Smooth radial petals: a constructed motif, not traced raster art.
    p=[]
    for i in range(240):
        a=i*math.tau/240; rr=r*(inner+(1-inner)*(1+math.cos(n*a))/2)
        p.append((x+rr*math.cos(a),y+rr*math.sin(a)))
    s.poly(p,c)

def star(s,x,y,r,c,n=8,inner=.60):
    s.poly([(x+(r if i%2==0 else r*inner)*math.cos(i*math.pi/n-math.pi/2),y+(r if i%2==0 else r*inner)*math.sin(i*math.pi/n-math.pi/2)) for i in range(n*2)],c)

def tile(s,x,y,z,kind,bg,fg,alt=None,rotation=0):
    s.group(x,y,z/100)
    s.clip(0,0,100,100);s.rect(0,0,100,100,bg)
    s.group(50,50,1,rotation);s.group(-50,-50)
    if kind=='flower': flower(s,50,50,43,fg,6,.44)
    elif kind=='scallop': flower(s,50,50,48,fg,16,.86)
    elif kind=='star': flower(s,50,50,48,fg,8,.67)
    elif kind=='cross':
        for a in [45,-45]:
            s.add(f'<ellipse cx="50" cy="50" rx="48" ry="15" fill="{fg}" transform="rotate({a} 50 50)"/>')
    elif kind=='clover':
        for xx,yy in [(26,26),(74,26),(26,74),(74,74)]:s.circle(xx,yy,24,fg)
    elif kind=='leaf':s.path('M18 18H61Q82 18 82 39V82H39Q18 82 18 61Z',fg)
    elif kind=='quarter':s.path('M100 0V100H0A100 100 0 0 1 100 0Z',fg)
    elif kind=='round':s.path('M100 20H64Q20 20 20 64V100H100Z',fg)
    elif kind=='fourarc':
        for xx,yy in [(0,0),(100,0),(0,100),(100,100)]:s.circle(xx,yy,42,fg)
    elif kind=='corner':s.path('M0 0H100V100H62V62H0Z',fg)
    elif kind=='arc':
        s.circle(100,100,100,fg);s.circle(100,100,52,alt or bg)
    elif kind=='half':s.path('M0 0H100V100H0Z',bg);s.path('M0 0A100 100 0 0 1 0 200Z',fg)
    elif kind=='disc':s.circle(50,50,48,fg)
    elif kind=='diamond':s.poly([(50,0),(100,50),(50,100),(0,50)],fg)
    elif kind=='spark':s.path('M50 0Q53 47 100 50Q53 53 50 100Q47 53 0 50Q47 47 50 0Z',fg)
    elif kind=='stripe':
        for i in range(-150,200,25):s.poly([(i,0),(i+13,0),(i+113,100),(i+100,100)],fg)
    elif kind=='checks':
        for i in range(5):
            for j in range(5):
                if (i+j)%2==0:s.rect(i*20,j*20,20,20,fg)
    elif kind=='grid':
        for i in range(0,101,25):s.line(i,0,i,100,fg,5);s.line(0,i,100,i,fg,5)
    elif kind=='chevron':s.poly([(0,0),(42,0),(100,50),(42,100),(0,100),(59,50)],fg)
    elif kind=='triangles':
        for i in range(3):s.poly([(i*34,100),(i*34+34,0),(i*34+34,100)],fg)
    elif kind=='dots':
        for i in range(3):
            for j in range(3):s.circle(20+30*i,20+30*j,10,fg)
    s.end();s.end();s.end();s.end()

B='#343D9F';P='#FA0056';O='#FF7619';C='#FFE5A6';W='#F8F6ED'
KIT=[('leaf',W,P),('flower',P,W),('star',C,B),('clover',B,W),('scallop',P,B),('round',C,P),('cross',O,B),('arc',P,B)]
def tiles(s,x,y,z,n,offset=0):
    for i in range(n):
        k,b,f=KIT[(offset+i)%len(KIT)];tile(s,x+i*z,y,z,k,b,f,O)
def header(s):
    s.lines(40,55,['Aditya Ramlan','NIK: 123456789'],14,W,leading=1.15)
    s.lines(278,55,['SMK Inspirasi Bangsa','Tahun 2032/2033'],14,W,leading=1.15)
    flower(s,1220,60,24,W,4,.55)
def paragraph(s,x,y,kind='profile',color=W):
    texts={
    'profile':['Lengkapi bagian ini dengan','menjelaskan perusahaan tempat','praktik kerja. Tuliskan nama, bidang','usaha, lokasi dan gambaran singkat','perusahaan atau instansi tempat PKL.','Anda juga bisa menambahkan visi','atau layanan utamanya jika relevan.'],
    'background':['Jelaskan latar belakang','dilaksanakannya PKL dan kaitannya','dengan pembelajaran di sekolah.','Uraikan maksud dan tujuannya.'],
    'vision':['Tuliskan apa yang menjadi visi','perusahaan tempat PKL di sini. Tuliskan','apa yang menjadi visi perusahaan','tempat PKL di sini.'],
    'history':['Jelaskan salah satu peristiwa','atau kegiatan yang menjadi','tonggak penting perusahaan','PKL di bagian ini.'],
    'job':['Jelaskan divisi atau bagian tempat kamu','ditempatkan selama PKL serta perannya dalam','perusahaan. Sebutkan pula posisi atau fokus','pekerjaan yang kamu pelajari.'],
    'task':['Rangkum tugas utama yang kamu','lakukan, baik harian maupun berkala.','Gunakan poin-poin singkat dan','tambahkan contoh pekerjaan agar','kontribusi Anda lebih mudah dipahami.']}
    s.lines(x,y,texts[kind],15,color,leading=1.35)

def slides():
    s=SVG(1280,720,B)
    for j in range(4):
        for i in range(2):
            k,b,f=[('scallop',P,B),('leaf',W,P),('round',C,O),('flower',P,W),('cross',B,P),('star',C,B),('clover',P,W),('arc',O,B)][j*2+i]
            tile(s,i*180,j*180,180,k,b,f,O)
    s.rect(360,540,920,180,P)
    s.lines(400,118,['Laporan Hasil Praktik Kerja Lapangan','(PKL) Digdaya Komunikasi'],22,W,leading=1.1)
    s.line(400,178,1245,178,W,1)
    s.text(395,302,'Laporan Hasil',98,W,100,'Study Light',width=595)
    s.text(395,394,'Kreativitas Praktik',94,W,700,width=840)
    s.text(395,486,'Kerja Lapangan',94,W,700,width=760)
    s.lines(400,649,['Aditya Ramlan','NIK: 123456789'],15,W,leading=1.8)
    s.lines(1070,649,['SMK Inspirasi Bangsa','Tahun 2032/2033'],15,W,leading=1.8)
    flower(s,1220,60,24,W,4,.55)
    s.save('slides','01-cover','Laporan Hasil · Cover')
    s=SVG(1280,720,P);header(s)
    s.text(40,405,'Daftar',98,W,100,'Study Light');s.text(40,500,'Isi',98,W,700)
    s.line(460,140,460,500,W,1)
    items=[('01','Latar belakang','& tujuan'),('02','Alur','kerja'),('03','Profil','perusahaan'),('04','Dokumentasi','kegiatan'),('05','Bidang','pekerjaan'),('06','Pencapaian',''),('07','Tugas dan','tanggung jawab'),('08','Saran &','Kesimpulan')]
    for i,(num,l1,l2) in enumerate(items):
        col=0 if i in [0,2] else 1 if i in [1,3,4,6] else 2
        row=0 if i<2 else 1 if i<4 else 2 if i<6 else 3
        x=[524,775,1025][col];y=177+108*row
        s.text(x,y,num,52,W,100,'Study Light');s.lines(x+90,y-20,[l1,l2],14,W,leading=1.4)
    for i,(k,b,f,a) in enumerate([('clover',B,W,None),('arc',O,C,O),('cross',B,P,None),('star',C,B,None),('round',O,P,None),('flower',B,W,None),('leaf',W,P,None),('scallop',P,B,None)]):tile(s,i*160,562,160,k,b,f,a)
    s.save('slides','02-contents','Daftar Isi')
    s=SVG(1280,720,B);s.rect(0,0,500,720,O);header(s)
    for i,(k,b,f) in enumerate([('scallop',P,O),('leaf',W,B),('flower',B,P),('round',P,O),('star',C,B)]):tile(s,500,i*144,144,k,b,f,rotation=90 if i==3 else 0)
    s.text(40,348,'Latar',72,B,100,'Study Light');s.text(40,415,'Belakang',72,B,700)
    s.line(680,430,1245,430,W,1);paragraph(s,680,530,'background');paragraph(s,970,610,'background')
    s.save('slides','03-background','Latar Belakang')
    s=SVG(1280,720,B);header(s)
    for i in range(8):
        k,b,f=[*KIT[:5],('round',C,O),('cross',O,C),('arc',P,C)][i];tile(s,(i%4)*138,144+(i//4)*138,138,k,b,f,O)
    s.text(625,205,'Profil',76,W,100,'Study Light');s.text(625,270,'Perusahaan',76,W,700,width=425)
    s.line(625,420,1240,420,W,1);paragraph(s,625,548);paragraph(s,955,548)
    s.save('slides','04-profile','Profil Perusahaan')
    s=SVG(1280,720,P);header(s)
    s.text(40,210,'Visi & Misi',74,W,100,'Study Light');s.text(40,276,'Perusahaan',74,W,700,width=455)
    for i in range(6):
        k,b,f=[('cross',O,P),('round',W,B),('scallop',B,P),('star',C,B),('flower',P,C),('leaf',O,C)][i]
        tile(s,40+(i%3)*135,450+(i//3)*135,135,k,b,f)
    s.lines(565,190,['Visi','Perusahaan'],38,W,100,leading=1.0,family='Study Light');paragraph(s,565,303,'vision')
    s.line(906,150,906,683,W,1)
    s.lines(958,400,['Misi','Perusahaan'],38,W,100,leading=1.0,family='Study Light')
    for i in range(3):
        tile(s,947,506+i*65,22,'cross',P,C)
        s.lines(1000,518+i*65,['Tuliskan apa yang menjadi visi','perusahaan tempat PKL di sini.'],14,W,leading=1.3)
    s.save('slides','05-vision','Visi & Misi Perusahaan')
    s=SVG(1280,720,B);header(s);tiles(s,0,124,160,8)
    s.text(40,385,'Sejarah',74,W,100,'Study Light');s.text(272,385,'Perusahaan',74,W,700,width=414)
    s.line(40,432,1240,432,W,1)
    for i,year in enumerate(['Th. 2000','Th. 2015','Th. 2020','Th. 2030']):
        x=40+i*323;tile(s,x,470,22,'cross',B,C)
        s.text(x,560,year,39,W,100,'Study Light');paragraph(s,x,602,'history')
    s.save('slides','06-history','Sejarah Perusahaan')
    s=SVG(1280,720,B);header(s);s.rect(0,440,1280,280,P)
    s.text(505,177,'Bidang',74,W,100,'Study Light');s.text(505,242,'Pekerjaan',74,W,700)
    tiles(s,0,300,142.23,8);tile(s,1137.84,300,142.23,'fourarc',O,C)
    s.lines(505,490,['Branding &','Identitas Visual'],38,W,100,leading=1.0,family='Study Light')
    s.lines(900,490,['Content','Design'],38,W,100,leading=1.0,family='Study Light')
    paragraph(s,505,607,'job');paragraph(s,900,607,'job')
    s.save('slides','07-work','Bidang Pekerjaan')
    s=SVG(1280,720,B);header(s)
    s.text(40,245,'Tugas &',74,W,100,'Study Light');s.lines(40,310,['Tanggung','Jawab'],74,W,700,leading=.94)
    for i in range(8):
        k,b,f=[('clover',O,B),('arc',P,C),('star',C,P),('cross',O,C),('flower',P,W),('round',C,B),('leaf',W,P),('scallop',P,B)][i];tile(s,454+(i%2)*138,172+(i//2)*138,138,k,b,f,O)
    s.line(802,172,1240,172,W,1)
    for i in range(3):
        y=242+i*184;s.lines(803,y,['Tugas',f'     0{i+1}'],38,W,100,leading=1.0,family='Study Light');paragraph(s,944,y-15,'task')
    s.save('slides','08-responsibilities','Tugas & Tanggung Jawab')

def collection():
    s=SVG(900,1200,'#EAE8E6')
    blue='#008BCD';green='#087C4A';pink='#F68CBC';yellow='#FFDE00';red='#F52B20';purple='#76258D';ink='#19191D'
    paper='#EAE8E6'
    s.rect(0,0,225,64,green);s.rect(0,64,225,86,blue)
    s.rect(225,0,75,150,paper);s.poly([(225,0),(300,75),(225,150)],blue);s.poly([(262,37),(300,75),(262,113)],ink)
    tile(s,300,0,150,'chevron',purple,paper);tile(s,450,0,150,'diamond',blue,paper);tile(s,600,0,150,'disc',yellow,pink);tile(s,750,0,150,'grid',paper,ink)
    s.rect(450,150,300,150,pink)
    for i in range(4):s.poly([(450+i*75,225),(525+i*75,150),(525+i*75,225),(450+i*75,300)],green)
    tile(s,750,150,150,'spark','#114B97',paper)
    tile(s,300,300,150,'spark',green,paper)
    s.rect(0,590,225,225,yellow);s.rect(0,590,225,111,O);s.circle(112,702,108,red)
    s.rect(225,590,113,225,pink);s.poly([(225,590),(338,646),(225,646)],yellow);s.poly([(225,646),(338,646),(225,702)],yellow);s.rect(225,702,113,113,blue)
    tile(s,338,590,112,'chevron',ink,paper,rotation=90);s.rect(338,702,112,113,O);s.circle(394,757,43,yellow)
    s.rect(450,590,112,112,red);tile(s,450,702,112,'diamond',O,paper)
    for j in range(2):
        for i in range(4):s.poly([(562+i*56,702+j*56),(618+i*56,590+j*112),(618+i*56,702+j*56)],blue)
    s.rect(562,590,225,112,green)
    for i in range(4):s.poly([(562+i*56,702),(618+i*56,590),(618+i*56,702)],'#1845A0')
    tile(s,787,590,113,'chevron',ink,paper,rotation=270);tile(s,787,702,113,'chevron',ink,paper,rotation=270)
    s.rect(0,815,150,340,'#0C59AB');s.clip(0,815,150,340)
    for y in range(750,1200,90):s.poly([(0,y),(150,y-100),(150,y-65),(0,y+35)],ink)
    s.end();s.rect(150,815,150,150,pink);s.rect(300,815,150,150,ink)
    for x in range(311,450,31):s.rect(x,815,12,150,paper)
    s.rect(150,965,150,190,green);s.rect(300,965,150,190,paper);s.clip(150,965,300,190);s.circle(300,1155,170,ink);s.circle(300,1155,156,paper);s.rect(150,965,150,190,ink);s.end()
    tile(s,600,965,150,'chevron',O,paper,rotation=180);s.rect(750,965,150,75,red);s.rect(750,1040,150,75,O)
    for i in range(3):tile(s,450+i*150,1115,150,['chevron','arc','quarter'][i],yellow if i==0 else green,O if i==0 else blue)
    s.rect(0,150,450,150,'#EAE8E6');s.text(24,204,'COLLECTION OF ACTS',36,ink,900,width=410);s.text(24,272,'Streetwise',40,ink)
    s.rect(450,300,450,300,'#EAE8E6')
    s.text(470,407,'集合行動',99,ink,900,width=408);s.text(470,516,'街頭小事',97,ink,400,width=410)
    s.text(472,582,'2019.5.16–5.19',23,ink,900);s.text(884,582,'策展人：王志豪',17,ink,700,anchor='end')
    tile(s,0,300,300,'stripe','#FD4138','#FF7B1A')
    tile(s,0,450,150,'disc',pink,'#F4E7E7');s.circle(75,525,43,pink)
    s.rect(150,450,300,150,yellow);s.clip(150,450,300,150)
    for i in range(-100,400,48):s.poly([(150+i,600),(174+i,600),(324+i,450),(300+i,450)],ink)
    s.end()
    s.rect(450,825,450,150,'#EAE8E6');s.text(470,885,'一場街頭的聚會!',52,ink,900,width=410);s.text(470,949,'Meet at The Corner!',37,ink)
    tile(s,450,975,150,'grid','#EAE8E6',ink)
    s.rect(0,1155,450,45,'#EAE8E6');s.text(22,1187,'XINTIANDI   S019',25,ink,700,spacing=2)
    s.save('posters','01-collection-of-acts','Collection of Acts · 街頭小事')

def new_design():
    s=SVG(900,1200,'#FFCB37');s.rect(20,24,860,1158,'#060605')
    s.rect(24,26,420,1154,'#07964F');s.rect(24,26,348,400,'#F3579D')
    s.path('M24 26H145V280Q145 417 24 427Z','#F3579D');s.path('M372 26H445V281Q445 412 372 427Z','#F3579D')
    s.rect(116,113,165,370,'#07964F')
    s.lines(130,152,['张左','程一'],29,'#FCFCF1',400,leading=1.0)
    s.text(143,191,'ZHANGCHENG',16,'#FFFFFF',transform='rotate(90 143 191)')
    s.text(181,191,'ZUOYI',16,'#FFFFFF',transform='rotate(90 181 191)')
    s.text(208,151,'策',22,'#FFFFFF');s.text(208,178,'展',22,'#FFFFFF');s.text(208,205,'人',22,'#FFFFFF')
    # The giant constructed character is a solid figure occupying the left field.
    s.path('M24 570Q24 470 126 470H390V590H312V850H215V590H126V850H24Z','#FFFDF3')
    s.path('M198 675A83 83 0 0 0 198 840Z','#FFFDF3')
    s.rect(444,26,415,166,'#0759FD')
    for i in range(5):
        x=444+i*83;s.path(f'M{x} 26Q{x+83} 26 {x+83} 109Q{x+83} 192 {x} 192Z','#050505')
    tile(s,444,109,166,'quarter','#0759FD','#07964F')
    tile(s,610,109,249,'half','#050505','#FF7829',rotation=90)
    s.rect(444,275,166,36,'#FFFFFF');s.rect(444,311,166,38,'#0759FD')
    for i,c in enumerate(['#FFFFFF','#F3579D','#FFFFFF','#FFE745']):s.circle(475+i*62,354,23,c)
    for i in range(12):s.rect(690+i*14,321,8,58,['#F3579D','#07964F'][i%2])
    s.lines(448,428,['22  AUGUST','30  DECEMBER','      09:00 — 17:00'],43,'#FFFFFF',700,leading=.98)
    # Three cut staves, each with the same scoop: lettering as geometry.
    for x in [485,642,766]:
        s.path(f'M{x} 516H{x+125}V710Q{x+125} 838 {x+12} 858V622H{x}Z','#9B38ED')
    s.path('M515 901H860Q850 996 726 996H652Q535 991 515 901Z','#FF7829')
    s.path('M652 996H725V1032Q852 1032 859 1158H514Q523 1032 652 1032Z','#FF7829');s.ellipse(688,1120,38,22,'#050505')
    s.text(24,958,'新锐设计展',68,'#FFF035',900,width=400)
    s.lines(24,1026,['NEW DESIGN','EXHIBITION'],53,'#071A0D',900,leading=1.0)
    s.text(24,1192,'OP: 上海 K11',64,'#FFFFFF',900,width=410)
    s.save('posters','02-new-design','新锐设计展 · New Design Exhibition')

def tresor():
    s=SVG(900,1200,'#020202');blue='#0969F9';red='#FF3A06';white='#F9F9F6'
    s.rect(10,10,880,1178,white)
    s.rect(10,10,436,42,red);s.path('M220 52Q250 0 299 10H414L440 52Z',blue,'#000000',10)
    for x in [478,604,730,856]:
        s.circle(x,21,27,'#FFFFFF','#000000',7);s.text(x,31,'SA',22,'#000000',900,anchor='middle')
    s.rect(10,64,436,234,white,'#000000',10)
    s.lines(22,115,['Move D','Jus-Ed','B2B','all night long!'],52,'#000000',700,leading=.96)
    s.rect(10,298,436,238,blue,'#000000',10)
    s.path('M10 298H195Q194 465 10 419Z',red,'#000000',10)
    s.text(24,328,'GLOBUS',19,'#000000',700)
    s.path('M446 64H890V215Q800 247 730 260Q603 289 446 64Z','#000000')
    s.path('M446 299C610 207 579 444 446 393Z','#000000')
    s.poly([(10,536),(446,430),(446,536)],red,'#000000',10)
    s.rect(302,536,588,158,blue,'#000000',10)
    s.text(321,676,'TRESOR',21,'#000000',700)
    s.path('M10 541H302V914H10Z','#000000')
    s.path('M10 630Q155 600 134 760Q123 830 10 849Z',white)
    s.path('M302 541Q143 560 146 716Q148 825 302 858Z',white)
    s.rect(302,694,430,220,white,'#000000',10)
    s.lines(316,750,['Dustin Zahn','Takaaki Itoh','HGR'],55,'#000000',700,leading=1.02)
    s.path('M733 914V694Q780 614 832 665L890 914Z',red,'#000000',10)
    s.path('M758 746L820 914H890V694H733Z',blue,'#000000',10)
    s.rect(10,914,722,230,red,'#000000',10)
    s.path('M10 914H85Q-7 999 10 1044Z',blue,'#000000',10)
    s.path('M178 914H583V1060L331 1009Q224 1008 178 914Z',blue,'#000000',10)
    s.path('M732 914H605V1144H732Z','#000000')
    s.path('M12 1078L170 1144H12Z',white)
    s.path('M603 1068Q689 1077 732 1120V1144H603Z',white)
    s.rect(732,914,158,230,white,'#000000',10)
    s.circle(812,979,36,'none','#000000',13);s.circle(812,979,12,'#000000')
    s.line(775,1035,849,1035,'#000000',8);s.text(811,1072,'TRESOR',27,'#000000',900,anchor='middle');s.text(811,1094,'EST.1991',13,'#000000',700,anchor='middle')
    s.rect(10,1144,880,45,white,'#000000',10)
    s.text(20,1186,'09.12.17',47,'#000000',700);s.text(307,1175,'TRESOR.KLUBNACHT',18,'#000000',700);s.line(290,1144,290,1188,'#000000',10);s.line(668,1144,668,1188,'#000000',10);s.text(686,1186,'23:59',47,'#000000',700)
    s.save('posters','03-tresor','Tresor · Klubnacht')

def monster(s,x,y,z,bg,fg,kind=0):
    s.group(x,y,z/100);s.rect(0,0,100,100,bg)
    if kind==0:
        flower(s,50,50,45,fg,8,.82);s.circle(50,35,7,'#FFFFFF');s.circle(50,35,3,'#000000')
        for i in range(7):
            for j in range(2):s.circle(28+i*7,53+j*7,2.3,'#FFFFFF')
    elif kind==1:
        s.path('M20 49Q0 4 29 14Q50 -5 71 14Q100 4 80 49L94 70Q97 89 80 80L62 67Q82 98 64 94L47 68Q56 102 40 93L31 65Q5 91 13 64Z',fg)
        for xx in [31,69]:s.circle(xx,28,9,'#FFFFFF');s.circle(xx,28,5,'#000000')
    else:
        s.circle(50,41,28,fg);s.circle(43,27,5,'#FFFFFF');s.circle(43,27,2,'#000000')
        for i in range(6):s.path(f'M{25+i*9} 58Q{45+i*9} 77 {25+i*9} 95','none',fg,6)
        for i in range(8):s.circle(29+i*6,40,2,'#000000')
    s.end()

def txc():
    red='#FF354A';pink='#FD8CE5';yellow='#FFE42C';blue='#1768F6';black='#030303'
    s=SVG(900,1200,red)
    s.rect(0,0,334,285,red);s.rect(334,0,338,170,yellow);s.rect(672,0,228,170,black)
    s.path('M105 -20Q243 -30 193 58Q282 97 224 141Q285 240 195 278Q55 294 105 170Q42 108 117 75Q54 49 105 -20Z',blue)
    s.circle(165,205,36,'#FFFFFF');s.circle(165,205,20,black)
    for x in [35,266]:s.poly([(x,0),(x+36,0),(x+8,50),(x+35,45),(x,105),(x+2,56),(x-17,59)],yellow)
    for i in range(3):s.ellipse(380+i*93,-4,43,169,pink)
    monster(s,672,0,228,black,red,1)
    s.rect(334,170,338,338,blue)
    for r in [157,125,93]:
        s.ellipse(503,339,r,54,yellow);s.ellipse(503,339,54,r,yellow)
    s.circle(503,339,74,blue);s.circle(503,339,62,yellow)
    monster(s,334,170,113,'#000000','#000000',0)
    for i in range(2):
        for j in range(2):s.rect(559+i*56,58+j*56,56,56,[pink,blue][(i+j)%2])
    tile(s,0,285,220,'disc',blue,blue)
    for i in range(8):s.circle(110+73*math.cos(i*math.tau/8),395+73*math.sin(i*math.tau/8),19,[pink,yellow,red][i%3])
    s.rect(220,285,114,223,pink)
    for i in range(6):s.line(235,450,323,450,['#FF3845','#1768F6','#FFE42C'][i%3],8) if i==0 else None
    s.group(277,450)
    for i in range(6):s.line(-49,0,49,0,[red,blue,yellow][i%3],9);s.add('<g transform="rotate(30)">')
    for _ in range(6):s.end()
    s.end()
    s.rect(672,170,228,228,red);star(s,786,284,111,pink,14,.42)
    s.rect(672,398,228,110,black);s.text(686,467,'台灣文化科技大會',29,'#FFFFFF',900,width=200)
    s.rect(0,508,672,222,'#FFFFFF');s.text(40,642,'TTXC 2024',105,black,900,width=588)
    s.text(48,685,'TAIWAN TECHNOLOGY CULTURE EXPO',27,black,700,'Study Condensed',width=584)
    monster(s,672,508,228,red,black,0)
    monster(s,0,730,220,red,yellow,2)
    s.text(260,822,'Takao Rock!',77,black,900,width=605);s.text(260,922,'打狗祭',115,black,900,width=600)
    s.text(272,985,'2024.10.11–13',59,black,900,width=568)
    s.rect(0,980,220,220,pink)
    for i in range(6):
        a=i*math.tau/6;s.poly([(110+22*math.cos(a),1090+22*math.sin(a)),(110+98*math.cos(a-.35),1090+98*math.sin(a-.35)),(110+98*math.cos(a+.35),1090+98*math.sin(a+.35))],red)
    s.lines(270,1120,['高雄流行音樂中心','Kaohsiung Music Center'],24,black,700,leading=1.3)
    s.save('posters','04-ttxc','TTXC 2024 · Takao Rock!')

HB='#1900F5';HG='#00ECA9';HP='#FA4EF5';HY='#FBFF08';HR='#FF6977';HW='#FFFFF2'
def graph(s):
    s.rect(18,18,864,1164,HB)
    for x in range(18,883,49):s.line(x,18,x,1182,'#797BFF',1.2)
    for y in range(18,1183,49):s.line(18,y,882,y,'#797BFF',1.2)
def iso(s,x,y,w,h,dx,dy,front,top,side):
    s.poly([(x,y),(x+w,y),(x+w+dx,y+dy),(x+dx,y+dy)],top,HB,4)
    s.poly([(x+w,y),(x+w+dx,y+dy),(x+w+dx,y+h+dy),(x+w,y+h)],side,HB,4)
    s.rect(x,y,w,h,front,HB,4)
def starburst(s,x,y,r,c):star(s,x,y,r,c,10,.48)
def hack_windows():
    s=SVG(900,1200,'#FFFFFF');graph(s)
    # A strip of receding windows precedes the principal window.
    s.rect(80,95,270,330,HW)
    s.lines(112,155,['SF','SEA','DUB','SG'],52,HB,700,leading=.95,family='Study Condensed')
    for i in range(22,0,-1):s.rect(260+i*8,160-i*3,190,140,HW,HB,3)
    s.lines(265,209,['REMOTES','TOO, OFC!'],34,HB,700,leading=1.0,family='Study Condensed')
    iso(s,626,300,172,310,80,60,HG,HG,HG)
    s.circle(236,585,205,HG,HB,4);s.circle(625,750,164,HP,HB,4)
    s.rect(438,295,201,165,HP,HB,4);s.ellipse(538,295,100,26,HY,HB,4)
    s.path('M529 280Q492 283 527 291Q576 297 532 308','none',HB,5)
    for i in range(8,0,-1):s.rect(250-i*20,391+i*23,495,330,HW,HB,4)
    s.rect(250,391,495,330,HW,HB,4);s.line(250,416,745,416,HB,4)
    s.text(269,550,'HACK-',147,HB,700,'Study Condensed',width=361);s.text(269,694,'ATHON',147,HB,700,'Study Condensed',width=384)
    s.text(651,695,'stripe',30,HB,700);s.text(719,408,'×',24,HB,700)
    s.group(730,554,1,14);s.poly([(math.cos(i*math.pi/10-math.pi/2)*(112 if i%2==0 else 54),math.sin(i*math.pi/10-math.pi/2)*(112 if i%2==0 else 54)) for i in range(20)],'#FFA2C9',HB,4);s.end()
    # Extruded yellow L, all planes constructed, with no light or shadow effect.
    pts=[(150,940),(307,912),(307,801),(411,782),(411,1007),(150,1056)]
    s.poly([(x+43,y+35) for x,y in pts],HY,HB,4);s.poly(pts,HY,HB,4)
    for i in [0,2,3,4,5]:s.line(*pts[i],pts[i][0]+43,pts[i][1]+35,HB,4)
    s.rect(578,831,154,151,HR,HB,4);s.ellipse(655,831,77,21,HR,HB,4)
    for i in range(10,0,-1):s.rect(430+i*8,919+i*8,168,112,HW,HB,3)
    s.rect(430,919,168,112,HW,HB,4);s.lines(461,966,['04.25.19','04.26.19'],36,HB,700,leading=1.0,family='Study Condensed')
    s.save('posters','05-hackathon-windows','Hackathon · Windows')

def design_week():
    s=SVG(900,1200,'#F6F0E5');ink='#1C1A1B';green='#005B32';blue='#258CB4';purple='#554699';yellow='#FDC442';pink='#F5AAA4';orange='#FF5205'
    s.text(18,221,'SA',258,ink,900,width=329)
    s.poly([(349,29),(538,29),(538,221)],pink);s.poly([(349,29),(349,221),(538,221)],blue)
    s.text(-20,418,'DIEG',254,ink,900,width=624);s.circle(641,326,96,yellow)
    s.lines(700,87,['DESIGN+','ART','COMMUNITY','CRAFT','EDUCATION','ENVIRONMENT','FOOD & DRINK','MUSIC','SPORTS','SUSTAINABILITY','TECHNOLOGY'],22,ink,700,leading=1.05)
    s.clip(0,225,100,200);s.circle(-5,325,98,green);s.end()
    s.text(-16,615,'DESIGN',249,ink,900,width=904);s.rect(419,425,54,193,purple)
    s.clip(0,424,94,198);s.circle(-8,523,96,orange);s.end()
    s.text(5,815,'W',254,ink,900,width=269)
    for i,c in enumerate([blue,yellow,orange,pink,purple,green]):s.rect(302+(i%2)*204,637+(i//2)*61,193,49,c)
    s.text(705,815,'K',255,ink,900,width=180)
    s.text(9,1016,'2',252,ink,900,width=159);s.circle(262,927,97,orange)
    s.text(357,1016,'2',252,ink,900,width=175);s.circle(609,927,97,purple)
    s.text(20,1068,'SEPTEMBER 9–13 | SDDESIGNWEEK.ORG | #SDDESIGNWEEK',25,ink,900,width=856)
    s.rect(20,1101,184,78,ink);s.lines(28,1127,['Mingei','International','Museum'],17,'#FFFFFF',leading=1.14)
    s.text(865,1162,'intuit.',38,ink,700,anchor='end')
    s.save('posters','06-san-diego','San Diego Design Week · 2020')

def forest():
    s=SVG(900,1200,'#F49CC9');pink='#F4A2C9';blue='#4B53E6';yellow='#FFE840';green='#20A90D'
    s.ellipse(226,0,238,95,'#000000');s.text(66,37,'forest',93,'#FFFFFF',900,width=329)
    star(s,664,31,168,green,12,.46);s.path('M655 0Q670 56 637 83','none','#000000',8)
    s.rect(0,130,900,58,'#FFFFFF')
    for i in range(15):
        if i%2==0:s.rect(i*60,130,60,30,'#000000')
        else:s.rect(i*60,160,60,28,'#000000')
    s.rect(0,188,255,1012,'#FFFFFF')
    for y in range(188,1200,62):
        for x in range(0,255,62):
            if (x//62+y//62)%2==0:s.rect(x,y,62,62,'#000000')
    s.rect(255,188,645,625,yellow)
    for i in range(3):s.ellipse(590,340+i*101,264,82,blue)
    s.ellipse(483,307,66,101,'#FFFFFF');s.ellipse(578,298,58,87,'#FFFFFF');s.ellipse(495,343,20,42,'#000000');s.ellipse(583,329,16,34,'#000000')
    s.circle(351,726,61,yellow,'#000000',8);s.text(351,756,'08',76,'#000000',700,'Study Condensed',anchor='middle')
    s.rect(0,813,645,387,blue);s.lines(31,877,['Forest concert is an open-air concert','held in a forest theater outside the','western suburbs of Berlin. Every','summer, the Berlin Philharmonic','Orchestra holds the last concert of','the performance season here.'],24,'#FFFFFF',700,leading=1.22)
    s.text(31,1200,'2022',91,'#000000',700)
    s.path('M224 1140Q407 1003 413 1179Q352 1255 247 1194Q215 1152 331 1139','none',pink,17)
    s.rect(486,850,99,350,pink,rx=49);s.text(524,870,'06*15*06*24',50,'#000000',700,transform='rotate(90 524 870)')
    s.rect(645,813,255,387,'#000000')
    for i in range(4):s.poly([(771,820+i*74),(687-i*7,980+i*50),(855+i*7,980+i*50)],green)
    s.rect(754,1100,36,100,'#FFFFFF')
    s.save('posters','07-forest','Forest · Open-air Concert')

def hack_blocks():
    s=SVG(900,1200,'#FFFFFF');graph(s)
    s.circle(705,158,149,HP,HB,4);s.circle(495,1054,140,HG,HB,4)
    # Large open three-dimensional bracket; faces share the same vertices.
    s.poly([(80,0),(395,0),(585,174),(585,486),(735,486),(735,739),(442,739),(442,492),(80,174)],HG,HB,4)
    s.poly([(585,174),(735,174),(819,252),(664,252)],HW,HB,4)
    s.poly([(664,252),(819,252),(819,840),(663,840),(663,664),(445,664),(445,868),(300,868),(300,486),(585,486),(585,252)],HW,HB,4)
    s.poly([(80,174),(263,358),(263,668),(80,480)],HY,HB,4)
    s.rect(263,174,322,312,HG,HB,4)
    s.lines(290,293,['HACK-','ATHON'],108,HB,700,leading=1.0,family='Study Condensed',width=268)
    s.text(674,300,'stripe',46,HB,700)
    s.rect(717,433,122,125,HR,HB,4);s.circle(780,495,28,HG,HB,3);s.poly([(746,506),(768,458),(789,506)],HY,HB,3);s.rect(782,451,27,29,HP,HB,3)
    iso(s,90,648,159,450,-42,-39,'#7C42FF','#7C42FF','#7C42FF')
    s.lines(110,754,['SF','SEA','DUB','SG'],72,HW,700,leading=.98,family='Study Condensed')
    iso(s,437,665,231,136,-83,-74,HP,HP,HP)
    s.text(454,760,'25–26.04',58,HW,700,'Study Condensed',width=196)
    s.rect(535,846,323,243,HY,HB,4);s.poly([(535,846),(615,798),(858,798),(858,846)],HY,HB,4)
    iso(s,692,889,120,126,-37,-37,HG,HG,HG)
    s.circle(751,952,38,HY,HB,4);s.circle(739,941,4,HB);s.circle(765,941,4,HB);s.path('M728 961Q751 983 775 961','none',HB,4)
    for i in range(11,0,-1):s.rect(350+i*8,919+i*7,170,126,HW,HB,3)
    s.rect(350,919,170,126,HW,HB,4);s.lines(367,966,['REMOTES','TOO, OFC!'],38,HB,700,leading=1.02,family='Study Condensed',width=136)
    s.lines(711,664,['HACK!','HACK!','HACK!'],24,HB,700,leading=1.28)
    s.save('posters','08-hackathon-blocks','Hackathon · Blocks')

def konbin():
    s=SVG(900,1200,'#23B990');yellow='#FFDF06';blue='#2836B5';red='#FF2E05';green='#22B88A';black='#000000';white='#FFFFF3'
    def face(x,y,w,h,slant,color):
        s.add(f'<g transform="matrix(1 {slant} 0 1 {x} {y})">');s.rect(0,0,w,h,color);s.clip(0,0,w,h)
    def endface():s.end();s.end()
    def roof(x,y,w,d,color):
        s.add(f'<g transform="matrix(1 .425 -1 .425 {x} {y})">');s.rect(0,0,w,d,color);s.clip(0,0,w,d)
    # Small stage at the left: all labels are in their own plane's local coordinates.
    roof(220,95,300,220,black)
    s.text(18,182,'03.06',133,yellow,900,'Study Condensed',width=270);endface()
    face(0,188,300,273,.425,yellow)
    s.poly([(36,78),(119,78),(119,183),(203,183),(203,248),(36,248)],black);endface()
    face(300,315.5,220,273,-.425,green)
    endface()
    # Upper-right lettered cube; roof, front and right face form one closed solid.
    roof(620,-8,280,200,blue)
    s.lines(13,72,['Sur la scène','des amiux','faux'],42,yellow,900,leading=1.0,width=249);endface()
    face(420,77,280,312,.425,yellow)
    s.text(15,159,'KON',163,blue,700,'Study Condensed',width=251);endface()
    face(700,196,200,312,-.425,red)
    s.text(10,205,'BINI',161,yellow,700,'Study Condensed',width=181);endface()
    # The roof sits above the uninterrupted white title bridge.
    roof(365,315,535,365,black)
    s.text(78,282,'03.06',161,yellow,900,'Study Condensed',width=397);endface()
    face(300,315.5,120,260,-.425,green)
    s.lines(14,84,['WE','LOVE','GREEN'],47,white,700,leading=1.0,family='Study Condensed',width=92);endface()
    face(0,670,540,450,.425,blue)
    s.lines(22,90,['LAZULI','MAUREEN','MOUSSE PARTY','DAVD'],78,yellow,700,leading=.96,family='Study Condensed');endface()
    face(540,899.5,360,295,-.425,yellow)
    s.text(19,205,'INLINI',171,red,700,'Study Condensed',width=322);endface()
    face(0,470,540,200,.425,white)
    s.text(17,162,'KONBIN',171,black,700,'Study Condensed',width=508);endface()
    face(540,699.5,360,200,-.425,white)
    s.text(14,163,'STAGE',143,black,700,'Study Condensed',width=331);endface()
    # Small distant cubes in the skyline, outside the main bridge.
    face(0,0,185,145,.425,blue)
    s.text(8,126,'KON',110,yellow,700,'Study Condensed',width=168);endface()
    s.lines(28,1125,['WE','LOVE','GREEN'],27,white,900,leading=.90)
    s.save('posters','09-konbin','Konbin Stage · We Love Green')

MB='#276DB3';MO='#F04D1B';MY='#F6C333';MP='#EDC6C0';ML='#CAE5F4';MR='#FF3235';MI='#080808'
def molly(s,x,y,z=1,color=MI):
    s.group(x,y,z);s.text(0,32,'M',40,color,900);flower(s,47,18,15,color,6,.47);s.text(64,32,'LLY',40,color,900,spacing=-2)
    s.text(7,49,'茉莉视觉设计',8,color,700,spacing=4);s.end()
def rings(s,x,y,z,bg,fg,corner=0):
    s.group(x,y,z/100);s.clip(0,0,100,100);s.rect(0,0,100,100,bg)
    cx,cy=[(0,100),(100,100),(0,0),(100,0)][corner]
    for r in [48,77,106,135]:s.circle(cx,cy,r,'none',fg,4)
    s.end();s.end()
def bloom(s,x,y,r,red=True):
    if red:
        flower(s,x,y,r,MR,6,.84);flower(s,x,y,r*.37,MY,7,.90)
        for a in range(6):s.circle(x+r*.70*math.cos(a*math.tau/6-math.pi/2),y+r*.70*math.sin(a*math.tau/6-math.pi/2),r*.105,MI)
    else:
        for rr,spread,color in [(r*.58,r*.37,MY),(r*.49,r*.32,'#F6AD1A'),(r*.37,r*.27,'#FF9218')]:
            for dx,dy in [(-1,-1),(1,-1),(-1,1),(1,1)]:s.circle(x+spread*dx,y+spread*dy,rr,color)
        flower(s,x,y,r*.31,MO,4,.73);flower(s,x,y,r*.18,'#FFF5D6',4,.80);s.circle(x,y,r*.07,MO)
def halfpair(s,x,y,z):
    s.rect(x,y,z,z,MP)
    s.rect(x,y,z/2,z,'#FFF1D2')
    s.path(f'M{x} {y}A{z/2} {z/2} 0 0 1 {x} {y+z}Z',MO)
    s.path(f'M{x} {y+z*.13}A{z*.37} {z*.37} 0 0 1 {x} {y+z*.87}Z',MB)
    s.path(f'M{x+z} {y}A{z/2} {z/2} 0 0 0 {x+z} {y+z}Z','#5699CD')
    s.path(f'M{x+z} {y+z*.13}A{z*.37} {z*.37} 0 0 0 {x+z} {y+z*.87}Z',ML)
def terrain(s,w,h,scale=1):
    # The same finite motif kit recomposes as an uneven skyline, preserving the white center.
    s.group(0,h-500*scale,scale);w=w/scale
    halfpair(s,0,0,100);rings(s,0,100,100,MO,MB,2);halfpair(s,0,200,150);rings(s,0,350,150,MO,'#FFF3D0',0)
    s.rect(150,335,280,165,MB);tile(s,150,335,165,'quarter',MP,MB,rotation=90)
    tile(s,232,335,82,'quarter',MY,MB,rotation=180);tile(s,314,335,82,'leaf',MB,ML,rotation=90)
    tile(s,150,444,95,'stripe',MY,MO,rotation=45)
    tile(s,245,444,185,'arc',ML,MB,MP,rotation=90)
    base=500
    for x in [472,548,624]:s.poly([(x,444),(x,370),(x+76,444)],MO)
    for i in range(6):s.poly([(430+i*105,500),(535+i*105,444),(640+i*105,500)],[MB,ML,'#559ACF'][i%3])
    s.poly([(467,294),(519,242),(571,294),(519,346)],MB);s.poly([(467,294),(571,294),(519,346)],ML)
    bloom(s,772,366,74,False)
    s.path('M898 352V449H1000A102 102 0 0 0 898 352Z',MB)
    s.path('M898 449Q850 449 850 396Q898 396 898 449Z','#579ACD');s.path('M903 449Q903 396 951 396Q951 449 903 449Z',MO)
    # Right elevation and a three-line outer spine.
    xr=w-430
    s.rect(xr,302,280,198,MB);tile(s,xr,302,140,'quarter',MB,MO,rotation=180)
    tile(s,xr+140,302,140,'quarter',MB,MP,rotation=90)
    tile(s,xr,442,140,'arc',ML,MB,rotation=90)
    for i in range(8):s.rect(xr+140+i*17.5,442,9,58,[MY,MO][i%2])
    halfpair(s,w-180,170,132)
    s.path(f'M{w-133} 170V108Q{w-133} 40 {w-47} 40V170Z',MO)
    s.rect(w-180,302,132,132,'#FFFFFF');bloom(s,w-114,368,61)
    rings(s,w-180,434,132,MP,MO,2)
    for i,c in enumerate([MB,'#F594DF',ML]):s.rect(w-48+i*16,170,16,330,c)
    for x in [w-309,w-268,w-227]:
        for y in [220,264]:s.circle(x,y,13,'none',MI,4)
    s.circle(xr,348,38,MO);s.path(f'M{xr} 310A38 38 0 0 1 {xr} 386Z','#579ACD')
    s.end()
def brand_title(s,x,y,size,color=MI,anchor=None):
    s.lines(x,y,['于繁华之中','遇见审美共鸣'],size,color,400,leading=.99,family='Study Pixel',anchor=anchor,spacing=-size*.02)
def brand_en(s,x,y,size,color=MB,anchor=None):
    s.lines(x,y,['AMID PROSPERITY','MEET AESTHETIC RESONANCE'],size,color,400,leading=1.15,family='Study Pixel',anchor=anchor)
BRAND_COPY=['艺术没有距离。它藏在繁华闹市，等待每一个','路过的人驻足。不必深谙理论，只需随心感受。在','人流之间，与作品对望，于平凡日常里，打捞独属','于自己的浪漫与共鸣。']
def tagline(s,x,y,size=24,c=MI,anchor=None):
    s.text(x,y,'烟火为幕  艺术为光',size,c,700,anchor=anchor)
    s.text(x,y+size*.85,"Life’s glow as backdrop, art as light.",size*.60,c,700,anchor=anchor)
def date(s,x,y,size=27,c=MI,anchor=None):
    s.text(x,y,'10.01–10.30',size,c,700,'Study Condensed',anchor=anchor)
    s.text(x,y+size*.46,'静安区南京西路1166号 兴业中心 L1 艺术展厅',size*.20,c,700,anchor=anchor)
def barcode(s,x,y,w,h,c=MI):
    # Decorative visual bars, intentionally not represented as a scannable identifier.
    units=[1,1,2,1,1,3,2,1,3,1,2,1,1,2,3,1,2,2,1,3,2,1,1,2,1,1,3,1,2,3,1,2,1,1,2,1,3,1,1,2]
    scale=w/(sum(units)+len(units));at=x
    for u in units:s.rect(at,y,u*scale,h,c);at+=(u+1)*scale
def brand_mosaic(s,x,y,w,h,variant=0,cols=4):
    z=w/cols;s.clip(x,y,w,h)
    for j in range(math.ceil(h/z)):
        for i in range(cols):
            xx=x+i*z;yy=y+j*z;k=(i+j*cols+variant)%9
            if k==0:halfpair(s,xx,yy,z)
            elif k==1:rings(s,xx,yy,z,MO,'#FFF1D2',0)
            elif k==2:s.rect(xx,yy,z,z,'#FFFFFF');bloom(s,xx+z/2,yy+z/2,z*.46)
            elif k==3:tile(s,xx,yy,z,'quarter',MB,MO,rotation=180)
            elif k==4:tile(s,xx,yy,z,'arc',ML,MB,MP,rotation=90)
            elif k==5:
                s.rect(xx,yy,z,z,MY)
                for k in range(4):s.rect(xx+k*z/4,yy,z/8,z,MO)
            elif k==6:tile(s,xx,yy,z,'quarter',MY,MB,rotation=90)
            elif k==7:tile(s,xx,yy,z,'arc',MP,MO,MO)
            elif k==8:
                s.rect(xx,yy,z,z,MB);s.poly([(xx,yy+z),(xx+z/2,yy),(xx+z,yy+z)],ML)
    s.end()
def brand():
    s=SVG(1600,770,'#FFFFFF');molly(s,64,48,1)
    tagline(s,1550,82,31,anchor='end')
    s.lines(858,266,['AMID PROSPERITY','MEET','AESTHETIC RESONANCE'],52,MB,400,leading=1.20,family='Study Pixel',anchor='end')
    s.line(888,220,888,393,MB,4);brand_title(s,924,286,88)
    s.text(1389,286,'，',59,MI,900,'Study CJK')
    terrain(s,1600,770,1)
    star(s,248,513,48,MB,11,.42)
    s.save('brand','01-banner','Molly · 主视觉横幅')
    for i in range(3):
        s=SVG(250,915,MB if i==1 else '#FFFFFF');s.add('<g transform="scale(1 .89)">')
        if i==0:halfpair(s,0,0,250);rings(s,0,250,250,MO,'#FFF3D5')
        elif i==1:
            s.rect(0,0,250,250,'#FFFFFF');bloom(s,125,125,118);rings(s,0,250,250,MP,MO,1)
        else:
            s.rect(0,0,250,230,'#DDDCD9');s.circle(125,120,112,MB);s.path('M46 199L204 41A112 112 0 0 1 46 199Z',MY);s.circle(125,120,20,MO)
            s.rect(0,230,250,123,MP);s.path('M0 353V293Q0 230 64 230H250V291Q250 353 187 353Z',MR);s.rect(0,353,250,147,MY)
        s.end()
        # Panels are 49% of the strip, while their artwork keeps its own proportions.
        s.rect(0,445,250,470,MB if i==1 else '#FFFFFF')
        color='#FFFFFF' if i==1 else MI
        brand_title(s,125,554,34,color,'middle');brand_en(s,125,634,12,color,'middle')
        s.lines(20,735,['艺术没有距离。它藏在繁华闹市，','等待每一个路过的人驻足。不必深谙','理论，只需随心感受。在人流之间，','与作品对望，于平凡日常里，打捞','独属于自己的浪漫与共鸣。'],9,color,700,leading=1.75)
        s.line(20,819,230,819,color,.8);date(s,125,865,27,color,'middle');barcode(s,37,887,176,22,color)
        s.save('brand',f'0{i+2}-ribbon','Molly · 竖幅 '+str(i+1))
    s=SVG(700,480,'#FFFFFF');molly(s,487,60,.83)
    s.lines(64,93,BRAND_COPY,14,MI,700,leading=1.75)
    tagline(s,64,284,24);date(s,64,410,35)
    s.clip(550,0,150,480);terrain(s,700,480,.66);s.end()
    s.save('brand','05-invitation-white','Molly · 白色邀请卡')
    s=SVG(700,480,MB);molly(s,42,27,.6,'#FFFFFF');brand_title(s,350,135,52,'#FFFFFF','middle');brand_en(s,350,263,24,'#FFFFFF','middle')
    halfpair(s,0,218,62);rings(s,0,328,100,MO,'#FFF1D2');halfpair(s,600,232,76);bloom(s,634,357,37)
    s.path('M624 232V194Q624 168 671 168V232Z',MO)
    brand_mosaic(s,268,356,332,124,2,4);brand_mosaic(s,0,418,268,62,0,4);brand_mosaic(s,600,398,100,82,7,1)
    s.save('brand','06-invitation-blue','Molly · 蓝色邀请卡')
    for i in range(2):
        s=SVG(330,550,'#666666')
        s.poly([(82,65),(122,0),(208,0),(250,65)],'#99A4AC');s.poly([(111,65),(135,27),(196,27),(222,65)],'#666666')
        s.poly([(98,0),(224,0),(239,29),(84,29)],'#0874BE')
        s.rect(0,65,330,485,MB if i else '#FFFFFF')
        if i==0:
            brand_mosaic(s,0,65,250,36,3,6);brand_mosaic(s,0,101,61,135,0,1)
            molly(s,213,129,.64);bloom(s,145,239,55,False)
            s.lines(248,220,['烟','火','为','幕','艺','术','为','光'],10,MI,700,leading=1.2)
            brand_title(s,34,390,39);brand_en(s,165,475,14,MI,'middle')
        else:
            brand_title(s,165,181,40,'#FFFFFF','middle');brand_en(s,165,273,15,'#FFFFFF','middle')
            brand_mosaic(s,0,310,330,158,0,4)
            s.text(165,509,'当艺术遇见城市烟火，在日常里触摸美学',11,'#FFFFFF',anchor='middle')
        s.save('brand',f'0{7+i}-bag','Molly · 手提袋 '+str(i+1))
    for i in range(2):
        s=SVG(240,500,'#666666');s.rect(89,0,62,112,'#0877C8');s.rect(85,105,70,25,'none',MI,6);s.rect(112,118,16,42,MI)
        s.rect(0,164,240,336,'#FFFFFF' if i else MB)
        if i==0:
            s.rect(0,164,240,66,'#FFFFFF');tagline(s,120,196,17,anchor='middle');brand_title(s,120,282,31,'#FFFFFF','middle')
            brand_mosaic(s,0,330,240,92,3,4)
            brand_en(s,120,452,11,'#FFFFFF','middle')
        else:
            tagline(s,120,196,17,anchor='middle')
            s.group(0,229);s.clip(0,0,240,14);terrain(s,240,14,.19);s.end();s.end()
            brand_title(s,120,302,31,MI,'middle');brand_en(s,120,369,11,MI,'middle')
            brand_mosaic(s,88,413,152,87,2,3);brand_mosaic(s,0,475,88,25,0,3)
        s.save('brand',f'{9+i:02d}-badge','Molly · 挂牌 '+str(i+1))
    s=SVG(340,550,MB);molly(s,22,20,.58,'#FFFFFF');brand_title(s,170,129,38,'#FFFFFF','middle');brand_en(s,170,219,15,'#FFFFFF','middle')
    s.lines(45,286,['艺术从来不止于美术馆的高墙，它是城市的','自在呼吸，是在人流里的驻足与靠近。不必','刻意寻找，在街头与作品相遇，便是一场审美','共鸣。以艺术之光，让日常的每刻都值得，','多一些发现与热爱。'],10,'#FFFFFF',700,leading=1.8)
    date(s,27,458,25,'#FFFFFF');brand_mosaic(s,0,477,340,73,3,5);bloom(s,238,438,35,False);halfpair(s,300,423,40)
    s.save('brand','11-leaflet','Molly · 活动长卡')

def gallery():
    (ROOT/'manifest.json').write_text(json.dumps(UNITS,ensure_ascii=False,indent=2))
    # Individual SVGs use shared local webfonts; the gallery and render are entirely offline.
    css='''*{box-sizing:border-box}body{margin:0;background:#191919;color:#eee;font:15px Arial,sans-serif;padding:40px}h1{font-size:32px;margin:0 0 12px}p{color:#aaa}nav{display:flex;gap:24px;margin:28px 0}a{color:inherit}section{margin-top:64px}h2{font-size:24px}.grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:28px}.slides{grid-template-columns:repeat(2,minmax(0,1fr))}figure{margin:0}figure svg{display:block;width:100%;height:auto}figcaption{font-size:13px;color:#aaa;margin-top:10px}dialog{border:0;padding:0;background:#333;max-width:94vw;max-height:96vh}dialog img{display:block;max-width:94vw;max-height:92vh}dialog button{position:fixed;right:20px;top:16px}button{cursor:pointer}figure a{display:block}@media(max-width:700px){body{padding:18px}.grid,.slides{grid-template-columns:1fr}}'''
    h=['<!doctype html><html lang="zh"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Memphis · Reference reconstruction</title><style>'+css+'</style><h1>Memphis · 参考作品复刻</h1><p>三张参考 / 28 件矢量稿 / 按原图顺序。点击作品打开独立 SVG；文字和图形保留编辑能力。</p><nav><a href="#slides">01 · 八页版式</a><a href="#posters">02 · 九张海报</a><a href="#brand">03 · 视觉物料</a></nav>']
    for group,title in [('slides','01 · PKL / 八页版式'),('posters','02 · 九张海报'),('brand','03 · Molly / 视觉物料')]:
        h.append(f'<section id="{group}"><h2>{title}</h2><div class="grid {group}">')
        for u in UNITS:
            if u['group']!=group:continue
            svg=(ROOT/u['file']).read_text().replace('../assets/','assets/')
            prefix=u['group']+'-'+u['name']+'-'
            svg=re.sub(r'id="(c\d+)"',lambda m:'id="'+prefix+m.group(1)+'"',svg)
            svg=re.sub(r'url\(#(c\d+)\)',lambda m:'url(#'+prefix+m.group(1)+')',svg)
            h.append(f'<figure data-file="{u["file"]}"><a href="{u["file"]}">{svg}</a><figcaption>{escape(u["title"])}</figcaption></figure>')
        h.append('</div></section>')
    (ROOT/'index.html').write_text(''.join(h)+'</html>')

if __name__=='__main__':
    slides()
    for make in [collection,new_design,tresor,txc,hack_windows,design_week,forest,hack_blocks,konbin]:make()
    brand()
    gallery()
