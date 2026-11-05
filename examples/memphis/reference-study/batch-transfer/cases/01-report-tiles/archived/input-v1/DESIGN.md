# 方砖报告系统

从本轮复刻反推的系统假设，不是制作前约束。数值只陈述关系，不抄写一张稿的坐标。

> Use alone: 先读 Overview，再按具体格式建立 Layout。S = 1000 指短边的参考尺度；数值乘实际短边 / 1000。新内容先重排，不压缩阅读文字。当前文件尚未通过新内容迁移验证。

## Overview
Reference-derived graphic system — Build the relationships visible in the reconstructed work; never replace its composition with a generic Memphis motif kit. 原作者及具体字库不详；这里描述构成，不作作者归属。
World: 方砖报告系统适用于共享同一构成关系的一组文化、活动或品牌物料。共同部分是图形语法、文字层级与色彩关系；每件新内容带来自己的标题长度、事实密度和主次。
Method: 先给每页一个有方向的图案场——竖柱、横带、角块或双列；再让图案场的边界确定标题与正文的轴。标题用轻字搭重字，形成一条连续阅读路径。
Amplitude: 保持参考的强度；是否降强度由新用途另行决定，不默默改成极简。
Anti-reference: 以中性页面加一排彩色几何图形便称完成。

## Images
只用原生矢量几何、活字与计算的平面关系，不把参考截图当作成品贴入。原图只供私有对照。图形缩放保持比例；新画幅重组图形区域，文字单独重排。

## Layout
Grid system: Modular — 用正方形方砖建立条带，正文区合并方格。横版按 8–9 块排横带、5 块排竖带；封面允许两列四行的较大方砖。不同条带可用不同模块，不能把整套固定成一个绝对砖尺寸。
图案区连续无缝，文字区保留整块蓝或粉色。文字安全边为约 S/18；正文分两列或三个任务组，图案从不压在正文下。
组内间隔约为正文行高的半倍，组间至少一个正文行高；拥挤先改区域尺寸，不降低事实字的级别。

## Typography
轻重对比领先。展示字约 S/8，章标题约 S/10，正文约 S/48，导航约 S/52；这里是参考的近距离阅读层级。重字保持紧凑，轻字与重字的实际墨迹边界对齐。
当前替代字库：Inter 400/700/900、Archivo variable、Noto Sans SC variable、Oswald 700；不是原字库确认结果。像素体系使用本轮制作的 Folio Pixel Study 替代。字体来源和授权见 ../../assets/fonts.json；已有 SVG 已内嵌字形，新内容必须重新补全所需字形，不能依赖本轮子集。

## Colors
paper `#F8F6ED`、blue `#343D9F`、pink `#FA0056`、orange `#FF7619`、cream `#FFE5A6`。这些颜色是参考色关系的屏幕近似；色块可以邻接，但不能因同属一种风格就在不同系统之间交换整套配色。每个实际文字与底色组合记录在 Tokens 的 pairs 内。

## Shapes
八类有限砖：六瓣花、八角软星、十字、四圆、密齿圆、圆角折块、叶块、四分之一环。圆角折块有内缩直边，不能替换成满格扇形。
有限的形状库先校正轮廓，再复用；不能以同一外接框尺寸冒充同一形。

## Forms
Cover / Statement：主标题或主物体先读；读字不能被图案压住。
Collection / Reference：相关事实按同一轴与相同级别排列，读者能找到日期、地点、名单或正文。
Sequence：同一语法延续，场形和信息密度随内容转折。
新格式：按上述结构重组；没有证据的图表、阅读长文与交互界面暂不从此文件推导。

## Variations
同一图案库在竖柱、横带、角块中换位；蓝底、粉底与橙色半场形成页间节奏。

## Do's and Don'ts
不要在每页塞一条相同的横带；不要随机打乱已被参考固定的砖序。
缩略图检验：先读主标题或主物体，再进入事实；移除配色，分区与层级仍成立。只复用可见关系，不把某件作品的逐格坐标写成通用规则。
复刻优先保留参考的颜色与小字；folio-check 对低对比配对的失败如实保留，不以改阈值消除。新原创输出应恢复可读性底线。
Caricature: 只保留颜色和几何，丢掉本文件的构图方法。

## Tokens

```yaml
colors:
  paper: "#F8F6ED"
  blue: "#343D9F"
  pink: "#FA0056"
  orange: "#FF7619"
  cream: "#FFE5A6"
typography:
  display: { fontFamily: "Study Light, Study CJK, sans-serif", fontSize: 136, fontWeight: 100, lineHeight: 1 }
  body: { fontFamily: "Study Sans, Study CJK, sans-serif", fontSize: 24, fontWeight: 400, lineHeight: 1.4 }
spacing:
  within: 12
  between: 24
pairs:
  paper-on-blue: { backgroundColor: "{colors.blue}", textColor: "{colors.paper}" }
  paper-on-pink: { backgroundColor: "{colors.pink}", textColor: "{colors.paper}" }
  paper-on-orange: { backgroundColor: "{colors.orange}", textColor: "{colors.paper}" }
  blue-on-orange-large: { backgroundColor: "{colors.orange}", textColor: "{colors.blue}" }
```

## Record
Folio version: 1.1.0. Template version: 14. Date: 2026-11-04.
Pieces: [slides/01-cover.svg](../../slides/01-cover.svg)、[slides/02-contents.svg](../../slides/02-contents.svg)、[slides/03-background.svg](../../slides/03-background.svg)、[slides/04-profile.svg](../../slides/04-profile.svg)、[slides/05-vision.svg](../../slides/05-vision.svg)、[slides/06-history.svg](../../slides/06-history.svg)、[slides/07-work.svg](../../slides/07-work.svg)、[slides/08-responsibilities.svg](../../slides/08-responsibilities.svg)
Evidence: 已有同图复刻及原图对照；只有图形一致性的局部证据。未做第二份新内容、独立制作或盲评，不能称为已验证的生成系统。
