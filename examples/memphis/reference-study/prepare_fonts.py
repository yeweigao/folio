#!/usr/bin/env python3
"""Bundle licensed, used glyphs; construct the reference's pixel display surrogate."""
from pathlib import Path
from html import unescape
import re, json, shutil
from fontTools import subset
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.ttGlyphPen import TTGlyphPen
from PIL import Image, ImageFont, ImageDraw

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'assets';OUT.mkdir(exist_ok=True)
text=''.join(unescape(x) for p in ROOT.glob('*/*.svg') for x in re.findall(r'<text[^>]*>(.*?)</text>',p.read_text()))
chars=set(text)|set(chr(i) for i in range(32,127))
fonts=[('Inter-400.ttf','sans-400'),('Inter-700.ttf','sans-700'),('Inter-900.ttf','sans-900'),('Archivo-variable.ttf','light'),('NotoSansSC-variable.ttf','cjk'),('Oswald-700.ttf','condensed')]
records=[]
for filename,dest in fonts:
    p=Path('/Users/vicoye/Library/Fonts')/filename
    options=subset.Options();options.flavor='woff2';options.name_IDs=['*'];options.name_legacy=True;options.name_languages=['*']
    font=subset.load_font(str(p),options)
    job=subset.Subsetter(options=options);job.populate(text=''.join(chars));job.subset(font)
    subset.save_font(font,str(OUT/(dest+'.woff2')),options)
    records.append(dict(file=dest+'.woff2',source=str(p),license='SIL Open Font License 1.1',substitution='Study substitute; original reference font unidentified'))

alphabet={
'A':['01110','11011','11011','11111','11011','11011','11011'],
'B':['11110','11011','11011','11110','11011','11011','11110'],
'C':['01111','11000','11000','11000','11000','11000','01111'],
'D':['11110','11011','11011','11011','11011','11011','11110'],
'E':['11111','11000','11000','11110','11000','11000','11111'],
'F':['11111','11000','11000','11110','11000','11000','11000'],
'G':['01111','11000','11000','11011','11011','11011','01111'],
'H':['11011','11011','11011','11111','11011','11011','11011'],
'I':['11111','01110','01110','01110','01110','01110','11111'],
'J':['00111','00011','00011','00011','11011','11011','01110'],
'K':['11011','11011','11110','11100','11110','11011','11011'],
'L':['11000','11000','11000','11000','11000','11000','11111'],
'M':['11011','11111','11111','11011','11011','11011','11011'],
'N':['11011','11111','11111','11111','11011','11011','11011'],
'O':['01110','11011','11011','11011','11011','11011','01110'],
'P':['11110','11011','11011','11110','11000','11000','11000'],
'Q':['01110','11011','11011','11011','11011','11110','00111'],
'R':['11110','11011','11011','11110','11100','11010','11011'],
'S':['01111','11000','11000','01110','00011','00011','11110'],
'T':['11111','01110','01110','01110','01110','01110','01110'],
'U':['11011','11011','11011','11011','11011','11011','01110'],
'V':['11011','11011','11011','11011','11011','01110','00100'],
'W':['11011','11011','11011','11011','11111','11111','01010'],
'X':['11011','11011','01110','00100','01110','11011','11011'],
'Y':['11011','11011','01110','00100','00100','00100','00100'],
'Z':['11111','00011','00110','01100','11000','11000','11111']}
glyphs={};metrics={};cmap={}
def glyph_rects(rows,cell,advance,xoffset=0):
    pen=TTGlyphPen(None)
    for j,row in enumerate(rows):
        # Coalesce a horizontal run, keeping adjacent rows separate for a pixel silhouette.
        runs=re.finditer('1+',row)
        for run in runs:
            x0=run.start()*cell+xoffset;x1=run.end()*cell+xoffset;y1=(len(rows)-j)*cell;y0=y1-cell
            pen.moveTo((x0,y0));pen.lineTo((x1,y0));pen.lineTo((x1,y1));pen.lineTo((x0,y1));pen.closePath()
    return pen.glyph(),(advance,0)
glyphs['.notdef'],metrics['.notdef']=glyph_rects(['11111','10001','10001','10001','10001','10001','11111'],100,600)
cjk_font=ImageFont.truetype('/Users/vicoye/Library/Fonts/NotoSansCJKsc-Black.otf',28)
for ch in sorted(chars):
    name=f'uni{ord(ch):04X}';cmap[ord(ch)]=name
    if ch.upper() in alphabet:
        rows=alphabet[ch.upper()];cell=110;advance=660;off=0
    elif ord(ch)>0x2fff:
        im=Image.new('L',(40,40));d=ImageDraw.Draw(im);d.text((0,0),ch,font=cjk_font,fill=255,anchor='lt')
        bb=im.getbbox()
        im=im.crop(bb).resize((28,28),Image.Resampling.NEAREST) if bb else Image.new('L',(28,28))
        rows=[''.join('1' if im.getpixel((x,y))>110 else '0' for x in range(28)) for y in range(28)];cell=32;advance=925;off=0
    else:
        f=ImageFont.truetype('/Users/vicoye/Library/Fonts/Inter-900.ttf',8)
        im=Image.new('L',(7,9));ImageDraw.Draw(im).text((0,0),ch,font=f,fill=255,anchor='lt')
        rows=[''.join('1' if im.getpixel((x,y))>100 else '0' for x in range(7)) for y in range(9)];cell=90;advance=660 if ch!=' ' else 330;off=0
    glyphs[name],metrics[name]=glyph_rects(rows,cell,advance,off)
fb=FontBuilder(1000,isTTF=True);fb.setupGlyphOrder(list(glyphs));fb.setupCharacterMap(cmap);fb.setupGlyf(glyphs);fb.setupHorizontalMetrics(metrics);fb.setupHorizontalHeader(ascent=950,descent=-100)
fb.setupNameTable({'familyName':'Folio Pixel Study','styleName':'Regular','uniqueFontIdentifier':'FolioPixelStudy-20261104','fullName':'Folio Pixel Study Regular','psName':'FolioPixelStudy-Regular','version':'Version 1.0','licenseDescription':'SIL Open Font License 1.1; Latin constructed for this study. CJK derived from Noto Sans CJK by Google/Adobe.','licenseInfoURL':'https://openfontlicense.org/'})
fb.setupOS2(sTypoAscender=950,sTypoDescender=-100,usWinAscent=1000,usWinDescent=100);fb.setupPost();fb.setupMaxp()
fb.font.flavor='woff2';fb.font.save(OUT/'pixel.woff2')
records.append(dict(file='pixel.woff2',source='Constructed Latin grid and pixel-derived Noto Sans CJK SC Black',license='SIL OFL 1.1',substitution='Authored surrogate, not the unidentified reference font'))
shutil.copy(ROOT.parent.parent/'swiss/flyer/fonts/inter-OFL.txt',OUT/'Inter-OFL.txt')
shutil.copy(ROOT.parent.parent/'swiss/flyer/fonts/noto-sans-sc-OFL.txt',OUT/'Noto-OFL.txt')
(OUT/'fonts.json').write_text(json.dumps(records,ensure_ascii=False,indent=2))
print('Bundled',len(records),'fonts;',len(chars),'used characters.')
