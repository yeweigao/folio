# 街头行动 · 不等跨模块拼贴

用满幅街区拼贴、粗尺度图案与同量级轻重中文组织公共文化活动信息。

> Use alone: 先读 Overview、Typography 与 Shapes，再建立 Layout。S = 1000 是短边参考尺度；尺寸乘实际短边 / 1000，由模块计算的值不再缩放。内容增加时合并街区或换行，不压缩字宽、不把大格纹理细化。

## Overview
Memphis-derived street graphics, unequal modular collage — Build neighboring districts of solid text and coarse graphic rhythm; never turn the full field into a fine decorative texture. 原作者不详，不作个人归属。
World: 用于城市行动、街区文化与公共活动海报。每件保留无沟槽的不等跨距街区、两处文字停留点，以及同量级中文轻重对照；活动内容决定文字区交错方式、图案方向和模块组合。
Method: 把信息分成辨认活动与查找参与事实两组，分别合并成整色街区。让箭头、圆和斜纹引导视线在两处停留点间移动；以粗线窗口格和宽条纹调节节奏，而不是填满空白。
Amplitude: 图案保持砖级粗尺度，文字区保持大字；安静内容扩大整色街区，不缩小图案单元。
Anti-reference: 等大的彩色棋盘、密细网格，以及浅底上后贴的标题卡片。

## Images
只用原生矢量图形和活字，不用照片、截图、噪点或立体纹理。图案覆盖所属街区并在区边裁切，圆可跨一条街区边界；不压文字。等比缩放圆、菱形、箭头与凹四角星，换画幅时重组街区，不拉伸单个形状。

## Layout
Grid system: Modular — 短边分六格，基格 u = S/6；长边续排同一格距，端部余量并入接边街区。允许半格与两格合并，让横条、方格和双高块交错。
边到边铺满，无外边距、阴影或圆角卡片。主文字区以 3×2 基格为起点，参与事实区以 3×1 基格为起点，随文字长度合并相邻整格；不锁定两区的位置。paper 留白也是街区，不能成为页面的剩余空地。
文字可见墨迹距区边至少 26，组内净距 12，主副文字组净距至少 24。图案在街区边终止，文字不得贴到线纹上。主文字区容纳同量级中文轻／重两行；若放不下，扩区并重排周围图块。
横幅把更多街区沿长边接续，竖幅沿长轴交错图与字，方幅保留两处文字停留点；均保留 1格、2格及半格跨距变化，不把整幅重划为同大窗口。

## Typography
Study Sans 映射 Inter 400/700/900，供正常宽度 Latin；Study CJK 映射 Noto Sans SC variable，供中文 300/400/700/900。均为 SIL OFL 1.1；来源与授权见 ../../assets/fonts.json。新内容重新嵌入全部所需字形。
主标题中文用 Study CJK 900、字号 110；成对中文轻行用同字体 300、字号 104，字身高度保持主行的 0.90–1.05，行高均为 1.05。轻行是同量级第二声部，不能缩成小粗副标题。两行对齐实际墨迹边，行间净距为 0.10–0.18 个主字高。
Latin 活动名用 Study Sans 900、字号 42；Latin 说明或译文用 Study Sans 400、字号 42，行高 1.15。保留正常字宽，不用窄体、水平压缩或强制字距填满中文行；Latin 是次级标识，不取代中文轻行。只有 Latin 时，以 110／900 与 104／400 形成同级轻重组，仍用正常字宽。
事实文字 26／700，解释文字 26／400、行高 1.35；这是最小阅读级。数字沿用所属角色正常宽度字体。长标题扩区或换行，事实不为装饰让位。

## Colors
paper `#EAE8E6` 承担主要阅读街区及圆、凹星等浅形；ink `#19191D` 承担文字、网格、条纹与剪影。yellow `#FFDE00` 可承担第二阅读街区，pink `#F68CBC` 可承担浅色副阅读区；三个浅场均用 ink 阅读。
blue `#008BCD`、green `#087C4A`、red `#F52B20`、purple `#76258D` 是相接的图形街区；pink 与 yellow 同时参与图案前景。相邻区以大色面区分，黑白条纹和黑色窗口格提供最强明暗节拍。深色图案区不接管小字阅读。
阅读文字只用 ink-on-paper／yellow／pink，不在条纹与网格上放字。所有实际阅读配对至少 4.5:1，大字至少 3:1；图案颜色不能自动成为文字颜色。

