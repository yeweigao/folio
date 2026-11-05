const fs = require('fs');
const path = require('path');
const { chromium } = require('/Users/vicoye/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
(async () => {
  const browser = await chromium.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:true});
  const page = await browser.newPage({viewport:{width:900,height:1200},deviceScaleFactor:1});
  await page.goto('file://' + path.join(__dirname,'poster.svg'));
  await page.evaluate(() => document.fonts.ready);
  await page.screenshot({path:path.join(__dirname,'render.png')});
  const report = await page.evaluate(() => ({
    width:document.documentElement.getAttribute('width'),
    height:document.documentElement.getAttribute('height'),
    fonts:[...document.fonts].map(f => ({family:f.family,weight:f.weight,status:f.status})),
    texts:[...document.querySelectorAll('text')].map(el => {
      const b=el.getBoundingClientRect();
      return {id:el.id,text:el.textContent,x:b.x,y:b.y,width:b.width,height:b.height,withinPage:b.x>=0 && b.y>=0 && b.right<=900 && b.bottom<=1200};
    })
  }));
  fs.writeFileSync(path.join(__dirname,'qa.json'),JSON.stringify(report,null,2));
  await page.setViewportSize({width:225,height:300});
  await page.evaluate(() => {
    document.documentElement.style.width='225px';
    document.documentElement.style.height='300px';
  });
  await page.screenshot({path:path.join(__dirname,'thumbnail.png')});
  await browser.close();
  console.log(JSON.stringify(report,null,2));
})();
