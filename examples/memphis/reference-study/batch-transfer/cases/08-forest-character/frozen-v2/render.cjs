const {chromium}=require('/Users/vicoye/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
(async()=>{
const browser=await chromium.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:true});
const page=await browser.newPage({viewport:{width:900,height:1200},deviceScaleFactor:1});
await page.goto('file:///Users/vicoye/Documents/GitHub/folio/examples/memphis/reference-study/batch-transfer/cases/08-forest-character/output-v2/poster.svg');
await page.evaluate(()=>document.fonts.ready);
await page.screenshot({path:'/Users/vicoye/Documents/GitHub/folio/examples/memphis/reference-study/batch-transfer/cases/08-forest-character/output-v2/preview.png'});
console.log(await page.evaluate(()=>Array.from(document.querySelectorAll('text')).map(t=>({text:t.textContent.trim(),box:[t.getBBox().x,t.getBBox().y,t.getBBox().width,t.getBBox().height],font:getComputedStyle(t).fontFamily}))));
await browser.close();
})();