## Shapes
所有图形无阴影。尺寸以基格 u 为单位；跨格区沿用同一尺度，不能按容器尺寸重新计算纹理密度。
- 窗口格：一个 u 中划 4×4 窗口，线中心距 0.25u、墨线宽 0.045u，外边用同样粗线；浅窗宽约 0.205u。跨两格时增加到八列，不把四列缩细或改成十余列。用 ink 画线、paper 作窗底。
- 黑白竖条：每条宽 0.10u，两色一周期 0.20u；横条可旋转 90°。斜条为 45°，按垂直条向量测量宽 0.12u、周期 0.24u，区边直接截断。彩色斜条沿用同宽度级，不变成细线填充。
- 双箭头：每个箭头以两个厚 0.22u 的斜臂在 90° 尖角接合，外高 0.70u、外宽 0.62u；同条带等距重复两到三个，指向一致。箭尾直切，不加箭杆或圆角。
- 菱形与圆：菱形由正方形旋转 45°，对角跨度 0.90–1.00u；圆直径取 u 或 2u，跨界圆保持整圆轮廓。两者为单个实心大块，无描边或高光。
- 凹四角星：在边长 u 的正方形四角各减去半径 0.50u 的四分之一圆，留下四尖朝边中点、四弧向内收的负形；不画成外凸花瓣。
- 半圆与圆环：半圆直径 u 或 2u，沿直径平切；圆环外径 u、环宽 0.18u。它们与条纹、窗口格同为砖级尺度，不当小图标使用。
相邻街区交替实心大形与粗重复图案；不要连排两个同方向同图案区，不加入花瓣、齿轮或任意星形扩充图形库。

## Forms
Cover / Statement：主街区承担同量级中文轻重组，图案把视线送回标题；不让 Latin 窄体成为另一主角。
Collection / Reference：事实合并进第二整色街区，同级同轴；图案独立相接，不把事实散入纹理缝隙。
Sequence：箭头或斜条随内容推进，每段保留两个文字停留点；不复制某张海报的图块位置。
Comparison：同类信息置于等跨距整色街区、直接标注差别；不靠颜色暗示排名。

## Variations
允许图案区旋转 90°、条纹改向、圆跨一条边，以及主副文字区交换方位。窗口格和条纹格距不随区面积改变；文字区扩大后减少相邻图案区数量，不能加密全部图案来补面积。

## Do's and Don'ts
缩略图应看见不同大小街区和两处文字停留点；灰度中粗窗口格与宽条纹仍是块级节拍。中文轻行与重行同量级，正常宽度 Latin 保持次级。检查文字完整，边缘图形出血不裁事实。
Caricature: 用细网纹理填满彩色矩形，配一行极黑中文和一行抢眼窄英文。

## Tokens

```yaml
colors:
  paper: "#EAE8E6"
  ink: "#19191D"
  blue: "#008BCD"
  green: "#087C4A"
  pink: "#F68CBC"
  yellow: "#FFDE00"
  red: "#F52B20"
  purple: "#76258D"
typography:
  display-cjk-heavy: { fontFamily: "Study CJK, sans-serif", fontSize: 110, fontWeight: 900, lineHeight: 1.05 }
  display-cjk-light: { fontFamily: "Study CJK, sans-serif", fontSize: 104, fontWeight: 300, lineHeight: 1.05 }
  display-latin-heavy: { fontFamily: "Study Sans, sans-serif", fontSize: 110, fontWeight: 900, lineHeight: 1.05 }
  display-latin-light: { fontFamily: "Study Sans, sans-serif", fontSize: 104, fontWeight: 400, lineHeight: 1.05 }
  latin-label: { fontFamily: "Study Sans, sans-serif", fontSize: 42, fontWeight: 900, lineHeight: 1.15 }
  latin-explanation: { fontFamily: "Study Sans, sans-serif", fontSize: 42, fontWeight: 400, lineHeight: 1.15 }
  facts: { fontFamily: "Study Sans, Study CJK, sans-serif", fontSize: 26, fontWeight: 700, lineHeight: 1.35 }
  body: { fontFamily: "Study Sans, Study CJK, sans-serif", fontSize: 26, fontWeight: 400, lineHeight: 1.35 }
spacing:
  within: 12
  between: 24
  reading-inset: 26
pairs:
  ink-on-paper: { backgroundColor: "{colors.paper}", textColor: "{colors.ink}" }
  ink-on-yellow: { backgroundColor: "{colors.yellow}", textColor: "{colors.ink}" }
  ink-on-pink: { backgroundColor: "{colors.pink}", textColor: "{colors.ink}" }
```

## Record
Folio version: 1.1.0. Template version: 14. Date: 2026-11-05.
Pieces: [posters/01-collection-of-acts.svg](../../posters/01-collection-of-acts.svg)。
Baseline: batch-transfer/evaluation/identity-v1.json = 部分通过；structure-v1.json = 通过；craft-v1.json = 通过。已查看 v1 彩色与灰度对照和 cases/02-streetwise-collage/frozen-v1/poster.png；基线保留不等跨距街区与两处文字场，但窗口格过密，中文轻重同级与普通宽度英文关系丢失。
Revision: 保留已成立的模块组织与位置自由，补齐粗格距、条纹尺度与双语字体角色，指定阅读底色配对。修订尚待新内容独立生成与重新评估；不把基线结构和工艺结论扩展为修订版通过。
Static verification: 已运行 scripts/folio-check.py，本文件 schema 与声明配对对比度通过；阅读配对最低 7.84:1。未生成或验证修订版作品。
