# 实际决定

- 采用 900 × 1200 竖幅，以 S=900、u=225、半模块 112.5 组织无沟槽拼合。上部由 337.5 宽的高独眼、225 宽的长触手、225 方形花瓣及 112.5 方形图案构成；没有采用等宽角色列。
- 纸白标题横穿 y=450–600，主活动 `TTXC 2027` 独占 lead：105.3 px / 900。中文与英文主题各用独立一行 secondary：86.4 px / 900。
- 红色阅读区置于右下。日期和中文场地用 facts 54 px / 900；英文场地用 27 px / 700；口号用 body 21.6 px / 400。说明按 `ART × SOUND ×` / `TECHNOLOGY` 两行排列，27 px / 700，完整字符串不变。
- 下方模块带置于左侧，宽 225，从 y=600 延续至底边；包含七软瓣小角色、八根粗放射条、六个实心三角切片。末端图案在画幅边界裁切。
- 大角色为三层圆瓣单眼，主体宽 270，眼径 124、瞳径 70；长触手角色采用六条独立波线、圆眼和无嘴面部。较小软瓣角色只用小圆眼与三点嘴；角色不对应活动分类。
- 只采用给定六色，无渐变、描边装饰、阴影、摄影或位图。全部文字保留为 `<text>` / `<tspan>`；形状保留为原生 SVG 圆、椭圆、路径和矩形。
- 使用提供的中性 helper 嵌入 Study Sans 400/700/900 与 Study CJK 可变字重的新内容字形子集；两份使用字体的 OFL 全文另存入 SVG metadata。

# 未覆盖处

- 文件未规定新作的准确模块坐标、角色姿态、主活动与主题的主次及场地译名的字号层级；上面的选择是本次排版决定。
- 没有原图，也未读取原图、前作、旧绘制代码、外部 DESIGN 链接或评审。不能判断复刻精度或声称独立评审通过。
- 仅自行用给定本地 Chrome / Playwright 渲染检查；没有验证其他 SVG 编辑器中的字体导入行为，也没有验证实体印刷结果。

# 完整读取清单

文本完整读取：

- `input-v3/DESIGN.md`
- `input-v3/brief.md`
- `input-v3/TECHNICAL.md`
- `input-v3/embed_fonts.py`
- `input-v3/fonts/Inter-OFL.txt`
- `input-v3/fonts/Noto-OFL.txt`

字体二进制读取（度量、子集或许可元数据验证）：

- `input-v3/fonts/Inter-400.ttf`
- `input-v3/fonts/Inter-700.ttf`
- `input-v3/fonts/Inter-900.ttf`
- `input-v3/fonts/NotoSansSC-variable.ttf`

目录仅列举 `input-v3/` 与 `input-v3/fonts/`，没有打开其中其他字体或授权文件。自行生成后读取 / 检查 `output-v3/raw.svg`、`output-v3/poster.svg`、`output-v3/preview.png`；没有读取其他案例、版本、规则或生产代码。
