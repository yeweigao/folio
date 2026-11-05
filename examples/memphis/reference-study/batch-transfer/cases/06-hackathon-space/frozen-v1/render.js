const { chromium } = require('/Users/vicoye/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const path = require('path');
(async () => {
  const browser = await chromium.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:true});
  const page = await browser.newPage({viewport:{width:900,height:1200},deviceScaleFactor:1});
  await page.goto('file://' + path.join(__dirname,'poster.svg'));
  await page.evaluate(() => document.fonts.ready);
  await page.screenshot({path:path.join(__dirname,'poster.png')});
  const text = await page.locator('text').evaluateAll(nodes => nodes.map(n=>{const b=n.getBBox(); return {text:n.textContent, x:b.x,y:b.y,width:b.width,height:b.height,font:getComputedStyle(n).fontFamily};}));
  console.log(JSON.stringify(text,null,2));
  await browser.close();
})();
