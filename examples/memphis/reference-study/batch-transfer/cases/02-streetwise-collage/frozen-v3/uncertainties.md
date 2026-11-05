# 实际决定

- 按 900 px 短边将参考尺寸乘 0.9；基格为 150 px，中文主行 99 px / 900，轻行 93.6 px / 300，Latin 37.8 px，事实和说明 23.4 px。
- 五字副标题在三格宽的文字街区内换成“在城里／发现”，不缩窄字形；主标题与轻行按实际墨迹左边对齐。主阅读区因三行中文扩为 3×3 格。
- 第一文字区采用 paper，第二处采用 yellow；英文标题属于第一处，英文说明和参与事实合并在右下第二处。第二处保留较大的组间留白。
- 图案由 1 格、2 格及 3 格阅读街区交错组成；窗口中心距为 37.5 px，墨线为 6.75 px。斜条按垂直于条向测量为 18 px，周期 36 px。
- 文字位置以所提供字体在实际字重下的轮廓边界计算，没有水平压缩或字距拉伸。
- 每支箭头保留 90° 尖角、33 px 臂厚、105 px 高和直切端部。规则同时给出的 93 px 外宽与这些几何条件不能同时成立；采用由上述条件推出的约 75.83 px 外宽，未单独横向拉宽。
- 以原生矩形、线、圆、路径和活字制作；圆跨绿色／红色边界，顶部与底部使用分属相邻色区的切分曲面。字体用提供的中性 helper 内嵌，授权正文放在 SVG metadata 中。

# 未覆盖处

- 未提供各街区必须采用的具体位置；此版为新布局。
- 已检查 XML、七项固定文字、文字墨迹边界、字体内嵌及无栅格图像；未执行 Chrome 渲染或独立视觉评审。没有原图，未判断复刻精度，也未声称评审通过。

# 完整读取清单

输入内容：

- `input-v3/DESIGN.md`
- `input-v3/brief.md`
- `input-v3/TECHNICAL.md`
- `input-v3/embed_fonts.py`
- `input-v3/fonts/NotoSansSC-variable.ttf`
- `input-v3/fonts/Inter-400.ttf`
- `input-v3/fonts/Inter-700.ttf`
- `input-v3/fonts/Inter-900.ttf`
- `input-v3/fonts/Noto-OFL.txt`
- `input-v3/fonts/Inter-OFL.txt`

另仅列举过 `input-v3/fonts` 的文件名；未读取其余字体和授权文件内容。生成后自查读取了本人的 `output-v3/generate.py`、`output-v3/raw.svg` 与 `output-v3/poster.svg`。未读取 DESIGN 中的任何外部链接、其他目录、旧作、评审或生产脚本。
