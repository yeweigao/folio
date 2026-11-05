#!/usr/bin/env python3
"""Snapshot revised rules with the SAME briefs; keep all v1 evidence intact."""
from pathlib import Path
import json,hashlib,os,shutil,sys
R=Path(__file__).resolve().parent;S=R.parent
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 meta=json.loads((R/'cases.json').read_text())
 if not any(c['id']=='10-molly-scenery' for c in meta):
  case=R/'cases/10-molly-scenery';case.mkdir(exist_ok=True)
  shutil.copytree(S/'transfer-test/input',case/'input')
  shutil.copytree(S/'transfer-test/frozen-v1',case/'output-v1')
  shutil.copyfile(S/'transfer-test/input-manifest.json',case/'input-manifest.json')
  meta.append(dict(id='10-molly-scenery',title='艺术活动竖版海报',width=1080,height=1528,facts=9,design_sha256=digest(case/'input/DESIGN.md'),baseline_source='../transfer-test/frozen-v1'))
  (R/'cases.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2))
 selected=set(sys.argv[1:])
 for m in meta:
  if selected and m['id'] not in selected:continue
  case=R/'cases'/m['id'];dest=case/'input-v2'
  if dest.exists():raise SystemExit('Refusing to replace frozen v2 packet: '+str(dest))
  dest.mkdir();src=S/'systems'/m['id']/'DESIGN.md';shutil.copyfile(src,dest/'DESIGN.md')
  shutil.copyfile(case/'input/brief.md',dest/'brief.md')
  fonts=dest/'fonts';fonts.mkdir()
  for p in (case/'input/fonts').iterdir():
   if p.is_file():os.link(p,fonts/p.name)
  shutil.copyfile(R/'production/embed_fonts.py',dest/'embed_fonts.py')
  technical=(R/'cases/01-report-tiles/input/TECHNICAL.md').read_text().replace('input/','input-v2/').replace('output-v1/','output-v2/')
  (dest/'TECHNICAL.md').write_text(technical)
  manifest={str(p.relative_to(dest)):{'sha256':digest(p),'bytes':p.stat().st_size} for p in sorted(dest.rglob('*')) if p.is_file()}
  (case/'input-v2-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
  assert (dest/'brief.md').read_bytes()==(case/'input/brief.md').read_bytes()
 print('Prepared revised inputs with identical briefs:',', '.join(selected) if selected else 'all ten')
if __name__=='__main__':main()
