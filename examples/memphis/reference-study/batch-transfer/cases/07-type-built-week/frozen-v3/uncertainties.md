# 实际决定与未覆盖处

- 四条字墙依次为 TAIPEI、DESIGN、WEEK、2027；26 px 左右边距，前三行 178 px 字高，年份 205 px 字高，行间纸色间隙 12 px。展示活字按实际字形宽度横向定制；事实活字不缩放。
- DESIGN 的 E 取消竖笔，以三条独立等宽矩形重建；G 的整字位由蓝色圆环、纸色开口和黑色横画构成。年份 0 使用直径 205 px 的 orange-glyph 实色圆盘。圆形没有非等比缩放。
- 事实区完整重写 TAIPEI DESIGN WEEK 2027，确保图形化字位之外有完整可读名称；类别左对齐成五行，日期与机构在右列。HOST 与 PARTNER 是为表示简报中的机构角色添加的标签。
- 网站安排在黑色底带中，使用未压缩的 54 px 活字。底带属于事实区，不添加字墙外的几何装饰。
- 仅使用所给 Inter 400、700、900，以 Study Sans 名称内嵌；其完整 OFL 许可置于 SVG metadata。原生矩形、圆与活字均保留编辑能力。
- DESIGN 未规定每行具体断法、几何字位、页边距、事实分栏或网站底带，以上为本次制作决定。
- 未读取原图、旧作品、评审或其他绘制代码；不主张复刻精度或独立评审通过。

# 完整读取清单

- input-v3/DESIGN.md
- input-v3/brief.md
- input-v3/TECHNICAL.md
- input-v3/embed_fonts.py
- input-v3/fonts/Inter-400.ttf（字体度量；中性 helper 为内嵌读取）
- input-v3/fonts/Inter-700.ttf（字体度量；中性 helper 为内嵌读取）
- input-v3/fonts/Inter-900.ttf（字体度量、字形边界；中性 helper 为内嵌读取）
- input-v3/fonts/Inter-OFL.txt
- 自己生成的 output-v3/generate.py、raw.svg、poster.svg。

只枚举了 input-v3/fonts 的文件名；没有打开该目录中的其他字体或许可文件。未打开 DESIGN 中链接的外部文件。
