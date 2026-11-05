// Independent inspection of a finished transfer artifact; no design decisions.
const fs=require('fs'),path=require('path'),{pathToFileURL}=require('url');
const {chromium}=require('/Users/vicoye/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
async function main(){
  const dir=path.resolve(__dirname,process.argv[2]||'output-v1');
  const browser=await chromium.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:true});
  const page=await browser.newPage({viewport:{width:1080,height:1528},deviceScaleFactor:1});
  const errors=[];page.on('pageerror',e=>errors.push(e.message));
  await page.goto(pathToFileURL(path.join(dir,'poster.svg')).href,{waitUntil:'networkidle'});
  await page.evaluate(()=>document.fonts.ready);
  await page.screenshot({path:path.join(dir,'poster.png')});
  const result=await page.evaluate(()=>({
    width:innerWidth,height:innerHeight,
    texts:[...document.querySelectorAll('text')].map(t=>{
      const b=t.getBoundingClientRect();const c=getComputedStyle(t);
      return {text:t.textContent,x:b.x,y:b.y,width:b.width,height:b.height,
        font:c.fontFamily,size:c.fontSize,weight:c.fontWeight,fill:c.fill,
        outOfFrame:b.x < -1||b.y < -1||b.right > innerWidth+1||b.bottom > innerHeight+1};
    }),
    loadedFonts:[...document.fonts].filter(f=>f.status==='loaded').map(f=>({family:f.family,weight:f.weight})),
    failedFonts:[...document.fonts].filter(f=>f.status==='error').map(f=>f.family),
    rasterImages:document.querySelectorAll('image').length
  }));
  result.pageErrors=errors;
  const client=await page.context().newCDPSession(page);
  await client.send('DOM.enable');await client.send('CSS.enable');
  const dom=await client.send('DOM.getDocument');
  const nodes=await client.send('DOM.querySelectorAll',{nodeId:dom.root.nodeId,selector:'text'});
  result.actualFonts=[];
  for(let i=0;i<nodes.nodeIds.length;i++){
    const fonts=await client.send('CSS.getPlatformFontsForNode',{nodeId:nodes.nodeIds[i]});
    result.actualFonts.push({text:result.texts[i]?.text,fonts:fonts.fonts});
  }
  fs.writeFileSync(path.join(dir,'render-audit.json'),JSON.stringify(result,null,2));
  fs.writeFileSync(path.join(dir,'seen.txt'),result.texts.map(t=>t.text).join('\n'));
  await browser.close();
  console.log(JSON.stringify({textElements:result.texts.length,fontFaces:result.loadedFonts.length,
    fontFailures:result.failedFonts,outOfFrame:result.texts.filter(t=>t.outOfFrame).map(t=>t.text),pageErrors:errors}));
}
main().catch(e=>{console.error(e);process.exit(1)});
