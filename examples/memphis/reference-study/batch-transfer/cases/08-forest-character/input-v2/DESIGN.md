# Forest character · Soft body and checker frame

以下为新作品的施工规则；尺寸描述相对关系，活动内容另放简报。

> Use alone: 先读 Overview 和 Images，再按具体格式建立 Layout。S = 1000 指短边的参考尺度；数值乘实际短边 / 1000。由身体、棋盘或文字跨度推导的尺寸单独计算。新内容先重排，不压缩阅读文字。

## Overview
Reference-derived graphic system — Build a blue-violet soft character with adjoining protruding white eyes inside a black-and-white checker frame; never substitute a generic mascot and decorative border.
World: 本系统适用于以森林活动角色为主视觉的一组物料。共同部分是角色构造、棋盘框架与固定色彩职能；每件新内容带来自己的标题长度、事实密度和主次。
Method: 先画三层扁圆躯干和大白眼，再以硬棋盘围出黄色角色场；把蓝紫资料场、粉色日期柱和黑底绿树连接成另一组信息关系。
Amplitude: 保持大角色、粗棋盘与纯色分区的强度；是否降强度由新用途另行决定。
Anti-reference: 以中性页面加一排彩色几何图形便称完成。

## Images
只用原生矢量几何、活字与计算的平面关系，不需要外部图像。整体角色均匀缩放，身体、眼白和瞳孔分别保持比例；换画幅时重组区域，不拉伸角色。

## Layout
Grid system: Hierarchical — 从 W × H 中先分出相接的黄色角色场与蓝紫资料场；棋盘沿角色场的两个相邻边连接成框。竖幅可用约短边 28% 的窄列接入上方横带；宽幅可重新分配两场，但保留框与角色、正文与日期和树的邻接关系。
从窄列宽推导棋盘格宽，使窄列内有数格交替的实心黑白粗格；横带可使用同一格宽或其一半，不把整列变成单格，也不退成细线网格。黄色场须给身体和突出的眼白留出完整轮廓，角色保持最大连续前景形。
资料场先排正文，再留独立粉色竖日期胶囊；绿树必须占独立的黑色纵面板，面板与蓝紫正文区相接，不能让树直接落在蓝紫底上。字段增加时扩大资料场或重排行列。
组内间隔约为正文行高的半倍，组间至少一个正文行高；拥挤先改区域尺寸，不降低事实字的级别。

## Typography
黑白粗字紧凑且有亲和感；主标识约 S/10，日期约 S/18，正文约 S/37。竖日期是单独的窄胶囊，不把正文一起旋转。
Study Sans（Inter）900 用于主标识和大标题，700 用于日期与强调事实，400 用于正文；中文用相应字重的 Study CJK（Noto Sans SC）衔接。它们是已授权的替代字库，并非原字体鉴定；来源与 SIL OFL 1.1 授权见 [fonts.json](../../assets/fonts.json)。新内容必须补全所需字形，不能依赖已有 SVG 的子集。

## Colors
yellow `#FFE840` 只作角色场；blue `#4B53E6` 同时作三层躯干与资料场。paper `#FFFFFF` 与 ink `#000000` 组成棋盘、眼白和瞳孔。pink `#F4A2C9` 作日期胶囊及可选标识底带，不作躯干或棋盘浅格。green `#20A90D` 只作独立黑面板上的树形。文字用黄底黑字、粉底黑字、蓝紫底白字或黑底白字；每个文字组合列在 pairs，阅读文字至少 4.5:1，大字至少 3:1。

## Shapes
用三个等宽的水平扁椭圆上下重叠成躯干，总体高约为体宽的三分之二；重叠处仍显出三层波形侧边。眼白是相接或轻微重叠的两枚竖椭圆，一只略大；眼高约为躯干总高的一半，眼白顶部越过身体上沿约眼高的四分之一。黑色竖椭圆瞳孔置于白眼内，不把两眼分离、缩成圆点或完全收进身体。
树用层叠锯齿轮廓和直树干；棋盘用实心方格，日期柱两端半圆。复用时保留各自比例，不以同一外接框冒充同一形。

## Forms
Cover / Statement：主标题或主物体先读；读字不能被图案压住。
Collection / Reference：相关事实按同一轴与相同级别排列，读者能找到日期、地点、名单或正文。
Sequence：同一语法延续，场形和信息密度随内容转折。
新格式：按上述结构重组；没有证据的图表、阅读长文与交互界面暂不从此文件推导。

## Variations
角色场与资料场可随画幅改变面积与排列；保留角色构造及色彩分工。顶部标识或装饰性大字允许出血，须仍可辨认；日期、地点、正文等固定事实保留完整。

## Do's and Don'ts
不要把角色眼睛设成对称圆点；不要让棋盘填进正文背景。
缩略图检验：先读主标题或主物体，再进入事实；移除配色，分区与层级仍成立。不把某件作品的逐格坐标写成通用规则。
Caricature: 只保留颜色和几何，丢掉本文件的构图方法。

## Tokens

```yaml
colors:
  paper: "#FFFFFF"
  ink: "#000000"
  pink: "#F4A2C9"
  blue: "#4B53E6"
  yellow: "#FFE840"
  green: "#20A90D"
typography:
  display: { fontFamily: "Study Sans, Study CJK, sans-serif", fontSize: 103, fontWeight: 900, lineHeight: 1 }
  body: { fontFamily: "Study Sans, Study CJK, sans-serif", fontSize: 27, fontWeight: 400, lineHeight: 1.4 }
  date: { fontFamily: "Study Sans, Study CJK, sans-serif", fontSize: 56, fontWeight: 700, lineHeight: 1 }
spacing:
  within: 12
  between: 24
pairs:
  paper-on-blue: { backgroundColor: "{colors.blue}", textColor: "{colors.paper}" }
  ink-on-pink: { backgroundColor: "{colors.pink}", textColor: "{colors.ink}" }
  ink-on-yellow: { backgroundColor: "{colors.yellow}", textColor: "{colors.ink}" }
  paper-on-ink: { backgroundColor: "{colors.ink}", textColor: "{colors.paper}" }
```

## Record
Folio version: 1.1.0. Template version: 14. Date: 2026-11-05.
Pieces: [posters/07-forest.svg](../../posters/07-forest.svg)
Evidence: 一份新内容迁移样本 [v1](../../batch-transfer/cases/08-forest-character/frozen-v1/poster.png) 在 [identity](../../batch-transfer/evaluation/identity-v1.json) 中部分通过，在 [structure](../../batch-transfer/evaluation/structure-v1.json) 与 [craft](../../batch-transfer/evaluation/craft-v1.json) 中通过。完整判据与像素证据见评估记录。
Changes: 补明眼身比例、黑白棋盘和固定色彩职能，改为按画幅与构件比例施工；清理外部参考依赖，明确字体与对比度底线。修订文件尚待新的迁移测试，未宣称偏差已修复。
