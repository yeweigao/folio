#!/usr/bin/env python3
"""Reproduce the ORIGINAL draft hypotheses after the reconstruction study.

This historical generator does not encode later, transfer-tested revisions.
Reviewed files are preserved by default; --overwrite-original-drafts explicitly
recreates the initial drafts. It does not author or alter artwork.
"""
from pathlib import Path
import json, sys
ROOT=Path(__file__).resolve().parent
SYSTEMS=[
dict(id='01-report-tiles',title='方砖报告系统',pieces=['slides/01-cover.svg','slides/02-contents.svg','slides/03-background.svg','slides/04-profile.svg','slides/05-vision.svg','slides/06-history.svg','slides/07-work.svg','slides/08-responsibilities.svg'],
  method='先给每页一个有方向的图案场——竖柱、横带、角块或双列；再让图案场的边界确定标题与正文的轴。标题用轻字搭重字，形成一条连续阅读路径。',
  grid='Modular — 用正方形方砖建立条带，正文区合并方格。横版按 8–9 块排横带、5 块排竖带；封面允许两列四行的较大方砖。不同条带可用不同模块，不能把整套固定成一个绝对砖尺寸。',
  type='轻重对比领先。展示字约 S/8，章标题约 S/10，正文约 S/48，导航约 S/52；这里是参考的近距离阅读层级。重字保持紧凑，轻字与重字的实际墨迹边界对齐。',
  space='图案区连续无缝，文字区保留整块蓝或粉色。文字安全边为约 S/18；正文分两列或三个任务组，图案从不压在正文下。',
  shape='八类有限砖：六瓣花、八角软星、十字、四圆、密齿圆、圆角折块、叶块、四分之一环。圆角折块有内缩直边，不能替换成满格扇形。',
  variation='同一图案库在竖柱、横带、角块中换位；蓝底、粉底与橙色半场形成页间节奏。',
  ban='不要在每页塞一条相同的横带；不要随机打乱已被参考固定的砖序。',
  colors={'paper':'#F8F6ED','blue':'#343D9F','pink':'#FA0056','orange':'#FF7619','cream':'#FFE5A6'},
  pairs=[('paper','blue',''),('paper','pink',''),('paper','orange',''),('blue','orange','-large')],display='Study Light',weight=100,size=136),
dict(id='02-streetwise-collage',title='街头行动 · 不等跨模块拼贴',pieces=['posters/01-collection-of-acts.svg'],
  method='把信息拆成相邻但不等大的街区；让两块实色文字区成为可停留的路口，其他格块用图形节奏把眼睛带回文字。',
  grid='Modular — 短边分为六个基格，允许半格与两格合并；横条、方砖与两倍高竖块交错，不能降成等大的棋盘。',
  type='极黑中文和粗英文构成合并文字块；大字为 S/9 至 S/10，副标题约 S/22，事实约 S/40。中英文各有自己的层级，不用中文大小去容纳英文。',
  space='边到边铺满；留白本身是一块有明确边界的纸色格。主标题区约占 3×2 基格，次文字区占 3×1 基格。',
  shape='斜条、双箭头、菱形、圆、四尖负形、细网格、粗黑白竖条和半圆；同一相邻区域不连续重复同一种图案。',
  variation='条纹方向与格块跨距交替；大圆允许跨过一条色块边界。',
  ban='不要用任意一套花和星替换街区图案；不要让文字区变成后贴的卡片。',
  colors={'paper':'#EAE8E6','ink':'#19191D','blue':'#008BCD','green':'#087C4A','pink':'#F68CBC','yellow':'#FFDE00','red':'#F52B20','purple':'#76258D'},pairs=[('ink','paper','')],display='Study Sans',weight=900,size=110),
dict(id='03-cut-glyph-exhibition',title='展览 · 切割字形与双栏色场',pieces=['posters/02-new-design.svg'],
  method='先把展示字造到能切开整个版面，再把日期和展名嵌入剩余的实色矩形。大字是图，不是放大的普通标题。',
  grid='Hierarchical — 两条近等宽竖场，不同底色贯穿；横向装饰节奏、日期带和展示字分占连续高度。窄边框与主体相互错开，但不使用阴影。',
  type='两个展示字各占单栏大半高度，优先重建外轮廓和负形。展名约 S/13，英文约 S/17，日期约 S/21；署名是贴近竖轴的小字。',
  space='大形紧贴栏边，所有阅读文字落在纯色带里。白不是通用背景，只作为展示字与小事实的墨色。',
  shape='直立半圆柱、半圆碗、平口圆点与机械切割字形；切口、收口和内白必须逐一保持。',
  variation='上部圆弧节奏、小段条纹和巨型字形可共存，但不可把巨字缩成若干普通砖。',
  ban='不要用现成的粗黑中文字替代参考的构字；不要把直立半圆改成斜向叶形。',
  colors={'paper':'#FFFFFF','ink':'#050505','green':'#07964F','pink':'#F3579D','yellow':'#FFF035','blue':'#0759FD','orange':'#FF7829','purple':'#9B38ED'},pairs=[('paper','green',''),('paper','ink',''),('yellow','green','-large')],display='Study Sans',weight=900,size=76),
dict(id='04-club-partitions',title='俱乐部 · 黑框与曲面分区',pieces=['posters/03-tresor.svg'],
  method='先用黑线划出相互咬合的大分区，再用两种高饱和色与黑白曲面给分区施压。艺人名单占完全干净的矩形。',
  grid='Hierarchical — 横向分区交错成阶梯，一条主竖轴在中部、一条次竖轴在右侧；线宽约 S/90，黑框本身也是构图质量。',
  type='名单是首要可读信息：粗而不极黑，约 S/17，行距约 1；标签约 S/43，时间约 S/19。每组名单不拆散。',
  space='大白场与黑实地互相反转；矩形文字区贴着黑框，靠同一小内边距对齐。',
  shape='圆弧与自由曲线抵住硬边分区；描边只用于分区及曲面边界，不向其他孟菲斯作品推广。',
  variation='黑白负形可跨两区，日期压在底部一条硬分割事实带内。',
  ban='不要给所有物体加描边；不要让曲线切进名单的字。',
  colors={'paper':'#F9F9F6','ink':'#000000','blue':'#0969F9','red':'#FF3A06'},pairs=[('ink','paper',''),('ink','blue','')],display='Study Sans',weight=700,size=61),
dict(id='05-culture-monsters',title='文化科技 · 角色拼贴',pieces=['posters/04-ttxc.svg'],
  method='先让角色的眼、嘴与触手形成可辨识的角色库，再把角色格与条纹、星芒和主标题块拼接；图案与角色不是同一种素材。',
  grid='Modular — 上部约 42% 为不等跨拼贴，中央白色题名带为约 19%，下部事件信息占剩余面积；角色砖可占半格、一格或两格。',
  type='极黑字构成双语事件块；主标题约 S/9，次事件名约 S/11，英文说明约 S/33，地点约 S/38。',
  space='上部以满格角色造密度，中部白带负责识别，下部大片红色承载时间与场地。',
  shape='独眼弯体、软触手、露齿黑怪、圆嘴水母、放射细杆、尖芒与六角切片；每个角色保留不同的眼嘴比例。',
  variation='角色可裁在格边，主事件标题与日期不能被裁；一块细密图形与一块实色互相交替。',
  ban='不要用同一朵花代替不同角色；不要把上部每格都画成圆盘。',
  colors={'paper':'#FFFFFF','ink':'#030303','red':'#FF354A','pink':'#FD8CE5','yellow':'#FFE42C','blue':'#1768F6'},pairs=[('ink','paper',''),('ink','red',''),('paper','ink','')],display='Study Sans',weight=900,size=117),
dict(id='06-hackathon-space',title='技术活动 · 网格、窗口与积木',pieces=['posters/05-hackathon-windows.svg','posters/08-hackathon-blocks.svg'],
  method='把界面窗口、远程副本和积木空间当成同一个活动的材料；在图纸网格上建立一件主物体，再把日期和城市作为附属面或附属窗口。',
  grid='Hierarchical — 细网格间隔约 S/18，仅作共同坐标；一件主物体跨短边约 2/3，其他物体依照前后遮挡组织而不是平均分配。',
  type='窄而重的直立无衬线，展示字约 S/6 至 S/8，城市堆叠约 S/13，日期约 S/23；所有读字保持原字形比例，面上的文字跟随面作仿射变换。',
  space='用纯色物体隔开密网格；副本后退的每步约 S/100 到 S/45。主文字只落在最前层的完整面内。',
  shape='薄线窗口、连续的直角连接体、等轴立方体、圆柱、尖星与圆片；几何深度来自共享顶点和三种平面，不来自阴影。',
  variation='主角可以是窗口堆叠，也可以是一体的三维积木；两者共享网格、描边、字体和荧光配色。',
  ban='不要每张都套相同构图；不要让栈的前后关系切断标题；副本先画底和边，最后才画前景标签。',
  colors={'paper':'#FFFFF2','blue':'#1900F5','green':'#00ECA9','pink':'#FA4EF5','yellow':'#FBFF08','coral':'#FF6977','violet':'#7C42FF'},pairs=[('blue','paper',''),('paper','violet','')],display='Study Condensed',weight=700,size=163),
dict(id='07-type-built-week',title='设计周 · 字母即版面',pieces=['posters/06-san-diego.svg'],
  method='先用大字行把页面切成几条实墙，再用圆、三角与短色条替换特定字母的一部分。删除标题，整个版面就不能成立。',
  grid='Baseline-led — 四至五条几乎满短边宽的字行紧贴排列；字高与行距一起决定分区，小字只能进入字行留下的缺口。',
  type='单一极黑无衬线，主字行约 S/3.6；小项目清单约 S/41，底部事实约 S/36。展示字允许定制横向比例，事实文字不压缩。',
  space='纸色间隙细而均匀；实色图形属于字母结构而非覆盖在字母上的装饰。',
  shape='双色对角方、替代圆字的实色圆、替代横画的三条并置色条；不增加花、十字或角色。',
  variation='一行可出现一处彩色结构替代；连用彩色替代时字行的黑色质量仍保持主导。',
  ban='不要让彩色圆遮住项目清单；不要在字墙外再加图案边框。',
  colors={'paper':'#F6F0E5','ink':'#1C1A1B','green':'#005B32','blue':'#258CB4','purple':'#554699','yellow':'#FDC442','pink':'#F5AAA4','orange':'#FF5205'},pairs=[('ink','paper',''),('paper','ink','')],display='Study Sans',weight=900,size=282),
dict(id='08-forest-character',title='森林活动 · 角色与棋盘',pieces=['posters/07-forest.svg'],
  method='先建立一个能与眼睛相认的软体主角，再把棋盘当作硬的框架抵住它；角色所在的纯黄场与事实所在的蓝场形成上下节奏。',
  grid='Hierarchical — 左侧棋盘窄列约短边的 28%，上方横棋盘接入主图区；主角占中部右区，底部再分正文、竖日期和树三个区。',
  type='黑白粗字紧凑且有亲和感；主标识约 S/10，日期约 S/18，正文约 S/37。竖日期是单独的窄胶囊，不把正文一起旋转。',
  space='主角必须在整块黄底里舒展；棋盘仅在边缘改变尺度，不能退成细线格。',
  shape='三重叠扁圆的柔软身体、大小不一的双眼、锯齿树、硬棋盘与圆角日期柱。',
  variation='顶部标识与底部年份可以按参考被画幅裁切，近读事实保留完整。',
  ban='不要把角色眼睛设成对称圆点；不要让棋盘填进正文背景。',
  colors={'paper':'#FFFFFF','ink':'#000000','pink':'#F4A2C9','blue':'#4B53E6','yellow':'#FFE840','green':'#20A90D'},pairs=[('paper','blue',''),('ink','pink',''),('ink','yellow','')],display='Study Sans',weight=900,size=103),
dict(id='09-isometric-letter-stage',title='舞台 · 等轴文字建筑',pieces=['posters/09-konbin.svg'],
  method='先解出共享顶点的建筑，再在每个面的局部坐标内排字，最后统一投影；主标题是一座跨过积木的白桥。',
  grid='Diagonal — 两组约 ±0.425 的斜率与竖直线构成投影坐标，所有立体面严格共享端点；版面从上方远处小体块到下方巨大标题桥逐层前进。',
  type='窄重无衬线用尽面宽，面内留约宽度 3% 的安全边。不同面按所在面作相同仿射变换，不能在变换后凭屏幕坐标摆字。',
  space='白桥是最清晰的连续阅读面；其他面可密集，但不能用前景屋顶切断白桥上的文字。',
  shape='只用平行四边形、矩形与字；深度只靠共边、遮挡与异色面。',
  variation='屋顶文字可以随深度缩放；白桥两侧的标题字号分别计算，但墨迹高度接近。',
  ban='不要用阴影制造体积；不要在字已经跑出面后只用裁切掩盖错误。',
  colors={'paper':'#FFFFF3','ink':'#000000','yellow':'#FFDF06','blue':'#2836B5','red':'#FF2E05','green':'#22B88A'},pairs=[('yellow','ink',''),('yellow','blue',''),('ink','paper',''),('paper','green','-large')],display='Study Condensed',weight=700,size=190),
dict(id='10-molly-scenery',title='艺术活动 · 模块景观身份',pieces=[f'brand/{x}' for x in ['01-banner.svg','02-ribbon.svg','03-ribbon.svg','04-ribbon.svg','05-invitation-white.svg','06-invitation-blue.svg','07-bag.svg','08-bag.svg','09-badge.svg','10-badge.svg','11-leaflet.svg']],
  method='先画圆弧、花朵、种子与尖顶组成的有限材料库，再把材料搭成有高低的边缘景观。中心白场或蓝场由中英标题占领。',
  grid='Hierarchical — 横版沿底边建立不等高轮廓，两侧向上生长；竖幅可以先铺两个大模块，再把文字放在下面；手提袋用一处 L 形或横带，不得把同一底纹等比缩进所有格式。',
  type='展示是紧密的双行像素中文与较小像素英文；横幅中文约 S/9，英文约 S/15，窄物料中文约 S/7.4。普通正文用无衬线而不用像素字；字标与中文标题不得互相压住。',
  space='横版中心有真正连续的留白，图案不必铺满。窄幅大图占上方约 49%，文字占下方；小物料依照轮廓重新排，不缩放横幅。',
  shape='双半圆、同心弧、圆角折块、四圆瓣黄花、六瓣红花加黑点、菱形、六个空心圆、三角波与两片叶。花的外轮廓是圆瓣，不是同心菱形。',
  variation='白底与蓝底互换，黄花与红花分担焦点；条纹仅在窄脊和小块中出现；每个物料选择不同的模块组合。',
  ban='不要把边缘景观变成满版墙纸；不要把一张横幅的图案缩成所有物料共同的细条。',
  colors={'paper':'#FFFFFF','ink':'#080808','blue':'#276DB3','orange':'#F04D1B','yellow':'#F6C333','pink':'#EDC6C0','lightblue':'#CAE5F4','red':'#FF3235'},pairs=[('ink','paper',''),('paper','blue',''),('blue','paper','')],display='Study Pixel',weight=400,size=114)
]

