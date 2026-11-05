# 开口折角项目提案

项目提案、进程、团队与多栏成果说明。稳定的是暖纸底、扁宽重标题、细导线和开口折角；每件决定内容组数、图像跨距与色面重心。

> Use alone: 先读 Overview 和 Images，再按 Layout 由 W × H 构造。S = 1000 是短边参考尺度，Tokens 中数值乘实际 S / 1000。读距要求较大字级时扩大阅读场、减少同时分组或分页，不压扁字形，不让黑线／色面挤小事实文字。

## Overview
Modern reference-derived De Stijl application, author unconfirmed — Build an open frame from a few thick right-angle brackets and thin cross-page guides; let text, evidence and primary fields answer those guides; never enclose every group in a black card.
World: 项目提案、进程、团队与多栏成果说明。稳定的是暖纸底、扁宽重标题、细导线和开口折角；每件决定内容组数、图像跨距与色面重心。
Method: 先把新内容分成主张、解释、证据、同级比较和查阅项；以它们的关系决定阅读场和证据场，再引入本世界的线与色面。不要沿页码复制现成版式或沿参考的主题找装饰。
Amplitude: 复刻保留参考的图案幅度；新正文页先让阅读成立，再以本世界的关键关系维持身份。
Anti-reference: 普通白底文字页外加红黄蓝边框。

## Images
参考复刻中的照片来自用户截图的局部照片裁切，未把整页或文字版式作为图像贴入成品；它们的原摄影者未确认。新内容使用有来源的图片，不能重复旧参考照片作为新主题证据。图像按原比例等比裁切，人物脸／手及解释性对象必须保留；证据图标注来源与含义，概念图明确标注。图像本身不替代 live text。

## Layout
Grid system: Hierarchical — 以 W 的 0.10–0.18 形成窄导航轨，其余合成一至三块不等的阅读／证据区域；对比同级项时区域内部可等分。薄导线沿内容边或穿过两组的同一轴，粗折角只在转折处支撑／压住标题或证据边。折角有两至三段直角路径、端头平切，厚度是薄导线的 12–18 倍（约 30–40，S=1000）；至少一侧开放。普通正文页允许一个导线而没有粗括号。
一般正文为一至两栏；表格同级列可等宽，时间线同级阶段可等距。长文字先合并图案占据的阅读格，再按语义分页。不可省略简报事实来维持色块。文字行距约 1.5，组间至少 1.4 个正文行高，墨迹离图片／粗结构线至少一正文行高。横版有稳定共享轴；竖版重排内容轨而不是把横页整体缩小。

## Typography
标题为宽重无衬线，Inter 900；正文和事实用 Inter 400，中文用 Noto Sans SC 对应 900／400。标题分行保持正常字形；复刻中的扁宽形来自替代字库校准，新文字不横向拉伸。
Tokens 是可读的迁移起点：在 1280 × 720 的 read-alone 演示中正文约 20 px；投影须按读距提高到 26–32 px，并重排。复刻保留的截图微字与代用字体单独记为差异，不把它当作未来字号标准。新文字要嵌入完整所需字形子集，字体的授权说明见 [FONT-LICENSES.txt](../FONT-LICENSES.txt)。

## Colors
paper `#eedfbd`；ink `#111111`；red `#bf2b22`；yellow `#ebc000`；blue `#086bb7`；white `#ffffff`。色名是功能：paper 是阅读底，ink 是结构和正文，原色负责该组声明的场／节点／强调，white 只反白在已检查的深底。参考原图的低对比小字在迁移中不沿用。

## Shapes
只保留两档线：薄导线和粗折角，不能用中间粗细填空。大圆母题是实心红圆或空心红环，外径约 0.22–0.52S；它定位交点或跨过裁切边，不在每段前重复。时间线的小红节点另按正文字高构造，直径约 0.5–0.9 个正文行高；每阶段可重复一个，数量由内容决定，不能套用大圆尺寸。蓝／黄为连续大矩形场，黑为结构，红为节点或短强调；稀疏平行细线只在一个边缘形成局部节奏。线、圆、斜导线和照片均是本参考的现代混合构造，不归为蒙德里安原作语法。

## Forms
封面把工作名安置在开口折角的转折端；正文在其余平静纸场中按语义分段；团队／成果以同级等宽列共用标题与基线；图像页沿导线排一大两小；时间线是正交阶梯折线，红节点按阶段连接，文字交替放在线段上／下并有净距；表格共用列轴，粗折角在表外，细行线在表内。

## Variations
章节可把蓝或黄扩成半场，再反转文字前景；最多一个大圆或粗折角承担主动作。信息密集页减少色面和装饰，保留两档线与宽重标题关系。

## Do's and Don'ts
Do: 同组共享轴、同级同尺；正文与证据保持清楚的先后；所有固定文字可读且 live；小字对实际底色至少 4.5:1。Don't: 按内容盒一盒随机染原色、把粗轨画进字或数据、为保留图案缩小正文。Test: 换掉主题文字后，相同的线／面／类型角色仍能组织新正文、表格和顺序。Caricature: 只剩红黄蓝和黑格，内容在其他地方照常排。

## Tokens

```yaml
colors:
  paper: "#eedfbd"
  ink: "#111111"
  red: "#bf2b22"
  yellow: "#ebc000"
  blue: "#086bb7"
  white: "#ffffff"
typography:
  display: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 160, fontWeight: 900, lineHeight: 1.02 }
  heading: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 72, fontWeight: 900, lineHeight: 1.1 }
  body: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 28, fontWeight: 400, lineHeight: 1.5 }
  label: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 22, fontWeight: 400, lineHeight: 1.4 }
spacing:
  line: 34
  thinLine: 2.1
  readingInset: 34
  groupGap: 42
pairs:
  ink-on-paper: { backgroundColor: "{colors.paper}", textColor: "{colors.ink}" }
  ink-on-yellow: { backgroundColor: "{colors.yellow}", textColor: "{colors.ink}" }
  white-on-blue: { backgroundColor: "{colors.blue}", textColor: "{colors.white}" }
  white-on-red: { backgroundColor: "{colors.red}", textColor: "{colors.white}" }
```

## Record
Folio version: 1.1.0. Template version: 14. Date: 2026-11-05.
Reference scope: IMG_8173.PNG · 12 页。这些是现代参考应用，不声称蒙德里安原作或原字体鉴定。
Reconstruction pieces: [01-cover](01-cover.svg)、[02-about-us](02-about-us.svg)、[03-our-team](03-our-team.svg)、[04-project-name](04-project-name.svg)、[05-project-concept](05-project-concept.svg)、[06-photo-board](06-photo-board.svg)、[07-project-stages](07-project-stages.svg)、[08-timeline](08-timeline.svg)、[09-stage-details](09-stage-details.svg)、[10-progress](10-progress.svg)、[11-outcomes](11-outcomes.svg)、[12-thank-you](12-thank-you.svg)。
Transfer: [长正文](transfer-01-reading.svg) · [表格](transfer-02-table.svg) · [时间线](transfer-03-timeline.svg)。制作者只持输入骨架、新简报、声明图片与字体；主流程复核了实际渲染。每套只有一个新简报。当前版本的大圆／小节点区分及线重由主流程澄清并对现有新作作相应修正，未再做全新上下文复测。
