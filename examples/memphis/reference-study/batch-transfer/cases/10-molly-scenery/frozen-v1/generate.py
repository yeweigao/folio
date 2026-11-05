from pathlib import Path
from io import BytesIO
from base64 import b64encode
from math import cos, sin, pi
from html import escape

from fontTools.ttLib import TTFont
from fontTools import subset
from fontTools.varLib.instancer import instantiateVariableFont


HERE = Path(__file__).resolve().parent
FONTS = HERE.parent / "input" / "fonts"

TITLE = ["艺术在场", "日常发光"]
ENGLISH = ["ART IN", "EVERYDAY", "LIFE"]
DATE = "2027.04.17—05.05"
TIME = "10:00–20:00"
LOCATION = "城市艺术中心 · 一层展厅"
ENTRY = "免费入场"
DESCRIPTION = "把街角的颜色、声音与相遇，变成每个人都能参与的艺术现场。"


def embedded_font(filename, characters, weight=None):
    font = TTFont(FONTS / filename)
    required = set(characters)
    missing = required - {chr(c) for c in font.getBestCmap()}
    if missing:
        raise ValueError(f"Missing glyphs in {filename}: {missing}")
    if weight is not None and "fvar" in font:
        font = instantiateVariableFont(font, {"wght": weight}, inplace=False)
    options = subset.Options()
    options.recalc_bounds = True
    options.recalc_timestamp = False
    options.layout_features = ["*"]
    subsetter = subset.Subsetter(options=options)
    subsetter.populate(text="".join(sorted(required)))
    subsetter.subset(font)
    font.flavor = "woff2"
    output = BytesIO()
    font.save(output)
    return b64encode(output.getvalue()).decode("ascii")


pixel = embedded_font("FolioPixelStudy.woff2", "".join(TITLE + ENGLISH))
sans = embedded_font("NotoSansSC-variable.ttf", LOCATION + ENTRY + DESCRIPTION, 400)
numerals = embedded_font("Inter-700.ttf", DATE + TIME)
brand = embedded_font("Inter-900.ttf", "MOLLY")

svg = [f'''<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1528" viewBox="0 0 1080 1528" role="img" aria-labelledby="poster-title poster-description">
<title id="poster-title">MOLLY · 艺术在场 · 日常发光</title>
<desc id="poster-description">{escape(DATE)}，{escape(TIME)}。{escape(LOCATION)}。{ENTRY}。{DESCRIPTION}</desc>
<defs>
<style>
@font-face{{font-family:'Poster Pixel';src:url(data:font/woff2;base64,{pixel}) format('woff2');font-weight:400;font-style:normal;}}
@font-face{{font-family:'Poster Sans';src:url(data:font/woff2;base64,{sans}) format('woff2');font-weight:400;font-style:normal;}}
@font-face{{font-family:'Poster Numerals';src:url(data:font/woff2;base64,{numerals}) format('woff2');font-weight:700;font-style:normal;}}
@font-face{{font-family:'Poster Brand';src:url(data:font/woff2;base64,{brand}) format('woff2');font-weight:900;font-style:normal;}}
text{{font-synthesis:none;}}
.pixel{{font-family:'Poster Pixel';font-weight:400;}}
.body{{font-family:'Poster Sans';font-weight:400;}}
.numeric{{font-family:'Poster Numerals';font-weight:700;font-variant-numeric:tabular-nums;}}
</style>
</defs>
<rect width="1080" height="1528" fill="#FFFFFF"/>

<!-- Two large, unequal-height landscape modules. -->
<g aria-hidden="true">
  <rect x="540" y="0" width="540" height="620" fill="#276DB3"/>
  <path d="M0 748V478A270 270 0 0 1 540 478V748Z" fill="#276DB3"/>
  <path d="M54 748V478A216 216 0 0 1 486 478V748Z" fill="#F04D1B"/>
  <path d="M108 748V478A162 162 0 0 1 432 478V748Z" fill="#CAE5F4"/>
  <path d="M162 748V478A108 108 0 0 1 378 478V748Z" fill="#276DB3"/>
  <path d="M216 748V478A54 54 0 0 1 324 478V748Z" fill="#FFFFFF"/>

  <g fill="#F6C333">
    <circle cx="810" cy="192" r="124"/>
    <circle cx="928" cy="310" r="124"/>
    <circle cx="810" cy="428" r="124"/>
    <circle cx="692" cy="310" r="124"/>
  </g>
  <path d="M540 620H810A135 135 0 0 1 540 620Z M810 620H1080A135 135 0 0 1 810 620Z" fill="#EDC6C0"/>
</g>

<!-- The small six-petal flower and wordmark share the open upper margin. -->
<g aria-hidden="true" fill="#FF3235">''']

for i in range(6):
    angle = i * pi / 3
    svg.append(f'<circle cx="{434 + 35 * cos(angle):.4f}" cy="{102 + 35 * sin(angle):.4f}" r="29"/>')

svg.append('''</g>
<circle cx="434" cy="102" r="17" fill="#080808" aria-hidden="true"/>
<text x="60" y="123" font-family="Poster Brand" font-weight="900" font-size="66" letter-spacing="-1.8" fill="#080808">MOLLY</text>

<!-- Editable display type. -->
<g class="pixel" fill="#080808" font-size="166">
  <text x="60" y="940">艺术在场</text>
  <text x="60" y="1106">日常发光</text>
</g>
<g class="pixel" fill="#276DB3" font-size="49">
  <text x="739" y="842">ART IN</text>
  <text x="739" y="903">EVERYDAY</text>
  <text x="739" y="964">LIFE</text>
</g>
<g aria-hidden="true" fill="none" stroke="#276DB3" stroke-width="8">''')

for y in [1030, 1090]:
    for x in [765, 855, 945]:
        svg.append(f'<circle cx="{x}" cy="{y}" r="21"/>')

svg.append(f'''</g>

<!-- Event facts retain a common reading axis and ordinary sans serif. -->
<g fill="#080808">
  <text class="numeric" x="60" y="1238" font-size="53">{escape(DATE)}</text>
  <text class="numeric" x="1020" y="1238" font-size="31" text-anchor="end">{escape(TIME)}</text>
  <text class="body" x="60" y="1318" font-size="31">{LOCATION}</text>
</g>
<rect x="820" y="1279" width="200" height="54" fill="#276DB3"/>
<text class="body" x="920" y="1317" font-size="28" text-anchor="middle" fill="#FFFFFF">{ENTRY}</text>
<text class="body" x="60" y="1433" font-size="28" fill="#080808">{DESCRIPTION}</text>
</svg>
''')

(HERE / "poster.svg").write_text("\n".join(svg), encoding="utf-8")
print(HERE / "poster.svg")
