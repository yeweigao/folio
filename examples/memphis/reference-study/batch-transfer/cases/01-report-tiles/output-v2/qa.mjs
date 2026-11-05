import { chromium } from '/Users/vicoye/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright/index.mjs';
import { writeFile } from 'node:fs/promises';
const base = new URL('.', import.meta.url);
const browser = await chromium.launch({ executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless: true });
const page = await browser.newPage({ viewport: { width: 1280, height: 720 }, deviceScaleFactor: 1 });
await page.goto(new URL('poster.svg', base).href);
await page.evaluate(() => document.fonts.ready);
await page.screenshot({ path: new URL('preview.png', base).pathname });
const result = await page.evaluate(() => ({
  dimensions: [document.documentElement.getAttribute('width'), document.documentElement.getAttribute('height')],
  fonts: [...document.fonts].map(f => ({ family: f.family, weight: f.weight, status: f.status })),
  texts: [...document.querySelectorAll('text')].map(e => {
    const b = e.getBBox(); const s = getComputedStyle(e);
    return { text: e.textContent, x: b.x, y: b.y, width: b.width, height: b.height, family: s.fontFamily, size: s.fontSize, weight: s.fontWeight };
  }),
  embeddedFaces: (document.querySelector('style').textContent.match(/@font-face/g) || []).length,
  images: document.querySelectorAll('image').length,
}));
await writeFile(new URL('qa.json', base), JSON.stringify(result, null, 2) + '\n');
console.log(JSON.stringify(result, null, 2));
await browser.close();
