# 方砖报告系统

用连续方砖分区、轻重标题和整色阅读场组织项目报告与系列说明页。

> Use alone: 先读 Overview 与 Shapes，再按 Layout 建立画幅。S = 1000 是短边参考尺度；尺寸乘实际短边 / 1000，由模块推导的尺寸只计算一次。新内容先改分区和换行，再增页，不压扁字形或缩小事实文字。

## Overview
Memphis-derived report graphics, geometric tile construction — Build a continuous tile field that gives the report its reading edges; never scatter independent symbols around a neutral page. 原作者不详，不作个人归属。
World: 用于有标题、分组事实和项目进程的报告、章节页与文化项目说明。每件保留无缝方砖带、有限轮廓库和轻／重成对标题；主题决定条带方向、跨距、内容组数与图案顺序。
Method: 先分出主标题与可查阅事实组；选择竖柱、横带、角块或双列作为图案场，使场边成为文字轴。把相邻事实合成整色区域，再以轻字引题、重字命名重点。图案场在内容转折时改变方向或宽度。
Amplitude: 保留大色场与满格图形；安静页减少图案面积，仍保留完整砖宽和轻重标题关系。
Anti-reference: 把通用几何平均排在每页页脚，正文再独立居中。

## Images
只用原生矢量路径与活字，不用照片、纹理或截图。图形按 Shapes 生成，砖内路径等比缩放，裁切只发生在砖边；横竖换幅时重排整砖。图案场接画幅边或文字场的整齐边界，不浮在正文上。

## Layout
Grid system: Modular — 用正方形模块 u 铺成连续条带；文字区域合并若干模块，不逐格塞字。
沿选定条带的整边等分：横向长带取 8–9 砖，贯穿短边的竖带取 5 砖；强调页可用两列四行的大砖场。不同条带可用不同 u，同一连续场只用一个 u。依据内容在四种场形中选择，不固定其所在边或复制砖序。
主阅读场用 blue 或 pink，orange 可承担副阅读场。文字可见墨迹离场边至少 55；正文分两列或三个任务组。图案与阅读场共边，无卡片圆角、阴影或额外沟槽。文字与相邻图形净距至少一个正文行高；组内净距 12，组间净距至少 34，均从可见墨迹量起。
横幅让长边承接横带或双列边场；竖幅把长正文沿场边延伸；方幅可把角块扩大为双列。密度增加时合并更多文字格或增页，不把图案缩成细小贴纸。

## Typography
Study Sans 映射 Inter 400/700/900；Study Light 映射 Archivo variable，使用 100；Study CJK 映射 Noto Sans SC variable，按角色使用 100/400/700/900。均为 SIL OFL 1.1；来源与授权见 ../FONT-LICENSES.txt。新内容嵌入全部所需字形，不依赖旧文件子集。
主标题的轻／重两段同为 136、行高 1.0：Latin 用 Study Light 100／Study Sans 900，中文用 Study CJK 100／900。两段对齐实际墨迹左边，混排时对齐字身；章节标题用 100 的轻／重配对。长标题换行并扩展文字场，重段不得降成正文。
分组标题 34／700，正文与事实 24／400、行高 1.4，导航 22／400、行高 1.3；这是最小阅读级。正文保持正常字宽，轻字不代替小字。数字沿用所属角色字库，强调数字可用轻标题级，但不成为第二主标题。

## Colors
blue `#343D9F` 是主要阅读场和反白图形；pink `#FA0056` 是轮换阅读场及高强度砖底；orange `#FF7619` 是副场、折块和环形。paper `#F8F6ED` 与 cream `#FFE5A6` 是浅砖底和图形前景，paper 也是 blue 上的阅读墨色。ink `#111118` 只承担浅底、pink 与 orange 上的阅读文字，不另造黑色大场。
条带内交替深底浅形与浅底深形：blue 配 paper／cream，pink 配 paper／cream，orange 配 blue／pink；颜色改变不改变轮廓。
正文只用 paper-on-blue 或 ink-on-paper／cream／pink／orange。paper-on-pink、blue-on-orange 仅供大字。所有实际阅读配对至少 4.5:1，大字至少 3:1；大字须在最终输出达到普通字 24px 或粗字 18.7px，不满足时改用该底色允许的阅读墨色。

