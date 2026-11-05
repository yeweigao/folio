const { chromium } = require('/Users/vicoye/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const path = require('path');
(async () => {
 const browser = await chromium.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless:true});
 const page = await browser.newPage({viewport:{width:900,height:1200},deviceScaleFactor:1});
 await page.goto('file://'+path.join(__dirname,'poster.svg'));
 await page.evaluate(()=>document.fonts.ready);
 await page.screenshot({path:path.join(__dirname,'preview.png')});
 const checks = await page.evaluate(()=>({
  fonts:document.fonts.check('700 60px "Study Condensed"'),
  dimensions:[document.documentElement.getAttribute('width'),document.documentElement.getAttribute('height')],
  texts:[...document.querySelectorAll('text')].map(el=>({text:el.textContent,box:(()=>{const b=el.getBBox();return{x:b.x,y:b.y,width:b.width,height:b.height};})()})),
  embeddedFonts:document.querySelector('style').textContent.includes('data:font/woff2;base64,')
 }));
 console.log(JSON.stringify(checks,null,2));
 await browser.close();
})();
