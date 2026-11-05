const { chromium } = require('/Users/vicoye/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const { pathToFileURL } = require('url');
const fs = require('fs');
const path = require('path');
(async () => {
  const browser = await chromium.launch({executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless: true});
  const page = await browser.newPage({viewport:{width:900,height:1200},deviceScaleFactor:1});
  await page.goto(pathToFileURL(path.join(__dirname,'poster.svg')).href);
  await page.evaluate(() => document.fonts.ready);
  await page.screenshot({path:path.join(__dirname,'self-preview.png')});
  const data = await page.evaluate(() => ({
    fonts: [...document.fonts].map(f => ({family:f.family,weight:f.weight,status:f.status})),
    text: [...document.querySelectorAll('text')].map(e => {const b=e.getBBox();return {id:e.id,text:e.textContent,bbox:{x:b.x,y:b.y,w:b.width,h:b.height},family:getComputedStyle(e).fontFamily,size:getComputedStyle(e).fontSize,weight:getComputedStyle(e).fontWeight};}),
    size: {width:document.documentElement.getAttribute('width'),height:document.documentElement.getAttribute('height')},
    images: document.querySelectorAll('image').length,
    paths:document.querySelectorAll('path').length
  }));
  fs.writeFileSync(path.join(__dirname,'self-qa.json'),JSON.stringify(data,null,2));
  console.log(JSON.stringify(data));
  await browser.close();
})();
