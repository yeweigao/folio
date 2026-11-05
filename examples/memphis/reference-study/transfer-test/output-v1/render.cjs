const { chromium } = require('/Users/vicoye/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const { pathToFileURL } = require('node:url');
const path = require('node:path');

(async () => {
  const browser = await chromium.launch({
    executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    headless: true,
    args: ['--no-sandbox', '--disable-dev-shm-usage'],
  });
  const page = await browser.newPage({ viewport: { width: 1080, height: 1528 }, deviceScaleFactor: 1 });
  await page.goto(pathToFileURL(path.join(__dirname, 'poster.svg')).href);
  await page.evaluate(() => document.fonts.ready);
  const checks = await page.evaluate(() => ({
    fonts: [...document.fonts].map(f => ({ family: f.family, status: f.status })),
    text: [...document.querySelectorAll('text')].map(t => ({
      value: t.textContent,
      box: { x: t.getBBox().x, y: t.getBBox().y, width: t.getBBox().width, height: t.getBBox().height },
    })),
  }));
  await page.screenshot({ path: path.join(__dirname, 'poster.png'), fullPage: false });
  console.log(JSON.stringify(checks, null, 2));
  await browser.close();
})();
