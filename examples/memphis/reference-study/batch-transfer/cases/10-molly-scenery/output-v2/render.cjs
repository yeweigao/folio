const { chromium } = require('/Users/vicoye/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const { pathToFileURL } = require('url');
const path = require('path');
const fs = require('fs');
(async () => {
 let browser;
 try {
  browser = await chromium.launch({ executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless: true, args:['--disable-gpu','--allow-file-access-from-files'] });
  const page = await browser.newPage({ viewport: { width: 1080, height: 1528 }, deviceScaleFactor: 1 });
  await page.goto(pathToFileURL(path.join(__dirname,'poster.svg')).href);
  await page.evaluate(async () => { await document.fonts.ready; });
  const report=await page.evaluate(() => ({fontStatus:document.fonts.status,fonts:[...document.fonts].map(f=>({family:f.family,weight:f.weight,status:f.status})),text:[...document.querySelectorAll('text')].map(t=>({text:t.textContent,bounds:{x:t.getBBox().x,y:t.getBBox().y,width:t.getBBox().width,height:t.getBBox().height}})),svg:{width:document.documentElement.getAttribute('width'),height:document.documentElement.getAttribute('height')}}));
  fs.writeFileSync(path.join(__dirname,'qa.json'),JSON.stringify(report,null,2));
  console.log(JSON.stringify(report,null,2));
  const cdp=await page.context().newCDPSession(page);
  await cdp.send('Emulation.setDeviceMetricsOverride',{width:1080,height:1528,screenWidth:1080,screenHeight:1528,deviceScaleFactor:1,mobile:false});
  const capture=await cdp.send('Page.captureScreenshot',{format:'png',captureBeyondViewport:true,clip:{x:0,y:0,width:1080,height:1528,scale:1}});
  fs.writeFileSync(path.join(__dirname,'poster.png'),Buffer.from(capture.data,'base64'));
 } finally { if (browser) await browser.close(); }
})();
