# 展览 · 切割字形与双栏色场

从本轮复刻反推的系统假设，不是制作前约束。数值只陈述关系，不抄写一张稿的坐标。

> Use alone: 先读 Overview，再按具体格式建立 Layout。S = 1000 指短边的参考尺度；数值乘实际短边 / 1000。新内容先重排，不压缩阅读文字。当前文件尚未通过新内容迁移验证。

## Overview
Reference-derived graphic system — Build the relationships visible in the reconstructed work; never replace its composition with a generic Memphis motif kit. 原作者及具体字库不详；这里描述构成，不作作者归属。
World: 展览 · 切割字形与双栏色场适用于共享同一构成关系的一组文化、活动或品牌物料。共同部分是图形语法、文字层级与色彩关系；每件新内容带来自己的标题长度、事实密度和主次。
Method: 先把展示字造到能切开整个版面，再把日期和展名嵌入剩余的实色矩形。大字是图，不是放大的普通标题。
Amplitude: 保持参考的强度；是否降强度由新用途另行决定，不默默改成极简。
Anti-reference: 以中性页面加一排彩色几何图形便称完成。

## Images
只用原生矢量几何、活字与计算的平面关系，不把参考截图当作成品贴入。原图只供私有对照。图形缩放保持比例；新画幅重组图形区域，文字单独重排。

## Layout
Grid system: Hierarchical — 两条近等宽竖场，不同底色贯穿；横向装饰节奏、日期带和展示字分占连续高度。窄边框与主体相互错开，但不使用阴影。
大形紧贴栏边，所有阅读文字落在纯色带里。白不是通用背景，只作为展示字与小事实的墨色。
组内间隔约为正文行高的半倍，组间至少一个正文行高；拥挤先改区域尺寸，不降低事实字的级别。

## Typography
两个展示字各占单栏大半高度，优先重建外轮廓和负形。展名约 S/13，英文约 S/17，日期约 S/21；署名是贴近竖轴的小字。
当前替代字库：Inter 400/700/900、Archivo variable、Noto Sans SC variable、Oswald 700；不是原字库确认结果。像素体系使用本轮制作的 Folio Pixel Study 替代。字体来源和授权见 ../../assets/fonts.json；已有 SVG 已内嵌字形，新内容必须重新补全所需字形，不能依赖本轮子集。

## Colors
paper `#FFFFFF`、ink `#050505`、green `#07964F`、pink `#F3579D`、yellow `#FFF035`、blue `#0759FD`、orange `#FF7829`、purple `#9B38ED`。这些颜色是参考色关系的屏幕近似；色块可以邻接，但不能因同属一种风格就在不同系统之间交换整套配色。每个实际文字与底色组合记录在 Tokens 的 pairs 内。

## Shapes
直立半圆柱、半圆碗、平口圆点与机械切割字形；切口、收口和内白必须逐一保持。
有限的形状库先校正轮廓，再复用；不能以同一外接框尺寸冒充同一形。

## Forms
Cover / Statement：主标题或主物体先读；读字不能被图案压住。
Collection / Reference：相关事实按同一轴与相同级别排列，读者能找到日期、地点、名单或正文。
Sequence：同一语法延续，场形和信息密度随内容转折。
新格式：按上述结构重组；没有证据的图表、阅读长文与交互界面暂不从此文件推导。

## Variations
上部圆弧节奏、小段条纹和巨型字形可共存，但不可把巨字缩成若干普通砖。

## Do's and Don'ts
不要用现成的粗黑中文字替代参考的构字；不要把直立半圆改成斜向叶形。
缩略图检验：先读主标题或主物体，再进入事实；移除配色，分区与层级仍成立。只复用可见关系，不把某件作品的逐格坐标写成通用规则。
复刻优先保留参考的颜色与小字；folio-check 对低对比配对的失败如实保留，不以改阈值消除。新原创输出应恢复可读性底线。
Caricature: 只保留颜色和几何，丢掉本文件的构图方法。

## Tokens

```yaml
colors:
  paper: "#FFFFFF"
  ink: "#050505"
  green: "#07964F"
  pink: "#F3579D"
  yellow: "#FFF035"
  blue: "#0759FD"
  orange: "#FF7829"
  purple: "#9B38ED"
typography:
  display: { fontFamily: "Study Sans, Study CJK, sans-serif", fontSize: 76, fontWeight: 900, lineHeight: 1 }
  body: { fontFamily: "Study Sans, Study CJK, sans-serif", fontSize: 24, fontWeight: 400, lineHeight: 1.4 }
spacing:
  within: 12
  between: 24
pairs:
  paper-on-green: { backgroundColor: "{colors.green}", textColor: "{colors.paper}" }
  paper-on-ink: { backgroundColor: "{colors.ink}", textColor: "{colors.paper}" }
  yellow-on-green-large: { backgroundColor: "{colors.green}", textColor: "{colors.yellow}" }
```

## Record
Folio version: 1.1.0. Template version: 14. Date: 2026-11-04.
Pieces: [posters/02-new-design.svg](../../posters/02-new-design.svg)
Evidence: 已有同图复刻及原图对照；只有图形一致性的局部证据。未做第二份新内容、独立制作或盲评，不能称为已验证的生成系统。
