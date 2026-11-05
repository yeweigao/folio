# Memphis reference reconstruction study

按用户给出的三张参考，先复刻成品，再反推规则。

## 查看

- [完整图库](index.html)：28 件独立 SVG，可点开，字体已内嵌，文字与图形可编辑。
- [第一组：8 页版式](previews/01-slides.png) · [原图对照](previews/01-slides-comparison.png)
- [第二组：9 张海报](previews/02-posters.png) · [原图对照](previews/02-posters-comparison.png)
- [第三组：11 件视觉物料](previews/03-brand.png) · [原图对照](previews/03-brand-comparison.png)
- [已实施的 skill 修改](SKILL-ITERATION.md)
- [实际渲染与校验记录](VERIFICATION.md)
- [十套独立迁移与修订结果](batch-transfer/RESULTS.md) · [原组 / 基线 / 修订版图库](batch-transfer/index.html)
- [第十套首次失败记录](transfer-test/RESULT.md)

## 反推的 10 套系统

| 复刻范围 | DESIGN.md |
|---|---|
| 第一张的整套报告 | [方砖报告](systems/01-report-tiles/DESIGN.md) |
| 第二张左上 | [不等跨拼贴](systems/02-streetwise-collage/DESIGN.md) |
| 第二张中上 | [切割字形](systems/03-cut-glyph-exhibition/DESIGN.md) |
| 第二张右上 | [黑框曲面分区](systems/04-club-partitions/DESIGN.md) |
| 第二张左中 | [角色拼贴](systems/05-culture-monsters/DESIGN.md) |
| 第二张两张 Hackathon | [网格、窗口与积木](systems/06-hackathon-space/DESIGN.md) |
| 第二张右中 | [字母即版面](systems/07-type-built-week/DESIGN.md) |
| 第二张左下 | [角色与棋盘](systems/08-forest-character/DESIGN.md) |
| 第二张右下 | [等轴文字建筑](systems/09-isometric-letter-stage/DESIGN.md) |
| 第三张整套身份 | [模块景观身份](systems/10-molly-scenery/DESIGN.md) |

每套旁边的 brief.md 保存本次内容；DESIGN.md 保存结构关系。十套均已独立生成过新内容，并在修订规则后交给全新上下文复测。原输入与失败结果保留；逐例结论和限制见批量结果，不能由单个样本推断普遍可靠。

## 制作与素材

引用图是用户提供的 `/Users/vicoye/Downloads/IMG_8102.JPG`、`IMG_8103.JPG`、`IMG_8104.JPG`。交付图形全部重画，没有把原图像素贴入 SVG；不复刻截图水印、灰背景以外的社交界面或阴影。原作者未确认，本项目不声称原创设计或原作归属。用于参考复刻与 skill 调试。

字体使用有 OFL 授权的替代品，见 assets/fonts.json 与相应授权文件。像素英文字由格点构造，中文字从 Noto Sans CJK 重构为像素替代字形，名为 Folio Pixel Study；它不是参考原字体，沿用 OFL 授权。原字体、微小文案与部分形状仍有差异，对照图可直接检视。

独立 SVG 和图库不依赖系统字体或联网。文字子集仅覆盖当前作品；新增内容需重新补字。

## 复现

`build.py` 只生成作品；`extract_systems.py` 是最初草稿的历史生成器，两者互不调用。默认保留已修订 DESIGN；`--overwrite-original-drafts` 才会覆盖为未经迁移修正的初稿。

```sh
python3 build.py
python3 prepare_fonts.py
python3 embed_fonts.py
node render.cjs
python3 make_boards.py
# 看完实际成品之后，再反推系统：
python3 extract_systems.py
```

字体处理需要 fonttools、brotli、Pillow；拼图需要 Pillow；渲染需要 Playwright 与 Chrome。当前脚本中的字体、浏览器及参考路径对应本机环境，换机器时需更新。已导出的作品文件无需这些工具即可查看。
