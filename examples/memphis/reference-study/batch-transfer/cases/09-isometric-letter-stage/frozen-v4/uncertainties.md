# v4 制作记录

## 实际决定

- 使用 900 × 1200 原生 SVG；以整场黄色为背景，仅使用指定六色、原生四边形与可编辑文字。
- 统一世界投影为 `x = 440 + u − v`、`y = 730 + 0.425(u + v) − z`。各体块三面由同一组顶点生成，面内文字使用相同仿射投影。
- 将“白桥”解释为前景横跨两座异色支柱的连续双立面：左面读 `KONBIN`，右面读 `STAGE`。两面字体均为 126.5；对短词 STAGE 调整字距以充满其承载面。
- 以一座高窄塔、一座右侧宽台、一座前侧低台组成错位轮廓，而非同心叠层。高塔的两个立面分别将 `RINA VEIL`、`LAGO` 在局部平面内转向 90°，然后随立面投影。
- `17.07` 放在绿色高塔屋顶；`OPEN AIR` 放在黑色宽台屋顶；`WE MAKE / NOISE` 占据绿色标题桥屋顶的清晰区域。红色面均无字。
- `MOTIF / CLUB` 与 `NEON / PALMS` 按语义换行，原词不改。所有文字均采用 Study Condensed（Oswald）700，根据授权字体的字宽计算字号；没有文字轮廓化、栅格图片或裁切补救。
- 为两行姓名与屋顶口号添加完整短语的可访问标签；标签不额外印入画面。

## 未覆盖或仍需观察

- 输入未规定精确体块数量、坐标、各词字号、桥的支柱形式与姓名朝向；上述均为本次内容重排决定。
- 没有读取原图、前作或任何其他版本，因此不作原图精度、风格鉴定或独立审阅通过声明。
- 本轮没有运行浏览器渲染或截图。文字字形边界在各自未投影承载面内的数值检查，不能替代 Chrome 实际渲染、缩略图层级与视觉遮挡检查。

## 已完成自查

- `generate.py` 已实际运行，生成 `raw.svg`，并调用指定中性 helper 输出内嵌字体的 `poster.svg`。
- `poster.svg` 可由 Python XML 解析器解析；宽高为 900 × 1200，viewBox 为 `0 0 900 1200`。
- 逐一核对 12 个原生 text 节点，覆盖全部固定信息：KONBIN STAGE、17.07、OPEN AIR、WE MAKE NOISE、RINA VEIL、LAGO、MOTIF CLUB、NEON PALMS。
- 12 个文字节点均通过字体实际字形边界与局部承载面边界检查；没有 image、path 或 clipPath；共有 18 个原生 polygon。
- 输出含 Study Condensed 700 的内嵌 WOFF2 字体声明，没有外部字体 URL。

## 完整读取清单

以下路径均以本 case 目录为基准：

1. `input-v4/DESIGN.md`（全文）
2. `input-v4/brief.md`（全文）
3. `input-v4/TECHNICAL.md`（全文）
4. `input-v4/embed_fonts.py`（全文；执行用于字体内嵌）
5. `input-v4/fonts/`（仅列出目录项名称，未读取未用字体文件）
6. `input-v4/fonts/Oswald-700.ttf`（由 fontTools 读取字宽、字形边界及字体内嵌）
7. `output-v4/generate.py`（本人本次创建、随后读取并修正）
8. `output-v4/raw.svg`（本人生成；中性 helper 读取）
9. `output-v4/poster.svg`（本人生成；XML、固定文字与字体声明检查）
10. `output-v4/uncertainties.md`（本人本次创建）

未读取 case 中其他版本、其他目录、参考图、SKILL、旧作、其他生产脚本、评审或外链。
