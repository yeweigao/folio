const fs = require('node:fs');
const path = require('node:path');
const { chromium } = require('/Users/vicoye/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');

(async () => {
  const browser = await chromium.launch({
    executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    headless: true,
  });
  const page = await browser.newPage({ viewport: { width: 900, height: 1200 }, deviceScaleFactor: 1 });
  await page.goto('file://' + path.join(__dirname, 'poster.svg'));
  await page.evaluate(() => document.fonts.ready);
  await page.screenshot({ path: path.join(__dirname, 'preview.png') });
  const qa = await page.evaluate(() => ({
    dimensions: [document.documentElement.getAttribute('width'), document.documentElement.getAttribute('height')],
    fontFaces: [...document.fonts].map(f => ({ family: f.family, weight: f.weight, status: f.status })),
    texts: [...document.querySelectorAll('text')].map(t => {
      const r = t.getBoundingClientRect();
      return {
        text: t.textContent,
        family: getComputedStyle(t).fontFamily,
        fontSize: getComputedStyle(t).fontSize,
        bounds: { x: r.x, y: r.y, width: r.width, height: r.height },
      };
    }),
    embeddedFaces: [...document.querySelectorAll('style')].reduce((n, s) => n + (s.textContent.match(/data:font\/woff2;base64,/g) || []).length, 0),
  }));
  fs.writeFileSync(path.join(__dirname, 'qa.json'), JSON.stringify(qa, null, 2) + '\n');
  console.log(JSON.stringify(qa, null, 2));
  await browser.close();
})();
