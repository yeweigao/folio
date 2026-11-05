# 舞台 · 等轴文字建筑

从本轮复刻反推的系统假设，不是制作前约束。数值只陈述关系，不抄写一张稿的坐标。

> Use alone: 先读 Overview，再按具体格式建立 Layout。S = 1000 指短边的参考尺度；数值乘实际短边 / 1000。新内容先重排，不压缩阅读文字。当前文件尚未通过新内容迁移验证。

## Overview
Reference-derived graphic system — Build the relationships visible in the reconstructed work; never replace its composition with a generic Memphis motif kit. 原作者及具体字库不详；这里描述构成，不作作者归属。
World: 舞台 · 等轴文字建筑适用于共享同一构成关系的一组文化、活动或品牌物料。共同部分是图形语法、文字层级与色彩关系；每件新内容带来自己的标题长度、事实密度和主次。
Method: 先解出共享顶点的建筑，再在每个面的局部坐标内排字，最后统一投影；主标题是一座跨过积木的白桥。
Amplitude: 保持参考的强度；是否降强度由新用途另行决定，不默默改成极简。
Anti-reference: 以中性页面加一排彩色几何图形便称完成。

## Images
只用原生矢量几何、活字与计算的平面关系，不把参考截图当作成品贴入。原图只供私有对照。图形缩放保持比例；新画幅重组图形区域，文字单独重排。

## Layout
Grid system: Diagonal — 两组约 ±0.425 的斜率与竖直线构成投影坐标，所有立体面严格共享端点；版面从上方远处小体块到下方巨大标题桥逐层前进。
白桥是最清晰的连续阅读面；其他面可密集，但不能用前景屋顶切断白桥上的文字。
组内间隔约为正文行高的半倍，组间至少一个正文行高；拥挤先改区域尺寸，不降低事实字的级别。

## Typography
窄重无衬线用尽面宽，面内留约宽度 3% 的安全边。不同面按所在面作相同仿射变换，不能在变换后凭屏幕坐标摆字。
当前替代字库：Inter 400/700/900、Archivo variable、Noto Sans SC variable、Oswald 700；不是原字库确认结果。像素体系使用本轮制作的 Folio Pixel Study 替代。字体来源和授权见 ../../assets/fonts.json；已有 SVG 已内嵌字形，新内容必须重新补全所需字形，不能依赖本轮子集。

## Colors
paper `#FFFFF3`、ink `#000000`、yellow `#FFDF06`、blue `#2836B5`、red `#FF2E05`、green `#22B88A`。这些颜色是参考色关系的屏幕近似；色块可以邻接，但不能因同属一种风格就在不同系统之间交换整套配色。每个实际文字与底色组合记录在 Tokens 的 pairs 内。

## Shapes
只用平行四边形、矩形与字；深度只靠共边、遮挡与异色面。
有限的形状库先校正轮廓，再复用；不能以同一外接框尺寸冒充同一形。

## Forms
Cover / Statement：主标题或主物体先读；读字不能被图案压住。
Collection / Reference：相关事实按同一轴与相同级别排列，读者能找到日期、地点、名单或正文。
Sequence：同一语法延续，场形和信息密度随内容转折。
新格式：按上述结构重组；没有证据的图表、阅读长文与交互界面暂不从此文件推导。

## Variations
屋顶文字可以随深度缩放；白桥两侧的标题字号分别计算，但墨迹高度接近。

## Do's and Don'ts
不要用阴影制造体积；不要在字已经跑出面后只用裁切掩盖错误。
缩略图检验：先读主标题或主物体，再进入事实；移除配色，分区与层级仍成立。只复用可见关系，不把某件作品的逐格坐标写成通用规则。
复刻优先保留参考的颜色与小字；folio-check 对低对比配对的失败如实保留，不以改阈值消除。新原创输出应恢复可读性底线。
Caricature: 只保留颜色和几何，丢掉本文件的构图方法。

## Tokens

```yaml
colors:
  paper: "#FFFFF3"
  ink: "#000000"
  yellow: "#FFDF06"
  blue: "#2836B5"
  red: "#FF2E05"
  green: "#22B88A"
typography:
  display: { fontFamily: "Study Condensed, Study CJK, sans-serif", fontSize: 190, fontWeight: 700, lineHeight: 1 }
  body: { fontFamily: "Study Sans, Study CJK, sans-serif", fontSize: 24, fontWeight: 400, lineHeight: 1.4 }
spacing:
  within: 12
  between: 24
pairs:
  yellow-on-ink: { backgroundColor: "{colors.ink}", textColor: "{colors.yellow}" }
  yellow-on-blue: { backgroundColor: "{colors.blue}", textColor: "{colors.yellow}" }
  ink-on-paper: { backgroundColor: "{colors.paper}", textColor: "{colors.ink}" }
  paper-on-green-large: { backgroundColor: "{colors.green}", textColor: "{colors.paper}" }
```

## Record
Folio version: 1.1.0. Template version: 14. Date: 2026-11-04.
Pieces: [posters/09-konbin.svg](../../posters/09-konbin.svg)
Evidence: 已有同图复刻及原图对照；只有图形一致性的局部证据。未做第二份新内容、独立制作或盲评，不能称为已验证的生成系统。
