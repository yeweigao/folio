# 粗框分区知识演示

需要正文、定义、比较、表格、数据与阶段说明的演示。稳定的是粗黑分区、窄粗标题、圆润正文及少量被裁切的形状；每件按阅读任务调整分区，不能先定装饰数量。

> Use alone: 先读 Overview 和 Images，再按 Layout 由 W × H 构造。S = 1000 是短边参考尺度，Tokens 中数值乘实际 S / 1000。读距要求较大字级时扩大阅读场、减少同时分组或分页，不压扁字形，不让黑线／色面挤小事实文字。

## Overview
Modern reference-derived De Stijl application, author unconfirmed — Build unequal white reading fields with thick black horizontal and vertical divisions; set a condensed title inside the lead field and align paragraphs, comparisons and data beneath it; never substitute primary-colour furniture for the argument.
World: 需要正文、定义、比较、表格、数据与阶段说明的演示。稳定的是粗黑分区、窄粗标题、圆润正文及少量被裁切的形状；每件按阅读任务调整分区，不能先定装饰数量。
Method: 先把新内容分成主张、解释、证据、同级比较和查阅项；以它们的关系决定阅读场和证据场，再引入本世界的线与色面。不要沿页码复制现成版式或沿参考的主题找装饰。
Amplitude: 复刻保留参考的图案幅度；新正文页先让阅读成立，再以本世界的关键关系维持身份。
Anti-reference: 普通白底文字页外加红黄蓝边框。

## Images
参考复刻中的照片来自用户截图的局部照片裁切，未把整页或文字版式作为图像贴入成品；它们的原摄影者未确认。新内容使用有来源的图片，不能重复旧参考照片作为新主题证据。图像按原比例等比裁切，人物脸／手及解释性对象必须保留；证据图标注来源与含义，概念图明确标注。图像本身不替代 live text。

## Layout
Grid system: Hierarchical — 以一条近边竖轨和一条横轨建立不对称主阅读面；轨厚约 18–22（S=1000）。需要并列论点时在白面内建立隐式的二或三列，共用标题、行高与底线；不得因为整体不对称而破坏真实同级项的等宽比较。题头多在上缘，正文实际墨迹离轨至少一个正文字高。细表格线／数据轴单独降到 1–2。白阅读区至少容纳当前所有文字；装饰先退、内容后分页。
一般正文为一至两栏；表格同级列可等宽，时间线同级阶段可等距。长文字先合并图案占据的阅读格，再按语义分页。不可省略简报事实来维持色块。文字行距约 1.5，组间至少 1.4 个正文行高，墨迹离图片／粗结构线至少一正文行高。横版有稳定共享轴；竖版重排内容轨而不是把横页整体缩小。

## Typography
Latin 标题用 Oswald 700（窄粗），正文用 Nunito 400，事实强调用 Nunito 700；中文标题与正文用 Noto Sans SC 700／400。标题的窄与正文的圆形成角色差异，不把粗窄字体铺成整段正文。
Tokens 是可读的迁移起点：在 1280 × 720 的 read-alone 演示中正文约 20 px；投影须按读距提高到 26–32 px，并重排。复刻保留的截图微字与代用字体单独记为差异，不把它当作未来字号标准。新文字要嵌入完整所需字形子集，字体的授权说明见 [FONT-LICENSES.txt](../FONT-LICENSES.txt)。

## Colors
paper `#ffffff`；ink `#080808`；red `#dc2f26`；yellow `#ffc500`；blue `#086eac`；muted `#505050`；white `#ffffff`。色名是功能：paper 是阅读底，ink 是结构和正文，原色负责该组声明的场／节点／强调，white 只反白在已检查的深底。参考原图的低对比小字在迁移中不沿用。

## Shapes
粗轨端头平切，角为直角，无阴影与圆角。原色色场紧贴粗轨、画幅边或相邻阅读面；黄常承接标题，红承接另一论点，蓝承接图示。圆可以裁入边缘，直径约 0.22–0.42S，或作为真实步骤节点；斜角只在一个角切入，不变成全页背景。细线描插图与照片作为有来源的内容进入白格，圆与三角是现代课件的混合构造。

