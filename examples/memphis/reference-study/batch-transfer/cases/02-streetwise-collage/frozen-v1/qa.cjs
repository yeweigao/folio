const fs = require('node:fs');
const path = require('node:path');
const { chromium } = require('/Users/vicoye/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
(async () => {
 const browser = await chromium.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:true});
 const page = await browser.newPage({viewport:{width:900,height:1200}, deviceScaleFactor:1});
 await page.goto('file://' + path.resolve('output-v1/poster.svg'));
 await page.evaluate(() => document.fonts.ready);
 const report = await page.evaluate(() => ({
  width: document.documentElement.width.baseVal.value,
  height: document.documentElement.height.baseVal.value,
  text: [...document.querySelectorAll('text')].map(t=>{const b=t.getBBox();return {text:t.textContent,x:b.x,y:b.y,width:b.width,height:b.height,font:getComputedStyle(t).fontFamily}}),
  fonts: [...document.fonts].map(f=>({family:f.family,weight:f.weight,status:f.status})),
  images: document.querySelectorAll('image').length
 }));
 fs.writeFileSync('output-v1/qa.json', JSON.stringify(report,null,2));
 await page.screenshot({path:'output-v1/preview.png'});
 console.log(JSON.stringify(report));
 await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
