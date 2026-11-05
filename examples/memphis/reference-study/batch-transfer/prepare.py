#!/usr/bin/env python3
"""Freeze nine unchanged systems and unrelated new content for independent makers."""
from pathlib import Path
import hashlib, json, os, shutil
R=Path(__file__).resolve().parent;STUDY=R.parent
CASES=[
('01-report-tiles','新报告页',1280,720,[
 ('报告名','Laporan Proyek Komunikasi Visual'),('主题','Eksplorasi Ruang Kota'),('作者','Nadia Putri'),('机构','Studio Sekolah'),('年份','2027'),('分组一','Observasi'),('正文一','Mengamati tanda, warna, dan kebiasaan di ruang publik sebagai dasar sistem komunikasi visual.'),('分组二','Eksperimen'),('正文二','Menguji bentuk dan bahasa visual melalui prototipe yang dekat dengan kehidupan sehari-hari.')]),
('02-streetwise-collage','街区散步活动海报',900,1200,[
 ('主标题','集合散步'),('副标题','在城里发现'),('英文标题','CITY WALKS'),('英文说明','Small discoveries, shared streets.'),('日期','2027.05.14–05.16'),('地点','河岸街区'),('活动说明','一起走进街角的日常')]),
('03-cut-glyph-exhibition','新设计展海报',900,1200,[
 ('展名','共生设计展'),('展示主题','共生'),('英文展名','COEXIST DESIGN EXHIBITION'),('开始日期','12 JUNE'),('结束日期','28 AUGUST'),('时间','09:00–18:00'),('地点','城市设计馆'),('署名','策展：林岚')]),
('04-club-partitions','新俱乐部活动海报',900,1200,[
 ('活动名','Night Assembly'),('主厅艺人一','Rosa Flux'),('主厅艺人二','Mika Lo'),('主厅说明','B2B until dawn'),('副厅名','LOWER ROOM'),('副厅艺人一','Alba Phase'),('副厅艺人二','Dorian East'),('副厅艺人三','NEX'),('日期','17.07.27'),('开始时间','23:00'),('场地','FORMA CLUB')]),
('05-culture-monsters','新文化科技活动海报',900,1200,[
 ('主活动','TTXC 2027'),('中文主题','城市游乐场'),('英文主题','City Play!'),('说明','ART × SOUND × TECHNOLOGY'),('口号','一起把城市玩出新花样'),('日期','2027.09.10–12'),('中文场地','海岸文化中心'),('英文场地','Coast Culture Center')]),
('06-hackathon-space','新开发者活动海报',900,1200,[
 ('活动名','BUILD-ATHON'),('城市一','TYO'),('城市二','SEL'),('城市三','SIN'),('城市四','SYD'),('日期一','06.18.27'),('日期二','06.19.27'),('远程说明','REMOTE TEAMS WELCOME'),('口号','MAKE WHAT CONNECTS US'),('组织名','stripe')]),
('07-type-built-week','新设计周海报',900,1200,[
 ('城市','TAIPEI'),('主题','DESIGN'),('活动类型','WEEK'),('年份','2027'),('类别一','ARCHITECTURE'),('类别二','CRAFT'),('类别三','FOOD'),('类别四','MUSIC'),('类别五','PUBLIC SPACE'),('日期','OCTOBER 4–10'),('网站','TAIPEIDESIGNWEEK.EXAMPLE'),('主办方','City Design Museum'),('合作方','Open City Lab')]),
('08-forest-character','新森林音乐活动海报',900,1200,[
 ('品牌','forest'),('主题','After Hours'),('年份','2027'),('日期','07.03–07.24'),('时间','18:30–22:00'),('地点','Riverside Forest Stage'),('正文','Open-air music returns to the riverside forest. Bring your friends, follow the lights, and spend a summer evening among the trees.')]),
('09-isometric-letter-stage','新舞台活动海报',900,1200,[
 ('活动名','KONBIN STAGE'),('日期','17.07'),('场地类型','OPEN AIR'),('口号','WE MAKE NOISE'),('艺人一','RINA VEIL'),('艺人二','LAGO'),('艺人三','MOTIF CLUB'),('艺人四','NEON PALMS')]),
]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
if __name__=='__main__':
 R.mkdir(exist_ok=True);cases=[]
 for id,title,w,h,facts in CASES:
  case=R/'cases'/id;inp=case/'input';inp.mkdir(parents=True,exist_ok=True)
  src=STUDY/'systems'/id/'DESIGN.md';shutil.copyfile(src,inp/'DESIGN.md')
  fonts=inp/'fonts';fonts.mkdir(exist_ok=True)
  for f in (STUDY/'transfer-test/input/fonts').iterdir():
   dest=fonts/f.name
   if f.is_file() and not dest.exists():os.link(f,dest)
  brief=f'# 新内容迁移简报 · {title}\n\n## Reader and outcome\n为该世界制作另一件完整作品，画幅 {w} × {h} px。近距离可读，缩略图有明确主次。活动与人名均为测试虚构，不代表真实活动。\n\n## Facts\n'
  brief+='\n'.join(f'- {label}：`{value}`' for label,value in facts)
  brief+='\n\n## Deliverable\n一件静态原生 SVG，所有固定信息可见且文字可编辑、字体内嵌；可以按语义换行，但不修改或遗漏事实。图形化字形不得让活动主题失去可读性。\n\n## Design authority\n只依据随附 DESIGN.md 重组。没有原图、前作、图形组件或旧绘制代码；不读取其他 skill。自行记录文件没说明而必须决定的事项，记录不印在作品中。允许自己的渲染自查；独立审阅后不修改首轮输出来争取通过。\n'
  (inp/'brief.md').write_text(brief)
  for name in ['embed_fonts.py']:
   shutil.copyfile(R/'production'/name,inp/name)
  (inp/'TECHNICAL.md').write_text('''# 中性制作支持\n\nembed_fonts.py 只把提供的字体子集内嵌，不含图形或布局。SVG 中用 Study Sans（400/700/900）、Study Light（100–900）、Study CJK（100–900）、Study Condensed（700）；均来自 DESIGN.md 列出的字库。\n\n运行：`/private/tmp/folio-memphis-tools/bin/python input/embed_fonts.py input/fonts output-v1/raw.svg output-v1/poster.svg`。\n\nPython 已有 fontTools、brotli、Pillow。渲染可用 Node /opt/homebrew/bin/node，Playwright /Users/vicoye/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright，Chrome /Applications/Google Chrome.app/Contents/MacOS/Google Chrome。通用工具不提供美学判断。\n''')
  manifest={str(p.relative_to(inp)):{'sha256':sha(p),'bytes':p.stat().st_size} for p in sorted(inp.rglob('*')) if p.is_file()}
  (case/'input-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
  cases.append(dict(id=id,title=title,width=w,height=h,facts=len(facts),design_sha256=sha(src)))
 (R/'cases.json').write_text(json.dumps(cases,ensure_ascii=False,indent=2))
 print('Prepared',len(cases),'frozen cases.')
