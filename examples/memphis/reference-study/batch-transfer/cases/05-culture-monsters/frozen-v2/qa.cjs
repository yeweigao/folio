const { chromium } = require('/Users/vicoye/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const path = require('path');
const fs = require('fs');
(async () => {
  const browser = await chromium.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:true});
  const page = await browser.newPage({viewport:{width:900,height:1200},deviceScaleFactor:1});
  await page.setContent('<!doctype html><html><head><style>html,body{margin:0;width:900px;height:1200px;overflow:hidden}svg{display:block}</style></head><body>' + fs.readFileSync(path.join(__dirname,'poster.svg'),'utf8') + '</body></html>');
  await page.evaluate(() => document.fonts.ready);
  const report = await page.evaluate(() => ({
    fonts:document.fonts.status,
    size:[document.querySelector('svg').getAttribute('width'),document.querySelector('svg').getAttribute('height')],
    text:[...document.querySelectorAll('text')].map(n=>{
      const b=n.getBBox();
      return {text:n.textContent,box:[b.x,b.y,b.width,b.height],font:getComputedStyle(n).fontFamily,weight:getComputedStyle(n).fontWeight};
    })
  }));
  fs.writeFileSync(path.join(__dirname,'qa.json'),JSON.stringify(report,null,2));
  console.log(JSON.stringify(report,null,2));
  await page.screenshot({path:path.join(__dirname,'preview.png'),clip:{x:0,y:0,width:900,height:1200},timeout:20000});
  await browser.close();
})();