## Forms
长正文用判断式标题、二段文字及必要证据；概念集合在同一级隐式等列中排组名、定义；比较把真实两项分到不同色面而保留相同阅读轴；表格列宽按标签和数值计算，单位在表头、数字对齐；时间线以细连接线和可读阶段标题串起节点；图表直接标单位与类别，粗黑结构在绘图区外，数据语义决定图种；结论只重申前页已证明的判断。

## Variations
一页可以把黄面扩成主阅读场，或用一组圆节点承载章节顺序；普通正文不必带圆、三角或插图。源参考的饼图只在复刻中保留，新内容优先按数据问题使用直标条形／折线／表格。

## Do's and Don'ts
Do: 同组共享轴、同级同尺；正文与证据保持清楚的先后；所有固定文字可读且 live；小字对实际底色至少 4.5:1。Don't: 按内容盒一盒随机染原色、把粗轨画进字或数据、为保留图案缩小正文。Test: 换掉主题文字后，相同的线／面／类型角色仍能组织新正文、表格和顺序。Caricature: 只剩红黄蓝和黑格，内容在其他地方照常排。

## Tokens

```yaml
colors:
  paper: "#ffffff"
  ink: "#080808"
  red: "#dc2f26"
  yellow: "#ffc500"
  blue: "#086eac"
  muted: "#505050"
  white: "#ffffff"
typography:
  display: { fontFamily: "Oswald, Noto Sans SC, sans-serif", fontSize: 160, fontWeight: 700, lineHeight: 1.02 }
  heading: { fontFamily: "Oswald, Noto Sans SC, sans-serif", fontSize: 72, fontWeight: 700, lineHeight: 1.1 }
  body: { fontFamily: "Nunito, Noto Sans SC, sans-serif", fontSize: 28, fontWeight: 400, lineHeight: 1.5 }
  label: { fontFamily: "Nunito, Noto Sans SC, sans-serif", fontSize: 22, fontWeight: 400, lineHeight: 1.4 }
spacing:
  line: 20
  thinLine: 1.5
  readingInset: 34
  groupGap: 42
pairs:
  ink-on-paper: { backgroundColor: "{colors.paper}", textColor: "{colors.ink}" }
  ink-on-yellow: { backgroundColor: "{colors.yellow}", textColor: "{colors.ink}" }
  white-on-blue: { backgroundColor: "{colors.blue}", textColor: "{colors.white}" }
  white-on-red: { backgroundColor: "{colors.red}", textColor: "{colors.white}" }
  muted-on-paper: { backgroundColor: "{colors.paper}", textColor: "{colors.muted}" }
```

## Record
Folio version: 1.1.0. Template version: 14. Date: 2026-11-05.
Reference scope: IMG_8174.PNG–IMG_8177.PNG · 20 页（未给的 3/5 不补作复刻）。这些是现代参考应用，不声称蒙德里安原作或原字体鉴定。
Reconstruction pieces: [01-cover](01-cover.svg)、[02-contents](02-contents.svg)、[03-section](03-section.svg)、[04-whoa](04-whoa.svg)、[05-reading-list](05-reading-list.svg)、[06-concept-review](06-concept-review.svg)、[07-team](07-team.svg)、[08-big-number](08-big-number.svg)、[09-key-figures](09-key-figures.svg)、[10-problem-solution](10-problem-solution.svg)、[11-graph](11-graph.svg)、[12-infographic](12-infographic.svg)、[13-table](13-table.svg)、[14-map](14-map.svg)、[15-timeline](15-timeline.svg)、[16-percentages](16-percentages.svg)、[17-photo-board](17-photo-board.svg)、[18-conclusions](18-conclusions.svg)、[19-awesome-words](19-awesome-words.svg)、[20-thanks](20-thanks.svg)。
Transfer: [长正文](transfer-01-reading.svg) · [表格](transfer-02-table.svg) · [时间线](transfer-03-timeline.svg)。制作者只持输入骨架、新简报、声明图片与字体；主流程复核了实际渲染。每套只有一个新简报。
