const {chromium}=require('/Users/vicoye/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const fs=require('fs');
(async()=>{
 const browser=await chromium.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:true});
 const page=await browser.newPage({viewport:{width:900,height:1200},deviceScaleFactor:1});
 await page.goto('file:///Users/vicoye/Documents/GitHub/folio/examples/memphis/reference-study/batch-transfer/cases/09-isometric-letter-stage/output-v1/poster.svg');
 await page.evaluate(()=>document.fonts.ready);
 await page.screenshot({path:__dirname+'/preview.png'});
 const result=await page.evaluate(()=>({fontStatus:document.fonts.status,size:[document.documentElement.getAttribute('width'),document.documentElement.getAttribute('height')],text:[...document.querySelectorAll('text')].map(e=>({id:e.id,text:e.textContent,bbox:{x:e.getBBox().x,y:e.getBBox().y,width:e.getBBox().width,height:e.getBBox().height}})),faces:document.querySelectorAll('polygon').length,fontFaces:[...document.fonts].map(f=>({family:f.family,status:f.status}))}));
 fs.writeFileSync(__dirname+'/qa.json',JSON.stringify(result,null,2)+'\n');
 console.log(JSON.stringify(result));
 await browser.close();
})();
