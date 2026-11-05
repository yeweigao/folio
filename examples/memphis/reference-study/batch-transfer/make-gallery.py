#!/usr/bin/env python3
"""Build the offline evidence gallery from selected, frozen outputs."""
from pathlib import Path
from html import escape
import json

ROOT = Path(__file__).resolve().parent


def main():
    cases = json.loads((ROOT / 'cases.json').read_text())
    stages = json.loads((ROOT / 'evaluation/final-case-stages.json').read_text())
    sections = []
    for case in cases:
        ident = case['id']
        stage = stages[ident]
        final = f'cases/{ident}/frozen-{stage}'
        assert (ROOT / final / 'poster.png').is_file(), ident
        source = 'IMG_8102.JPG' if ident.startswith('01') else 'IMG_8104.JPG' if ident.startswith('10') else 'IMG_8103.JPG'
        panels = []
        for label, src in [
            ('复刻参照', f'evaluation/blind/{ident}/reference.png'),
            ('首轮生成 · v1', f'cases/{ident}/frozen-v1/poster.png'),
            (f'修订生成 · {stage}', f'{final}/poster.png'),
        ]:
            assert (ROOT / src).is_file(), src
            panels.append(f'<figure><figcaption>{label}</figcaption><a href="{src}" target="_blank"><img src="{src}" loading="lazy" alt="{escape(ident)} {label}"></a></figure>')
        history = []
        for version in ['v2', 'v3', 'v4', 'v5']:
            p = f'cases/{ident}/frozen-{version}/poster.png'
            if version != stage and (ROOT / p).exists():
                history.append(f'<figure><figcaption>{version}</figcaption><a href="{p}" target="_blank"><img src="{p}" loading="lazy" alt="{ident} {version}"></a></figure>')
        sections.append(f'''<section id="{ident}"><h2>{ident[:2]} / {escape(case['title'])}</h2>
<p class="links"><a href="../systems/{ident}/DESIGN.md">DESIGN.md</a> · <a href="{final}/poster.svg">可编辑 SVG</a> · <a href="{final}/generate.py">制作源代码</a> · <a href="evaluation/final-review/{source}" target="_blank">用户原图</a></p>
<div class="panels">{''.join(panels)}</div>
<details><summary>查看中间轮次与制作边界</summary><p><a href="{final}/uncertainties.md">制作者决定与读取清单</a> · <a href="cases/{ident}/input-{stage}/brief.md">冻结新简报</a></p><div class="history">{''.join(history) or '<p>没有额外中间轮次。</p>'}</div></details></section>''')
    page = '''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>十个世界 · 迁移验证</title>
<style>*{box-sizing:border-box}body{margin:0;background:#e9e9e9;color:#171717;font:16px/1.6 Arial,sans-serif}header,main,footer{max-width:2000px;margin:auto;padding:28px}header{padding-top:48px}h1{font-size:36px;line-height:1.2;margin:0 0 18px}h2{margin:0;font-size:25px}p{max-width:1000px}a{color:#1745a3;text-underline-offset:3px}.links{font-size:14px}.panels{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}figure{margin:0;background:#d7d7d7}figcaption{padding:10px 14px;font-size:14px}img{display:block;width:100%;height:650px;object-fit:contain}section{padding:28px 0;border-top:1px solid #aaa;margin-bottom:35px}details{margin-top:18px}summary{cursor:pointer}.history{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}.history img{height:500px}footer{font-size:14px;border-top:1px solid #aaa}@media(max-width:900px){.panels,.history{grid-template-columns:1fr}img,.history img{height:auto;max-height:900px}header,main,footer{padding:20px}h1{font-size:29px}}</style>
<header><h1>十个世界 · 迁移验证</h1><p>每套独立制作：冻结 DESIGN.md、同一份新简报、授权字体。首轮与失败稿保留，修订后由新的制作者重做。</p><p><a href="RESULTS.md">完整结果与证据边界</a> · <a href="../index.html">28 件复刻作品</a> · <a href="evaluation/final/overview.png">最终十件总览</a></p><p>左栏是原生复刻参照，可通过“用户原图”核对原始 JPG。点击图片可放大；中间轮次可展开。所有作品为静态 SVG / PNG。</p></header><main>'''
    page += ''.join(sections)
    page += '</main><footer>原作者与原字库未确认。字体采用授权替代品；每套只有一个新简报的证据，未穷尽内容、格式或未来字形。</footer></html>'
    (ROOT / 'index.html').write_text(page)
    print('Built offline gallery:', len(cases), 'worlds')


if __name__ == '__main__':
    main()
