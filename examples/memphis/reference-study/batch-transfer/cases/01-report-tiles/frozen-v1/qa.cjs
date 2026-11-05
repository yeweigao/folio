const { chromium } = require('/Users/vicoye/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const path = require('path');
const fs = require('fs');
(async () => {
  const browser = await chromium.launch({ executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless: true });
  const page = await browser.newPage({ viewport: { width: 1280, height: 720 }, deviceScaleFactor: 1 });
  await page.goto('file://' + path.join(__dirname, 'poster.svg'));
  await page.evaluate(() => document.fonts.ready);
  const metrics = await page.evaluate(() => Array.from(document.querySelectorAll('text')).map(n => {
    const b = n.getBBox();
    return { text: n.textContent.replace(/\s+/g,' ').trim(), x:b.x, y:b.y, width:b.width, height:b.height, family:getComputedStyle(n).fontFamily };
  }));
  const result = { width:1280, height:720, text:metrics,
    outOfBounds:metrics.filter(n => n.x < 0 || n.y < 0 || n.x+n.width > 920 || n.y+n.height > 720),
    embeddedFaces: await page.evaluate(() => Array.from(document.fonts).map(f => ({family:f.family,weight:f.weight,status:f.status}))) };
  fs.writeFileSync(path.join(__dirname, 'qa.json'), JSON.stringify(result,null,2));
  await page.screenshot({ path: path.join(__dirname,'preview.png') });
  await browser.close();
  console.log(JSON.stringify(result,null,2));
})();
