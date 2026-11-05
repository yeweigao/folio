# 中性制作支持

embed_fonts.py 只把提供的字体子集内嵌，不含图形或布局。SVG 中用 Study Sans（400/700/900）、Study Light（100–900）、Study CJK（100–900）、Study Condensed（700）；均来自 DESIGN.md 列出的字库。

运行：`/private/tmp/folio-memphis-tools/bin/python input-v5/embed_fonts.py input-v5/fonts output-v5/raw.svg output-v5/poster.svg`。

Python 已有 fontTools、brotli、Pillow。渲染可用 Node /opt/homebrew/bin/node，Playwright /Users/vicoye/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright，Chrome /Applications/Google Chrome.app/Contents/MacOS/Google Chrome。通用工具不提供美学判断。
