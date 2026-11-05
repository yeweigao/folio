const { chromium } = require('/Users/vicoye/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const path = require('path');
const fs = require('fs');
(async () => {
  const browser = await chromium.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:true,args:['--disable-gpu']});
  try {
    const page = await browser.newPage({viewport:{width:900,height:1200},deviceScaleFactor:1});
    await page.goto('file://' + path.join(__dirname,'poster.svg'));
    await page.evaluate(() => document.fonts.ready);
    const result = await page.evaluate(() => ({
      dimensions:[document.documentElement.getAttribute('width'),document.documentElement.getAttribute('height')],
      fonts:Array.from(document.fonts).map(f=>({family:f.family,status:f.status})),
      text:Array.from(document.querySelectorAll('text')).map(n=>({text:n.textContent.trim(),bbox:(()=>{const b=n.getBBox();return{x:b.x,y:b.y,width:b.width,height:b.height}})()})),
      embeddedFontFaces:(document.querySelector('style').textContent.match(/@font-face/g)||[]).length,
      images:document.querySelectorAll('image').length
    }));
    fs.writeFileSync(path.join(__dirname,'self-check.json'),JSON.stringify(result,null,2));
    console.log(JSON.stringify(result,null,2));
    await page.screenshot({path:path.join(__dirname,'preview.png'),timeout:15000});
    console.log('Saved preview.png');
  } finally { await browser.close(); }
})().catch(e=>{console.error(e.message);process.exit(1)});
