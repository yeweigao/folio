# 构字分区封面

以短中文主张为中心的封面及其报告内页。参考只证实一个封面；正文、表格、时间线是从其构造提出的待验证扩展，不能称为已复刻的原始内页。

> Use alone: 先读 Overview 和 Images，再按 Layout 由 W × H 构造。S = 1000 是短边参考尺度，Tokens 中数值乘实际 S / 1000。读距要求较大字级时扩大阅读场、减少同时分组或分页，不压扁字形，不让黑线／色面挤小事实文字。

## Overview
Modern reference-derived De Stijl application, author unconfirmed — Build the main word at architectural scale across a thin ruled field, then let a few primary planes interrupt selected strokes and counters; attach secondary reading to the remaining cells; never lay a decorative grid over an ordinary title.
World: 以短中文主张为中心的封面及其报告内页。参考只证实一个封面；正文、表格、时间线是从其构造提出的待验证扩展，不能称为已复刻的原始内页。
Method: 先把新内容分成主张、解释、证据、同级比较和查阅项；以它们的关系决定阅读场和证据场，再引入本世界的线与色面。不要沿页码复制现成版式或沿参考的主题找装饰。
Amplitude: 复刻保留参考的图案幅度；新正文页先让阅读成立，再以本世界的关键关系维持身份。
Anti-reference: 普通白底文字页外加红黄蓝边框。

## Images
参考复刻中的照片来自用户截图的局部照片裁切，未把整页或文字版式作为图像贴入成品；它们的原摄影者未确认。新内容使用有来源的图片，不能重复旧参考照片作为新主题证据。图像按原比例等比裁切，人物脸／手及解释性对象必须保留；证据图标注来源与含义，概念图明确标注。图像本身不替代 live text。

## Layout
Grid system: Hierarchical — 封面主标题占 W 的约 0.72–0.86，字身高约 0.25–0.33S，放在跨越几个薄线分区的连续字带；字带上下保留可读的副标题／出处区域。画幅以二至四条竖线和三至五条横线划不等场，不建等格。主字墨迹与细线相交时仍完整可辨；主字之外各单元保持净距。报告页将主张缩到页标题级，把中间连续带合成大白阅读面，不按封面字格一格一段。
一般正文为一至两栏；表格同级列可等宽，时间线同级阶段可等距。长文字先合并图案占据的阅读格，再按语义分页。不可省略简报事实来维持色块。文字行距约 1.5，组间至少 1.4 个正文行高，墨迹离图片／粗结构线至少一正文行高。横版有稳定共享轴；竖版重排内容轨而不是把横页整体缩小。

## Typography
主字 Noto Sans SC 900，中文辅助 400／700；Latin 用 Lato 400／700。主字按可用字带宽和字数推导，保持字形比例；较长标题分两行并扩展字带，不能缩小全部阅读文字。正文内页不用构字字形承载段落。
Tokens 是可读的迁移起点：在 1280 × 720 的 read-alone 演示中正文约 20 px；投影须按读距提高到 26–32 px，并重排。复刻保留的截图微字与代用字体单独记为差异，不把它当作未来字号标准。新文字要嵌入完整所需字形子集，字体的授权说明见 [FONT-LICENSES.txt](../FONT-LICENSES.txt)。

## Colors
paper `#ebe5da`；ink `#080808`；red `#dc1c12`；yellow `#f7c506`；blue `#043a96`；white `#ffffff`。色名是功能：paper 是阅读底，ink 是结构和正文，原色负责该组声明的场／节点／强调，white 只反白在已检查的深底。参考原图的低对比小字在迁移中不沿用。

## Shapes
细结构线约 3–4，主字笔画远厚于线。大黑字优先使用可读的 Noto Sans SC 900；只有参考中明确的直角切分／内孔可改造，不能凭装饰毁掉新字。红、蓝、黄矩形以共边参与分区，只有少量小面嵌入字的内孔／笔画旁；不是每个字染一种色。台阶由重复直角折段连续上升，若不是数据就不附虚假坐标或数值。小箭头有起点方块、细杆和开放箭头，与主字保持级差。无圆角、圆形或阴影。

## Forms
封面在大字带外布置一组英文释义、日期／地点和一条行动说明；正文扩展把大字动作留在页题，把下方合成二栏阅读面；表格扩展把分区细线降成表的列轴，用同色数字和一处原色结论；时间线扩展采用单根细正交轴并以日期定位，台阶只有在阶段确实递进时才承担顺序；这些内页须实际生成验证，不能仅凭这个封面断言成立。

## Variations
正文页可去掉台阶、箭头及构字嵌色，仅保留大黑标题、细分区和一处原色面。原色面积和附加元素数量随内容分量变化；绝不填满留白。

## Do's and Don'ts
Do: 同组共享轴、同级同尺；正文与证据保持清楚的先后；所有固定文字可读且 live；小字对实际底色至少 4.5:1。Don't: 按内容盒一盒随机染原色、把粗轨画进字或数据、为保留图案缩小正文。Test: 换掉主题文字后，相同的线／面／类型角色仍能组织新正文、表格和顺序。Caricature: 只剩红黄蓝和黑格，内容在其他地方照常排。

## Tokens

```yaml
colors:
  paper: "#ebe5da"
  ink: "#080808"
  red: "#dc1c12"
  yellow: "#f7c506"
  blue: "#043a96"
  white: "#ffffff"
typography:
  display: { fontFamily: "Noto Sans SC, Lato, sans-serif", fontSize: 280, fontWeight: 900, lineHeight: 1.02 }
  heading: { fontFamily: "Lato, Noto Sans SC, sans-serif", fontSize: 72, fontWeight: 700, lineHeight: 1.1 }
  body: { fontFamily: "Lato, Noto Sans SC, sans-serif", fontSize: 28, fontWeight: 400, lineHeight: 1.5 }
  label: { fontFamily: "Lato, Noto Sans SC, sans-serif", fontSize: 22, fontWeight: 400, lineHeight: 1.4 }
spacing:
  line: 4
  thinLine: 1.5
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
Reference scope: IMG_8178.PNG · 独立封面 1 页。这些是现代参考应用，不声称蒙德里安原作或原字体鉴定。
Reconstruction pieces: [cover](cover.svg)。
Transfer: [长正文](transfer-01-reading.svg) · [表格](transfer-02-table.svg) · [时间线](transfer-03-timeline.svg)。制作者只持输入骨架、新简报、声明图片与字体；主流程复核了实际渲染。每套只有一个新简报。其中正文、表格和时间线是对单一封面构造的扩展，不能据此宣称原作者已有这些内页。
