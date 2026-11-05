# 实际决定

- 使用 900 × 1200，左绿右黑、450 : 450 连续双场。主要字块宽 405；C / O 高 492，E / X 高 520。文字与间距按短边 / 1000 = 0.9 换算。
- 从 COEXIST 提取 C / O / E / X 四个路径构字。C 与 E 共用外半径 202.5、内半径 100.5 和约 102 的笔厚；O 的橙色下碗承担整段主笔；最后一块把 X 抽象成相向曲叉及容纳英文展名的宽断口。
- C 的横向开口承接开始日期、结束日期、时间；O 的纵向深腔承接署名、地点；E 的两个开口分别承接「共生」「设计展」；X 的断口把英文展名按三个语义单词换行。固定事实由可编辑活字写全。
- 标题中文用 Study CJK 900、68.4；英文用 Study Sans 900、53.1；日期时间用 Study Sans 700、43.2；署名地点用 Study CJK 400、21.6。中文标题黄色用于大字，绿色场小字为黑色，黑色场活字为白色。
- 三个四分之一圆弧齿连接 C 的切边；三个纸白圆节点沿 O 的下碗排列。未使用可选外框，也未添加未提供的事实。
- 所有构字为平填原生路径，固定事实保留 text；字体由提供的中性 helper 子集内嵌，原字体授权全文保留于 SVG metadata。
- 自查发现「设计展」左部靠近 E 下开口的圆弧，将该行 x 从 154 移至 192；其余构图保留。

# 未覆盖处与验证边界

- DESIGN 没有指定从主题抽取中文还是英文、字块读序及具体切口坐标；以上为本次自行决定。X 的宽断笔与相向弧叉是抽象构字，完整主题读法由中英文展名确认。
- 已运行生成脚本，检查 raw.svg / poster.svg 均能解析，尺寸为 900 × 1200，并逐组断言全部固定信息完整。未将文字转轮廓。
- 使用提供的本机 Chrome / Playwright、仅 file:// 页面渲染了自己的 poster.svg，确认使用到的 Study Sans 700 / 900 与 Study CJK 内嵌字体已加载，并查看了 900 × 1200 预览。沙箱内首次启动 SIGABRT；经同一本地命令沙箱外执行后渲染成功。最终仅移动「设计展」一行后重新生成，最终预览随后重新渲染。
- 没有原图；未读取或比较前作、旧版本、评审、外部参考或全局 Folio 规则；不宣称复刻精度、识别效果或独立评审通过。

# 完整读取清单

输入文件（完整读取）：

- input-v3/DESIGN.md
- input-v3/brief.md
- input-v3/TECHNICAL.md
- input-v3/embed_fonts.py
- input-v3/fonts/Inter-OFL.txt
- input-v3/fonts/Noto-OFL.txt

字体二进制（测量或 helper 实际打开）：

- input-v3/fonts/Inter-400.ttf（helper）
- input-v3/fonts/Inter-700.ttf（测量与 helper）
- input-v3/fonts/Inter-900.ttf（测量与 helper）
- input-v3/fonts/NotoSansSC-variable.ttf（测量与 helper）

自生成文件（自查或重生成时读取）：

- output-v3/generate.py
- output-v3/raw.svg
- output-v3/poster.svg
- output-v3/preview.png

运行支持为 TECHNICAL.md 指定的 Python、Pillow / fontTools、Node、Playwright、Chrome；未读取其他生产绘图脚本或其他目录的设计资料。
