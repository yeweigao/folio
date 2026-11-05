# Type-built week · Letter walls

以下为新作品的施工规则；尺寸描述相对关系，活动内容另放简报。

> Use alone: 先读 Overview 和 Images，再按具体格式建立 Layout。S = 1000 指短边的参考尺度；数值乘实际短边 / 1000。由行宽推导的展示字尺寸单独计算。新内容先重排，不压缩阅读文字。

## Overview
Reference-derived graphic system — Build tightly stacked letter walls with geometric parts inside the letters; never scatter a motif kit around an ordinary title.
World: 本系统适用于以短标题为主体的一组文化、活动或品牌物料。共同部分是图形语法、文字层级与色彩关系；每件新内容带来自己的标题长度、事实密度和主次。
Method: 先用大字行把页面切成几条实墙，再用圆、三角与短色条替换特定字母的一部分。删除标题，整个版面就不能成立。
Amplitude: 保持大字行占满主体、黑色字身主导的强度；是否降强度由新用途另行决定。
Anti-reference: 以中性页面加一排彩色几何图形便称完成。

## Images
只用原生矢量几何、活字与计算的平面关系。图形缩放保持比例；新画幅重组字行与事实区，文字单独重排，不需要外部图像。

## Layout
Grid system: Baseline-led — 四至五条几乎满短边宽的字行紧贴排列；字高与行距一起决定分区，小字进入字行留下的缺口或字墙让出的独立事实区。
纸色间隙细而均匀；实色图形属于字母结构而非覆盖在字母上的装饰。
组内间隔约为正文行高的半倍，组间至少一个正文行高；拥挤先改区域尺寸，不降低事实字的级别。

## Typography
单一极黑无衬线；主字行按可用行宽、字数与总行数求字号，优先维持几乎满宽的字墙。小项目清单约 S/41，底部事实约 S/36。展示字允许定制横向比例，事实文字不压缩。
Study Sans（Inter）900 用于主字行，400 用于清单和正文，700 用于需要强调的事实；中文用相应字重的 Study CJK（Noto Sans SC）衔接。它们是已授权的替代字库，并非原字体鉴定；来源与 SIL OFL 1.1 授权见 [字体授权](../FONT-LICENSES.txt)。新内容必须补全所需字形，不能依赖已有 SVG 的子集。

## Colors
paper `#F6F0E5` 是底，ink `#1C1A1B` 是主字和事实；反白事实用 paper-on-ink。green `#005B32`、blue `#258CB4`、purple `#554699` 可在纸底上承担大字的结构替代。orange `#FF5205`、yellow `#FDC442`、pink `#F5AAA4` 保留作明亮图形；进入字形时，须留下足以独立辨认该字的 ink 笔画。圆盘独自承担字母或数字时使用近色 orange-glyph `#F54D05`，其纸底对比为 3.11:1，不以原 orange 承担独立字形。所有文字与底色组合列在 pairs：阅读文字至少 4.5:1，大字及独自承担字形的图形至少 3:1；彩色结构替代不用于阅读小字。

## Shapes
几何以整字格为尺度，直接接管笔画或一个字位，而非填进保留完整黑字的字腔。移除被替代区域的原黑笔，再造结构；不能只在普通字内部贴小方块。
双色对角方的边长约为字高，按对角线分两色，可接管一个完整字位或半字与邻字的共边；替代圆字的实色圆直径约为字高；替代横画的三条并置色条跨满原字宽，间隔与条厚同级，取消原竖笔，让三条独立矩形承担该字的节奏。它们保留字位与基线，不沿普通字的完整轮廓裁出彩色字体。
图形变化同时参与主标题字行与数字行，不把全部干预留给年份；主词行至少有一处整格替代和一处拆分笔画，具体字位随新词选择。必要时在小字事实区完整写明名称，保持辨认。不增加花、十字或角色。

## Forms
Cover / Statement：主标题或主物体先读；读字不能被图案压住。
Collection / Reference：相关事实按同一轴与相同级别排列，读者能找到日期、地点、名单或正文。
Sequence：同一语法延续，场形和信息密度随内容转折。
新格式：按上述结构重组；没有证据的图表、阅读长文与交互界面暂不从此文件推导。

## Variations
一行可出现一处彩色结构替代；连用彩色替代时字行的黑色质量仍保持主导。

## Do's and Don'ts
不要让彩色圆遮住项目清单；不要在字墙外再加图案边框。
缩略图检验：先读主标题或主物体，再进入事实；移除配色，分区与层级仍成立。不把某件作品的逐格坐标写成通用规则。
Caricature: 只保留颜色和几何，丢掉本文件的构图方法。

## Tokens

```yaml
colors:
  paper: "#F6F0E5"
  ink: "#1C1A1B"
  green: "#005B32"
  blue: "#258CB4"
  purple: "#554699"
  yellow: "#FDC442"
  pink: "#F5AAA4"
  orange: "#FF5205"
  orange-glyph: "#F54D05"
typography:
  display: { fontFamily: "Study Sans, Study CJK, sans-serif", fontWeight: 900, lineHeight: 1 }
  body: { fontFamily: "Study Sans, Study CJK, sans-serif", fontSize: 24, fontWeight: 400, lineHeight: 1.4 }
  facts: { fontFamily: "Study Sans, Study CJK, sans-serif", fontSize: 28, fontWeight: 700, lineHeight: 1.2 }
spacing:
  within: 17
  between: 34
pairs:
  ink-on-paper: { backgroundColor: "{colors.paper}", textColor: "{colors.ink}" }
  paper-on-ink: { backgroundColor: "{colors.ink}", textColor: "{colors.paper}" }
  green-on-paper-large: { backgroundColor: "{colors.paper}", textColor: "{colors.green}" }
  blue-on-paper-large: { backgroundColor: "{colors.paper}", textColor: "{colors.blue}" }
  purple-on-paper-large: { backgroundColor: "{colors.paper}", textColor: "{colors.purple}" }
  orange-glyph-on-paper-large: { backgroundColor: "{colors.paper}", textColor: "{colors.orange-glyph}" }
```

## Record
Folio version: 1.1.0. Template version: 14. Date: 2026-11-05.

复刻作品：[06-san-diego.svg](06-san-diego.svg)。

[独立迁移作品](transfer.svg)：基于新内容制作的最终采用版本，每套仅测试一个新简报，不能推断对所有内容或画幅的可靠性。
