// Run with Node; Playwright is supplied by the Codex workspace runtime.
const fs = require('fs');
const path = require('path');
const http = require('http');
const {chromium} = require('/Users/vicoye/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const root=__dirname;
const types={'.svg':'image/svg+xml','.html':'text/html; charset=utf-8','.woff2':'font/woff2','.json':'application/json'};
const server=http.createServer((req,res)=>{
  const p=path.resolve(root,'.'+decodeURIComponent(req.url.split('?')[0]));
  if(!p.startsWith(root+path.sep)){res.writeHead(403);res.end();return;}
  fs.readFile(p,(err,b)=>{if(err){res.writeHead(404);res.end();return;}res.setHeader('Content-Type',types[path.extname(p)]||'application/octet-stream');res.end(b);});
});
async function main(){
  await new Promise(r=>server.listen(0,'127.0.0.1',r));
  const base=`http://127.0.0.1:${server.address().port}`;
  const browser=await chromium.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:true});
  const page=await browser.newPage({deviceScaleFactor:1});
  const units=JSON.parse(fs.readFileSync(path.join(root,'manifest.json')));
  const report=[];
  fs.mkdirSync(path.join(root,'renders'),{recursive:true});
  const only=process.argv.find(a=>a.startsWith('--only='))?.slice(7);
  for(const u of (process.argv.includes('--gallery-only')?[]:units.filter(u=>!only||u.file===only))){
    await page.setViewportSize({width:u.width,height:u.height});
    await page.goto(base+'/'+u.file,{waitUntil:'networkidle'});
    await page.evaluate(()=>document.fonts.ready);
    await page.screenshot({path:path.join(root,'renders',u.group+'-'+u.name+'.png')});
    const audit=await page.evaluate(()=>{
      const bounds=[];
      for(const t of document.querySelectorAll('text')){
        const b=t.getBoundingClientRect();
        if(b.left < -2 || b.top < -2 || b.right > innerWidth+2 || b.bottom > innerHeight+2)
          bounds.push({text:t.textContent,x:b.x,y:b.y,right:b.right,bottom:b.bottom});
      }
      return {fonts:[...document.fonts].filter(f=>f.status==='loaded').map(f=>`${f.family}:${f.weight}`),textCount:document.querySelectorAll('text').length,outOfFrame:bounds};
    });
    report.push({file:u.file,...audit});
    console.log(u.file,audit.fonts.length+' fonts',audit.outOfFrame.length+' edge crossings');
  }
  if(report.length){
    const file=path.join(root,'render-audit.json');
    const merged=only&&fs.existsSync(file)?JSON.parse(fs.readFileSync(file)).map(a=>report.find(b=>b.file===a.file)||a):report;
    fs.writeFileSync(file,JSON.stringify(merged,null,2));
  }
  // Embedded fonts must work when the user opens the gallery as an ordinary local file.
  const errors=[];page.on('pageerror',e=>errors.push(e.message));
  await page.setViewportSize({width:1440,height:1000});
  await page.goto(require('url').pathToFileURL(path.join(root,'index.html')).href,{waitUntil:'networkidle'});
  await page.evaluate(()=>document.fonts.ready);
  const gallery=await page.evaluate(()=>({units:document.querySelectorAll('figure svg').length,
    duplicateIds:[...document.querySelectorAll('[id]')].map(x=>x.id).filter((id,i,all)=>all.indexOf(id)!==i),
    fonts:[...document.fonts].filter(f=>f.status==='loaded').map(f=>`${f.family}:${f.weight}`),
    fontErrors:[...document.fonts].filter(f=>f.status==='error').map(f=>f.family),
    width:innerWidth,scrollWidth:document.documentElement.scrollWidth}));
  gallery.pageErrors=errors;
  fs.writeFileSync(path.join(root,'gallery-audit.json'),JSON.stringify(gallery,null,2));
  await page.screenshot({path:path.join(root,'previews','gallery-proof.png')});
  await browser.close();server.close();
}
main().catch(e=>{console.error(e);server.close();process.exit(1)});
