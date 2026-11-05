const fs = require('fs');
const { chromium } = require('/Users/vicoye/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
(async () => {
 const root = __dirname;
 const browser = await chromium.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:true,args:['--disable-gpu']});
 const page = await browser.newPage({viewport:{width:900,height:1200},deviceScaleFactor:1});
 await page.goto('file://' + root + '/poster.svg');
 await page.evaluate(() => document.fonts.ready);
 const qa = await page.evaluate(() => ({
  fontsLoaded:document.fonts.check('700 54px "Study Sans"'),
  texts:[...document.querySelectorAll('text')].map(el=>{const b=el.getBBox();return {text:el.textContent,x:b.x,y:b.y,width:b.width,height:b.height,family:getComputedStyle(el).fontFamily};}),
  rasterCount:document.querySelectorAll('image').length
 }));
 fs.writeFileSync(root+'/qa.json',JSON.stringify(qa,null,2));
 console.log(JSON.stringify(qa,null,2));
 await page.screenshot({path:root+'/preview.png',fullPage:true,timeout:10000});
 await browser.close();
})();