## Shapes
每砖的局部单位为 u；路径无描边、阴影或立体侧面。各形按下列比例居中，环类允许接边；下列构造只定义砖内形状，不规定页面排列。
- 六瓣花：六个相同短圆瓣绕中心每 60° 相接；外半径 0.43u、谷半径 0.20u，瓣尖与谷底都用连续圆弧连接。保留六个圆瓣，不伸成长尖星。
- 八瓣软星：八个等角宽瓣，外半径 0.45u、谷半径 0.28u；瓣顶圆、谷内凹圆，形成厚实放射轮廓，不用尖锐三角齿。
- 斜向圆 X：两条长 0.92u、宽 0.28u 的圆头条以 +45°／−45° 交叠成一条合并路径；端头半径为条宽的一半。四端朝砖的四角，中心饱满，不能转成水平／竖直加号或直角十字。
- 四圆：四个直径 0.48u 的圆按 2×2 排列，圆心间距 0.50u；保持圆形与细小中央十字负形，不连成四瓣花。
- 十六瓣放射块：16 个等角圆瓣连接外半径 0.46u 与谷半径 0.39u，瓣顶略收、肩部圆滑。保留浅圆谷和短芒，不画方齿、径向平边或机械齿轮。
- 圆角折块：厚 0.32u 的直角带构成折返；外转弯半径 0.50u、内转弯半径 0.18u，留下直边凹口，不能填成实心扇形。
- 方叶：在 0.68u 正方形内保留一对对角直角，另一对角各以半径 0.28u 的四分之一圆收圆；四边仍有直线段。它是两个角收圆的方块，不是两端尖、全由弧边围出的透镜叶。
- 四分之一环：同心四分之一圆外半径 u、内半径 0.52u，两端沿砖边平切；内孔露出砖底，可与邻砖的圆角折块接续。

## Forms
Cover / Statement：轻段引入、重段落题，一个连续图案场划出标题边界；不增加第二个同级主角。
Collection / Reference：同级分组标题与共享基线组织事实，图案只分区；不把每条事实放进装饰砖。
Sequence：图案场方向或跨距随阶段转折，文字组沿场边延续；不让每页复制同一横带。
Argument / Comparison：证据留在整色阅读场，用直接标注与共同尺度说明；图案不代替数据。

## Variations
允许砖旋转 90°、180° 或 270°，保留 X 对角方向和方叶直边；允许条带换向、改宽与重排砖序。每个连续场至少同时包含圆瓣、直边凹口和圆弧三类轮廓，避免一种花占满全部砖。图案面积改变时，砖内几何和文字级差不变。

## Do's and Don'ts
缩略图先读轻／重主标题，再读分组与事实；灰度中仍看见完整阅读场与连续砖场。检查 X 四端朝角、圆瓣不是齿轮、方叶仍有直边。事实不压图、不截断、不用图形掩盖溢出。
Caricature: 只换明亮颜色，却把有限轮廓画成任意花、加号和尖叶。

## Tokens

```yaml
colors:
  paper: "#F8F6ED"
  blue: "#343D9F"
  pink: "#FA0056"
  orange: "#FF7619"
  cream: "#FFE5A6"
  ink: "#111118"
typography:
  display-light: { fontFamily: "Study Light, Study CJK, sans-serif", fontSize: 136, fontWeight: 100, lineHeight: 1 }
  display-heavy: { fontFamily: "Study Sans, Study CJK, sans-serif", fontSize: 136, fontWeight: 900, lineHeight: 1 }
  chapter-light: { fontFamily: "Study Light, Study CJK, sans-serif", fontSize: 100, fontWeight: 100, lineHeight: 1 }
  chapter-heavy: { fontFamily: "Study Sans, Study CJK, sans-serif", fontSize: 100, fontWeight: 700, lineHeight: 1 }
  group: { fontFamily: "Study Sans, Study CJK, sans-serif", fontSize: 34, fontWeight: 700, lineHeight: 1.15 }
  body: { fontFamily: "Study Sans, Study CJK, sans-serif", fontSize: 24, fontWeight: 400, lineHeight: 1.4 }
  navigation: { fontFamily: "Study Sans, Study CJK, sans-serif", fontSize: 22, fontWeight: 400, lineHeight: 1.3 }
spacing:
  within: 12
  between: 34
  reading-inset: 55
pairs:
  paper-on-blue: { backgroundColor: "{colors.blue}", textColor: "{colors.paper}" }
  ink-on-paper: { backgroundColor: "{colors.paper}", textColor: "{colors.ink}" }
  ink-on-cream: { backgroundColor: "{colors.cream}", textColor: "{colors.ink}" }
  ink-on-pink: { backgroundColor: "{colors.pink}", textColor: "{colors.ink}" }
  ink-on-orange: { backgroundColor: "{colors.orange}", textColor: "{colors.ink}" }
  paper-on-pink-large: { backgroundColor: "{colors.pink}", textColor: "{colors.paper}" }
  blue-on-orange-large: { backgroundColor: "{colors.orange}", textColor: "{colors.blue}" }
```

## Record
Folio version: 1.1.0. Template version: 14. Date: 2026-11-05.

复刻作品：[01-cover.svg](01-cover.svg)、[02-contents.svg](02-contents.svg)、[03-background.svg](03-background.svg)、[04-profile.svg](04-profile.svg)、[05-vision.svg](05-vision.svg)、[06-history.svg](06-history.svg)、[07-work.svg](07-work.svg)、[08-responsibilities.svg](08-responsibilities.svg)。

[独立迁移作品](transfer.svg)：基于新内容制作的最终采用版本，每套仅测试一个新简报，不能推断对所有内容或画幅的可靠性。
