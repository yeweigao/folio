# 技术活动 · 网格、窗口与积木

从本轮复刻反推的系统假设，不是制作前约束。数值只陈述关系，不抄写一张稿的坐标。

> Use alone: 先读 Overview，再按具体格式建立 Layout。S = 1000 指短边的参考尺度；数值乘实际短边 / 1000。新内容先重排，不压缩阅读文字。当前文件尚未通过新内容迁移验证。

## Overview
Reference-derived graphic system — Build the relationships visible in the reconstructed work; never replace its composition with a generic Memphis motif kit. 原作者及具体字库不详；这里描述构成，不作作者归属。
World: 技术活动 · 网格、窗口与积木适用于共享同一构成关系的一组文化、活动或品牌物料。共同部分是图形语法、文字层级与色彩关系；每件新内容带来自己的标题长度、事实密度和主次。
Method: 把界面窗口、远程副本和积木空间当成同一个活动的材料；在图纸网格上建立一件主物体，再把日期和城市作为附属面或附属窗口。
Amplitude: 保持参考的强度；是否降强度由新用途另行决定，不默默改成极简。
Anti-reference: 以中性页面加一排彩色几何图形便称完成。

## Images
只用原生矢量几何、活字与计算的平面关系，不把参考截图当作成品贴入。原图只供私有对照。图形缩放保持比例；新画幅重组图形区域，文字单独重排。

## Layout
Grid system: Hierarchical — 细网格间隔约 S/18，仅作共同坐标；一件主物体跨短边约 2/3，其他物体依照前后遮挡组织而不是平均分配。
用纯色物体隔开密网格；副本后退的每步约 S/100 到 S/45。主文字只落在最前层的完整面内。
组内间隔约为正文行高的半倍，组间至少一个正文行高；拥挤先改区域尺寸，不降低事实字的级别。

## Typography
窄而重的直立无衬线，展示字约 S/6 至 S/8，城市堆叠约 S/13，日期约 S/23；所有读字保持原字形比例，面上的文字跟随面作仿射变换。
当前替代字库：Inter 400/700/900、Archivo variable、Noto Sans SC variable、Oswald 700；不是原字库确认结果。像素体系使用本轮制作的 Folio Pixel Study 替代。字体来源和授权见 ../../assets/fonts.json；已有 SVG 已内嵌字形，新内容必须重新补全所需字形，不能依赖本轮子集。

## Colors
paper `#FFFFF2`、blue `#1900F5`、green `#00ECA9`、pink `#FA4EF5`、yellow `#FBFF08`、coral `#FF6977`、violet `#7C42FF`。这些颜色是参考色关系的屏幕近似；色块可以邻接，但不能因同属一种风格就在不同系统之间交换整套配色。每个实际文字与底色组合记录在 Tokens 的 pairs 内。

## Shapes
薄线窗口、连续的直角连接体、等轴立方体、圆柱、尖星与圆片；几何深度来自共享顶点和三种平面，不来自阴影。
有限的形状库先校正轮廓，再复用；不能以同一外接框尺寸冒充同一形。

## Forms
Cover / Statement：主标题或主物体先读；读字不能被图案压住。
Collection / Reference：相关事实按同一轴与相同级别排列，读者能找到日期、地点、名单或正文。
Sequence：同一语法延续，场形和信息密度随内容转折。
新格式：按上述结构重组；没有证据的图表、阅读长文与交互界面暂不从此文件推导。

## Variations
主角可以是窗口堆叠，也可以是一体的三维积木；两者共享网格、描边、字体和荧光配色。

## Do's and Don'ts
不要每张都套相同构图；不要让栈的前后关系切断标题；副本先画底和边，最后才画前景标签。
缩略图检验：先读主标题或主物体，再进入事实；移除配色，分区与层级仍成立。只复用可见关系，不把某件作品的逐格坐标写成通用规则。
复刻优先保留参考的颜色与小字；folio-check 对低对比配对的失败如实保留，不以改阈值消除。新原创输出应恢复可读性底线。
Caricature: 只保留颜色和几何，丢掉本文件的构图方法。

## Tokens

```yaml
colors:
  paper: "#FFFFF2"
  blue: "#1900F5"
  green: "#00ECA9"
  pink: "#FA4EF5"
  yellow: "#FBFF08"
  coral: "#FF6977"
  violet: "#7C42FF"
typography:
  display: { fontFamily: "Study Condensed, Study CJK, sans-serif", fontSize: 163, fontWeight: 700, lineHeight: 1 }
  body: { fontFamily: "Study Sans, Study CJK, sans-serif", fontSize: 24, fontWeight: 400, lineHeight: 1.4 }
spacing:
  within: 12
  between: 24
pairs:
  blue-on-paper: { backgroundColor: "{colors.paper}", textColor: "{colors.blue}" }
  paper-on-violet: { backgroundColor: "{colors.violet}", textColor: "{colors.paper}" }
```

## Record
Folio version: 1.1.0. Template version: 14. Date: 2026-11-04.
Pieces: [posters/05-hackathon-windows.svg](../../posters/05-hackathon-windows.svg)、[posters/08-hackathon-blocks.svg](../../posters/08-hackathon-blocks.svg)
Evidence: 已有同图复刻及原图对照；只有图形一致性的局部证据。未做第二份新内容、独立制作或盲评，不能称为已验证的生成系统。
