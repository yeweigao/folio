#!/usr/bin/env python3
"""Generic font embedding only. No drawing primitives, grid or composition."""
from pathlib import Path
import sys,io,base64,re,xml.etree.ElementTree as ET
from fontTools import subset

def main():
 fonts,src,out=map(Path,sys.argv[1:4]);data=src.read_text();root=ET.fromstring(data)
 text=''.join(''.join(n.itertext()) for n in root.iter() if n.tag.split('}')[-1]=='text')+''.join(chr(i) for i in range(32,127))
 faces=[('Study Sans','Inter-400.ttf','400'),('Study Sans','Inter-700.ttf','700'),('Study Sans','Inter-900.ttf','900'),('Study Light','Archivo-variable.ttf','100 900'),('Study CJK','NotoSansSC-variable.ttf','100 900'),('Study Condensed','Oswald-700.ttf','700'),('Study Pixel','FolioPixelStudy.woff2','400')]
 css=[]
 for name,file,weight in faces:
  if name not in data:
   continue
  opts=subset.Options();opts.flavor='woff2';opts.name_IDs=[0,1,2,3,4,5,6,13,14]
  font=subset.load_font(str(fonts/file),opts);job=subset.Subsetter(options=opts);job.populate(text=text);job.subset(font)
  font.flavor='woff2';b=io.BytesIO();font.save(b)
  css.append('@font-face{font-family:"'+name+'";font-weight:'+weight+';src:url(data:font/woff2;base64,'+base64.b64encode(b.getvalue()).decode()+')}')
 style='<style>'+''.join(css)+'</style>'
 data=data.replace('<!-- FONTS -->',style) if '<!-- FONTS -->' in data else re.sub(r'(<svg\b[^>]*>)',lambda m:m[1]+style,data,count=1)
 out.parent.mkdir(parents=True,exist_ok=True);out.write_text(data)
 print(out)
if __name__=='__main__':main()
