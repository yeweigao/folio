# 粗黑框线图文报告

图文报告、目录、章节与资料比较。稳定的是粗黑轨、薄照片框、白阅读面与红黄蓝附着关系；每件改变图片数量、标题带方向及正文跨度。

> Use alone: 先读 Overview 和 Images，再按 Layout 由 W × H 构造。S = 1000 是短边参考尺度，Tokens 中数值乘实际 S / 1000。读距要求较大字级时扩大阅读场、减少同时分组或分页，不压扁字形，不让黑线／色面挤小事实文字。

## Overview
Modern reference-derived De Stijl application, author unconfirmed — Build the reading area between a few thick orthogonal tracks, then let photographs cross a track with their own thin frame; keep the title and paragraphs on a calm white plane; never cover a finished ordinary page with a decorative lattice.
World: 图文报告、目录、章节与资料比较。稳定的是粗黑轨、薄照片框、白阅读面与红黄蓝附着关系；每件改变图片数量、标题带方向及正文跨度。
Method: 先把新内容分成主张、解释、证据、同级比较和查阅项；以它们的关系决定阅读场和证据场，再引入本世界的线与色面。不要沿页码复制现成版式或沿参考的主题找装饰。
Amplitude: 复刻保留参考的图案幅度；新正文页先让阅读成立，再以本世界的关键关系维持身份。
Anti-reference: 普通白底文字页外加红黄蓝边框。

## Images
参考复刻中的照片来自用户截图的局部照片裁切，未把整页或文字版式作为图像贴入成品；它们的原摄影者未确认。新内容使用有来源的图片，不能重复旧参考照片作为新主题证据。图像按原比例等比裁切，人物脸／手及解释性对象必须保留；证据图标注来源与含义，概念图明确标注。图像本身不替代 live text。

## Layout
Grid system: Hierarchical — 从 W × H 建立二至四个粗轨：靠边的竖轨离裁边约 0.04–0.10W，跨页横轨位于阅读区域的上下转折处，竖横不需每页同时出现。主体白面在轨内形成大阅读区，标题与正文用图片边或轨内净边对齐；实际墨迹离粗轨至少 0.6 个正文字高。不要把普通文字压进余下的小格。两栏普通页可为左图右文，也可上标题带、下双段正文，内容决定哪一面扩展。
一般正文为一至两栏；表格同级列可等宽，时间线同级阶段可等距。长文字先合并图案占据的阅读格，再按语义分页。不可省略简报事实来维持色块。文字行距约 1.5，组间至少 1.4 个正文行高，墨迹离图片／粗结构线至少一正文行高。横版有稳定共享轴；竖版重排内容轨而不是把横页整体缩小。

## Typography
主标题及中文用 Noto Sans SC 700；Latin 用 Lato 700／400，正文用 Noto Sans SC／Lato 400。章节数可成为一个大黄格中的主角；其余事实大小由读距而非照片数量决定。
Tokens 是可读的迁移起点：在 1280 × 720 的 read-alone 演示中正文约 20 px；投影须按读距提高到 26–32 px，并重排。复刻保留的截图微字与代用字体单独记为差异，不把它当作未来字号标准。新文字要嵌入完整所需字形子集，字体的授权说明见 [FONT-LICENSES.txt](../FONT-LICENSES.txt)。

## Colors
paper `#ffffff`；ink `#080808`；red `#f83227`；yellow `#ffc300`；blue `#1b67aa`；muted `#555555`；white `#ffffff`。色名是功能：paper 是阅读底，ink 是结构和正文，原色负责该组声明的场／节点／强调，white 只反白在已检查的深底。参考原图的低对比小字在迁移中不沿用。

## Shapes
粗轨在 S=1000 时约 18，照片框约 4；轨穿到裁边或进入邻接色场，照片框只包自身图像。照片可跨越粗轨，框沿保持清楚。黄矩形承接题头／章节，蓝色短条从图或轨伸出；红圆常被画幅裁去部分，直径约 0.32–0.55S。三角角切只在一处，圆／三角／雕像切图属于该现代参考的混合词汇。重复红节点只有在表示顺序或章节时才需要，实例数量随内容。

