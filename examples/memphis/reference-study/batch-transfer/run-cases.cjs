// Freeze and independently render completed maker outputs. No drawing decisions.
const fs=require('fs'),path=require('path'),crypto=require('crypto'),{pathToFileURL}=require('url');
const runtime='/Users/vicoye/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/';
const {chromium}=require(runtime+'playwright'),sharp=require(runtime+'sharp');
const ROOT=__dirname,stage=process.argv[2]||'v1',ids=process.argv.slice(3);
const meta=JSON.parse(fs.readFileSync(path.join(ROOT,'cases.json')));
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
function luminance(rgb){return rgb.map(n=>{n/=255;return n<=.04045?n/12.92:((n+.055)/1.055)**2.4}).reduce((v,n,i)=>v+n*[.2126,.7152,.0722][i],0)}
function ratio(a,b){const x=luminance(a),y=luminance(b);return (Math.max(x,y)+.05)/(Math.min(x,y)+.05)}
async function main(){
 const browser=await chromium.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:true});
 const page=await browser.newPage({deviceScaleFactor:1});
 for(const m of meta.filter(c=>!ids.length||ids.includes(c.id))){
  const caseDir=path.join(ROOT,'cases',m.id),out=path.join(caseDir,'output-'+stage),frozen=path.join(caseDir,'frozen-'+stage);
  if(!fs.existsSync(path.join(out,'poster.svg')))throw Error('Missing completed output '+m.id);
  if(!fs.existsSync(frozen)){
   fs.cpSync(out,frozen,{recursive:true});
   const fingerprints={};for(const n of fs.readdirSync(frozen)){const p=path.join(frozen,n);if(fs.statSync(p).isFile())fingerprints[n]={sha256:hash(fs.readFileSync(p)),bytes:fs.statSync(p).size}}
   fs.writeFileSync(path.join(caseDir,'frozen-'+stage+'-manifest.json'),JSON.stringify(fingerprints,null,2));
  }
  await page.setViewportSize({width:m.width,height:m.height});
  await page.goto(pathToFileURL(path.join(frozen,'poster.svg')).href,{waitUntil:'networkidle'});await page.evaluate(()=>document.fonts.ready);
  // Retain a maker's same-named preview before producing the independent render.
  const makerManifest=JSON.parse(fs.readFileSync(path.join(caseDir,'frozen-'+stage+'-manifest.json')));
  if(makerManifest['poster.png']&&!fs.existsSync(path.join(frozen,'maker-poster.png'))){
   const source=path.join(out,'poster.png');
   if(!fs.existsSync(source)||hash(fs.readFileSync(source))!==makerManifest['poster.png'].sha256)throw Error('Original maker preview changed '+m.id);
   fs.copyFileSync(source,path.join(frozen,'maker-poster.png'));
  }
  await page.screenshot({path:path.join(frozen,'poster.png')});
  fs.writeFileSync(path.join(frozen,'render-provenance.json'),JSON.stringify({renderer:'Independent Chrome/Playwright render of frozen poster.svg',svg_sha256:hash(fs.readFileSync(path.join(frozen,'poster.svg'))),render_sha256:hash(fs.readFileSync(path.join(frozen,'poster.png'))),maker_preview:makerManifest['poster.png']?{path:'maker-poster.png',sha256:makerManifest['poster.png'].sha256}:null},null,2));
  const audit=await page.evaluate(()=>({texts:[...document.querySelectorAll('text')].map((t,i)=>{
    let text='',previousY=null;
    for(const node of t.childNodes){
     const value=node.textContent||'';const y=node.nodeType===1?node.getBoundingClientRect().y:previousY;
     if(previousY!==null&&y!==null&&Math.abs(y-previousY)>2&&/[A-Za-z0-9,.!?]$/.test(text)&&/^[A-Za-z0-9]/.test(value))text+=' ';
     text+=value;if(y!==null)previousY=y;
    }
    t.setAttribute('data-audit-id',i);const r=t.getBoundingClientRect(),s=getComputedStyle(t);return {text,rawText:t.textContent,x:r.x,y:r.y,width:r.width,height:r.height,fill:s.fill,size:s.fontSize,weight:s.fontWeight,font:s.fontFamily,outOfFrame:r.x < -1||r.y < -1||r.right > innerWidth+1||r.bottom > innerHeight+1};
   }),fonts:[...document.fonts].filter(f=>f.status==='loaded').map(f=>({family:f.family,weight:f.weight})),fontErrors:[...document.fonts].filter(f=>f.status==='error').map(f=>f.family),rasterImages:document.querySelectorAll('image').length}));
  const cdp=await page.context().newCDPSession(page);await cdp.send('DOM.enable');await cdp.send('CSS.enable');
  const doc=await cdp.send('DOM.getDocument');const nodes=await cdp.send('DOM.querySelectorAll',{nodeId:doc.root.nodeId,selector:'text'});
  audit.actualFonts=[];
  for(let i=0;i<nodes.nodeIds.length;i++)audit.actualFonts.push({text:audit.texts[i].text,...await cdp.send('CSS.getPlatformFontsForNode',{nodeId:nodes.nodeIds[i]})});
  await cdp.detach();
  await page.evaluate(()=>document.querySelectorAll('text').forEach(t=>t.style.visibility='hidden'));
  const bg=await page.screenshot();const background=await sharp(bg).removeAlpha().raw().toBuffer();
  audit.contrast=[];
  for(let i=0;i<audit.texts.length;i++){
   const t=audit.texts[i],fg=(t.fill.match(/[\d.]+/g)||[]).slice(0,3).map(Number);
   if(fg.length!==3||t.width<=0||t.height<=0){audit.contrast.push({text:t.text,unsupported:true});continue}
   const clip={x:Math.max(0,Math.floor(t.x)),y:Math.max(0,Math.floor(t.y)),width:Math.max(1,Math.min(m.width,Math.ceil(t.x+t.width))-Math.max(0,Math.floor(t.x))),height:Math.max(1,Math.min(m.height,Math.ceil(t.y+t.height))-Math.max(0,Math.floor(t.y)))};
   if(clip.x>=m.width||clip.y>=m.height){audit.contrast.push({text:t.text,notVisible:true});continue}
   await page.evaluate(id=>document.querySelector(`[data-audit-id="${id}"]`).style.visibility='visible',i);
   const shot=await page.screenshot({clip});const pixels=await sharp(shot).removeAlpha().raw().toBuffer();
   await page.evaluate(id=>document.querySelector(`[data-audit-id="${id}"]`).style.visibility='hidden',i);
   const values=[];
   for(let y=0;y<clip.height;y+=2)for(let x=0;x<clip.width;x+=2){
    const k=(y*clip.width+x)*3,b=((y+clip.y)*m.width+x+clip.x)*3;
    const ink=[pixels[k],pixels[k+1],pixels[k+2]],ground=[background[b],background[b+1],background[b+2]];
    if(ink.every((n,j)=>Math.abs(n-fg[j])<=10)&&ink.reduce((n,v,j)=>n+Math.abs(v-ground[j]),0)>30)values.push(ratio(fg,ground));
   }
   values.sort((a,b)=>a-b);
   audit.contrast.push({text:t.text,samples:values.length,min:values.length?+values[0].toFixed(3):null,p05:values.length?+values[Math.floor(values.length*.05)].toFixed(3):null,below3:values.filter(n=>n<3).length,below4_5:values.filter(n=>n<4.5).length});
  }
  await page.evaluate(()=>document.querySelectorAll('text').forEach(t=>{t.style.removeProperty('visibility');t.removeAttribute('data-audit-id')}));
  fs.writeFileSync(path.join(frozen,'audit.json'),JSON.stringify(audit,null,2));
  const seen=audit.texts.map(t=>t.text).join('\n').replace(/([\p{Script=Han}，。！？、；：」》])\n(?=[\p{Script=Han}「《])/gu,'$1');
  fs.writeFileSync(path.join(frozen,'seen.txt'),seen);
  console.log(JSON.stringify({id:m.id,stage,texts:audit.texts.length,fonts:audit.fonts.length,bounds:audit.texts.filter(t=>t.outOfFrame).map(t=>t.text),lowContrast:audit.contrast.filter(c=>c.min!==null&&c.min<3).map(c=>[c.text,c.min])}));
 }
 await browser.close();
}
main().catch(e=>{console.error(e);process.exit(1)});
