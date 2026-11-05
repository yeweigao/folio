const { chromium } = require('/Users/vicoye/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const path = require('path');
const { pathToFileURL } = require('url');
(async () => {
  const browser = await chromium.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:true});
  const page = await browser.newPage({viewport:{width:900,height:1200},deviceScaleFactor:1});
  await page.goto(pathToFileURL(path.join(__dirname,'poster.svg')).href);
  await page.evaluate(() => document.fonts.ready);
  await page.screenshot({path:path.join(__dirname,'preview.png')});
  const result = await page.evaluate(() => ({
    fontsLoaded:document.fonts.status,
    faces:[...document.fonts].map(f=>({family:f.family,weight:f.weight,status:f.status})),
    text:[...document.querySelectorAll('text')].map(t=>({text:t.textContent,box:{x:t.getBBox().x,y:t.getBBox().y,width:t.getBBox().width,height:t.getBBox().height}}))
  }));
  console.log(JSON.stringify(result,null,2));
  await browser.close();
})();