def write(d):
    directory=ROOT/'systems'/d['id'];directory.mkdir(parents=True,exist_ok=True)
    record=dict(id=d['id'],title=d['title'],pieces=d['pieces'],design=f'systems/{d["id"]}/DESIGN.md')
    if (directory/'DESIGN.md').exists() and '--overwrite-original-drafts' not in sys.argv:
        print('Preserved reviewed system:',d['id'])
        return record
    palette='\n'.join(f'  {k}: "{v}"' for k,v in d['colors'].items())
    pairs='\n'.join(f'  {fg}-on-{bg}{suffix}: {{ backgroundColor: "{{colors.{bg}}}", textColor: "{{colors.{fg}}}" }}' for fg,bg,suffix in d['pairs'])
    values='、'.join(f'{k} `{v}`' for k,v in d['colors'].items())
    pieces='、'.join(f'[{p}](../../{p})' for p in d['pieces'])
    content=f'''# {d['title']}

从本轮复刻反推的系统假设，不是制作前约束。数值只陈述关系，不抄写一张稿的坐标。

> Use alone: 先读 Overview，再按具体格式建立 Layout。S = 1000 指短边的参考尺度；数值乘实际短边 / 1000。新内容先重排，不压缩阅读文字。当前文件尚未通过新内容迁移验证。

## Overview
Reference-derived graphic system — Build the relationships visible in the reconstructed work; never replace its composition with a generic Memphis motif kit. 原作者及具体字库不详；这里描述构成，不作作者归属。
World: {d['title']}适用于共享同一构成关系的一组文化、活动或品牌物料。共同部分是图形语法、文字层级与色彩关系；每件新内容带来自己的标题长度、事实密度和主次。
Method: {d['method']}
Amplitude: 保持参考的强度；是否降强度由新用途另行决定，不默默改成极简。
Anti-reference: 以中性页面加一排彩色几何图形便称完成。

## Images
只用原生矢量几何、活字与计算的平面关系，不把参考截图当作成品贴入。原图只供私有对照。图形缩放保持比例；新画幅重组图形区域，文字单独重排。

## Layout
Grid system: {d['grid']}
{d['space']}
组内间隔约为正文行高的半倍，组间至少一个正文行高；拥挤先改区域尺寸，不降低事实字的级别。

## Typography
{d['type']}
当前替代字库：Inter 400/700/900、Archivo variable、Noto Sans SC variable、Oswald 700；不是原字库确认结果。像素体系使用本轮制作的 Folio Pixel Study 替代。字体来源和授权见 ../../assets/fonts.json；已有 SVG 已内嵌字形，新内容必须重新补全所需字形，不能依赖本轮子集。

## Colors
{values}。这些颜色是参考色关系的屏幕近似；色块可以邻接，但不能因同属一种风格就在不同系统之间交换整套配色。每个实际文字与底色组合记录在 Tokens 的 pairs 内。

## Shapes
{d['shape']}
有限的形状库先校正轮廓，再复用；不能以同一外接框尺寸冒充同一形。

## Forms
Cover / Statement：主标题或主物体先读；读字不能被图案压住。
Collection / Reference：相关事实按同一轴与相同级别排列，读者能找到日期、地点、名单或正文。
Sequence：同一语法延续，场形和信息密度随内容转折。
新格式：按上述结构重组；没有证据的图表、阅读长文与交互界面暂不从此文件推导。

## Variations
{d['variation']}

## Do's and Don'ts
{d['ban']}
缩略图检验：先读主标题或主物体，再进入事实；移除配色，分区与层级仍成立。只复用可见关系，不把某件作品的逐格坐标写成通用规则。
复刻优先保留参考的颜色与小字；folio-check 对低对比配对的失败如实保留，不以改阈值消除。新原创输出应恢复可读性底线。
Caricature: 只保留颜色和几何，丢掉本文件的构图方法。

## Tokens

```yaml
colors:
{palette}
typography:
  display: {{ fontFamily: "{d['display']}, Study CJK, sans-serif", fontSize: {d['size']}, fontWeight: {d['weight']}, lineHeight: 1 }}
  body: {{ fontFamily: "Study Sans, Study CJK, sans-serif", fontSize: 24, fontWeight: 400, lineHeight: 1.4 }}
spacing:
  within: 12
  between: 24
pairs:
{pairs}
```

## Record
Folio version: 1.1.0. Template version: 14. Date: 2026-11-04.
Pieces: {pieces}
Evidence: 已有同图复刻及原图对照；只有图形一致性的局部证据。未做第二份新内容、独立制作或盲评，不能称为已验证的生成系统。
'''
    (directory/'DESIGN.md').write_text(content)
    facts=[]
    import re
    from html import unescape
    for p in d['pieces']:
        for t in re.findall(r'<text[^>]*>(.*?)</text>',(ROOT/p).read_text()):
            if t not in facts:facts.append(t)
    brief='# Reconstruction brief\n\n## Reader and outcome\n近距离观察参考构成、用于调试视觉 skill 的复刻练习；输出是可编辑 SVG，不是原作文件。\n\n## Facts\n'
    brief+='\n'.join('- `'+unescape(t).replace('`','')+'`' for t in facts)
    brief+='\n\n## Assumptions and gaps\n文字取自截图可辨认内容；微小文字有人工转录或近似，不保证逐字原样。原作者、原字库和授权归属未确认。部分几何仍近似，以对照板可见差异为准。本 brief 是复刻记录，不反写进 DESIGN.md。\n'
    (directory/'brief.md').write_text(brief)
    return record

if __name__=='__main__':
    (ROOT/'systems.json').write_text(json.dumps([write(d) for d in SYSTEMS],ensure_ascii=False,indent=2))
    print('Extracted 10 design-system hypotheses from the reviewed reconstruction set.')
