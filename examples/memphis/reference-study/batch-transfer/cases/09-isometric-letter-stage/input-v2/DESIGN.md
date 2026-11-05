# Isometric letter stage · Type as architecture

以下为新作品的施工规则；尺寸描述相对关系，活动内容另放简报。

> Use alone: 先读 Overview 和 Images，再按具体格式建立 Layout。S = 1000 指短边的参考尺度；数值乘实际短边 / 1000。由面宽推导的展示字尺寸单独计算。新内容先重排，不压缩阅读文字。

## Overview
Reference-derived graphic system — Build shared-edge isometric architecture and project type within its faces; never place detached text beside decorative cubes.
World: 本系统适用于以文字建筑为主体的一组文化、活动或品牌物料。共同部分是投影语法、文字层级与色彩关系；每件新内容带来自己的标题长度、事实密度和主次。
Method: 先解出共享顶点的建筑，再在每个面的局部坐标内排字，最后统一投影；主标题是一座跨过积木的白桥。
Amplitude: 保持实心建筑占据主体、文字撑满承载面的强度；是否降强度由新用途另行决定。
Anti-reference: 以中性页面加一排彩色几何图形便称完成。

## Images
只用原生矢量几何、活字与计算的投影关系，不需要外部图像。新画幅重组体块与文字面，再统一投影；不拉伸已经投影的成品。

## Layout
Grid system: Diagonal — 两组约 ±0.425 的斜率与竖直线构成投影坐标，所有立体面严格共享端点；版面从上方远处小体块到下方巨大标题桥逐层前进。
白桥是最清晰的连续阅读面；其他面可密集，但不能用前景屋顶切断白桥上的文字。
组内间隔约为正文行高的半倍，组间至少一个正文行高；拥挤先改区域尺寸，不降低事实字的级别。

## Typography
窄重无衬线用尽面宽，面内留约宽度 3% 的安全边。不同面按所在面作相同仿射变换，不能在变换后凭屏幕坐标摆字。
投影面内文字用 Study Condensed（Oswald）700；中文用 Study CJK（Noto Sans SC）700。独立于建筑面的阅读说明用 Study Sans（Inter）400，不作横向压缩。面内字号按面宽、行数与字数计算；Tokens 的 display 只规定字族、字重和行距。它们是已授权的替代字库，并非原字体鉴定；来源与 SIL OFL 1.1 授权见 [fonts.json](../../assets/fonts.json)。新内容必须补全所需字形，不能依赖已有 SVG 的子集。

## Colors
yellow `#FFDF06` 可作整场底色，并在 ink `#000000` 或 blue `#2836B5` 面上承载文字；paper `#FFFFF3` 是连续主标题桥的亮面，配 ink 字。green `#22B88A` 用于顶面或侧面，承载文字时用 ink；red `#FF2E05` 只作无字顶面、侧面或支柱。ink 也可作承重面与顶面。以这些异色面分离建筑，不必固定每个体块的位置或数量。每个文字组合列在 pairs：阅读文字至少 4.5:1，大字至少 3:1。

## Shapes
只用平行四边形、矩形与字；深度只靠共边、遮挡与异色面。
以字形或承载面的比例构造几何件，组合位置由新内容决定。

## Forms
Cover / Statement：主标题或主物体先读；读字不能被图案压住。
Collection / Reference：相关事实按同一轴与相同级别排列，读者能找到日期、地点、名单或正文。
Sequence：同一语法延续，场形和信息密度随内容转折。
新格式：按上述结构重组；没有证据的图表、阅读长文与交互界面暂不从此文件推导。

## Variations
屋顶文字可以随深度缩放；白桥两侧的标题字号分别计算，但墨迹高度接近。

## Do's and Don'ts
不要用阴影制造体积；不要在字已经跑出面后只用裁切掩盖错误。
缩略图检验：先读主标题或主物体，再进入事实；移除配色，分区与层级仍成立。不把某件作品的逐格坐标写成通用规则。
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
  display: { fontFamily: "Study Condensed, Study CJK, sans-serif", fontWeight: 700, lineHeight: 1 }
  body: { fontFamily: "Study Sans, Study CJK, sans-serif", fontSize: 24, fontWeight: 400, lineHeight: 1.4 }
spacing:
  within: 12
  between: 24
pairs:
  yellow-on-ink: { backgroundColor: "{colors.ink}", textColor: "{colors.yellow}" }
  yellow-on-blue: { backgroundColor: "{colors.blue}", textColor: "{colors.yellow}" }
  ink-on-paper: { backgroundColor: "{colors.paper}", textColor: "{colors.ink}" }
  ink-on-green: { backgroundColor: "{colors.green}", textColor: "{colors.ink}" }
```

## Record
Folio version: 1.1.0. Template version: 14. Date: 2026-11-05.
Pieces: [posters/09-konbin.svg](../../posters/09-konbin.svg)
Evidence: 一份新内容迁移样本 [v1](../../batch-transfer/cases/09-isometric-letter-stage/frozen-v1/poster.png) 在 [identity](../../batch-transfer/evaluation/identity-v1.json)、[structure](../../batch-transfer/evaluation/structure-v1.json)、[craft](../../batch-transfer/evaluation/craft-v1.json) 三项评估中均通过；这是一份样本的证据，不代表更广泛的生成能力已验证。v1 实际使用黑字绿底，未使用原声明的白字绿底。
Changes: 清理依赖未提供参考图的表述，明确字体角色与面内字号算法；以实际使用的 ink-on-green 替换未达对比度底线的 paper-on-green-large。修订文件尚待新的迁移测试。