## Forms
目录把分组编号与组名挂在同一白阅读面；章节把编号黄面和标题白面合成一个共框横体；正文一至两段配一张跨轨大图或一组同尺度细节；比较页同级照片可等宽；数据页把图表留在大白面，粗轨不替代数据轴；表格使用细行线和对齐数字；时间线在轨内用直接标记的阶段行，不增加第二套卡片框。

## Variations
标题可进入一整条黄色带；照片可在一处用单色覆层，但不改变其事实含义。纯阅读页收去剪贴物，只保留黑轨、标题和一个连接轨的原色色面。

## Do's and Don'ts
Do: 同组共享轴、同级同尺；正文与证据保持清楚的先后；所有固定文字可读且 live；小字对实际底色至少 4.5:1。Don't: 按内容盒一盒随机染原色、把粗轨画进字或数据、为保留图案缩小正文。Test: 换掉主题文字后，相同的线／面／类型角色仍能组织新正文、表格和顺序。Caricature: 只剩红黄蓝和黑格，内容在其他地方照常排。

## Tokens

```yaml
colors:
  paper: "#ffffff"
  ink: "#080808"
  red: "#f83227"
  yellow: "#ffc300"
  blue: "#1b67aa"
  muted: "#555555"
  white: "#ffffff"
typography:
  display: { fontFamily: "Lato, Noto Sans SC, sans-serif", fontSize: 160, fontWeight: 700, lineHeight: 1.02 }
  heading: { fontFamily: "Lato, Noto Sans SC, sans-serif", fontSize: 72, fontWeight: 700, lineHeight: 1.1 }
  body: { fontFamily: "Lato, Noto Sans SC, sans-serif", fontSize: 28, fontWeight: 400, lineHeight: 1.5 }
  label: { fontFamily: "Lato, Noto Sans SC, sans-serif", fontSize: 22, fontWeight: 400, lineHeight: 1.4 }
spacing:
  line: 18
  thinLine: 1.5
  readingInset: 34
  groupGap: 42
pairs:
  ink-on-paper: { backgroundColor: "{colors.paper}", textColor: "{colors.ink}" }
  ink-on-yellow: { backgroundColor: "{colors.yellow}", textColor: "{colors.ink}" }
  white-on-blue: { backgroundColor: "{colors.blue}", textColor: "{colors.white}" }
  ink-on-red: { backgroundColor: "{colors.red}", textColor: "{colors.ink}" }
  muted-on-paper: { backgroundColor: "{colors.paper}", textColor: "{colors.muted}" }
```

## Record
Folio version: 1.1.0. Template version: 14. Date: 2026-11-05.
Reference scope: IMG_8167.JPG–IMG_8172.JPG · 11 页。这些是现代参考应用，不声称蒙德里安原作或原字体鉴定。
Reconstruction pieces: [01-bonjour](01-bonjour.svg)、[02-contents](02-contents.svg)、[03-chapter-01](03-chapter-01.svg)、[04-picture-pair](04-picture-pair.svg)、[05-photo-collection](05-photo-collection.svg)、[06-chapter-02](06-chapter-02.svg)、[07-picture-and-copy](07-picture-and-copy.svg)、[08-picture-details](08-picture-details.svg)、[09-chapter-03](09-chapter-03.svg)、[10-data-and-photo](10-data-and-photo.svg)、[11-title-band-and-photos](11-title-band-and-photos.svg)。
Transfer: [长正文](transfer-01-reading.svg) · [表格](transfer-02-table.svg) · [时间线](transfer-03-timeline.svg)。制作者只持输入骨架、新简报、声明图片与字体；主流程复核了实际渲染。每套只有一个新简报。
