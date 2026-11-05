#!/usr/bin/env python3
"""Make each SVG and the HTML gallery independent of local font installations."""
from pathlib import Path
import base64
ROOT=Path(__file__).resolve().parent
for p in list(ROOT.glob('*/*.svg'))+[ROOT/'index.html']:
    text=p.read_text()
    for f in (ROOT/'assets').glob('*.woff2'):
        uri='data:font/woff2;base64,'+base64.b64encode(f.read_bytes()).decode()
        text=text.replace('../assets/'+f.name,uri).replace('assets/'+f.name,uri)
    p.write_text(text)
print('Embedded webfonts in every SVG and the HTML gallery.')
