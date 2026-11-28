const { chromium } = require('playwright');
const fs=require('fs'),path=require('path');
(async()=>{const svg=fs.readFileSync(process.argv[2],'utf8');const b=await chromium.launch();
const p=await b.newPage({deviceScaleFactor:Number(process.argv[4]||2)});
await p.setContent(`<html><body style="margin:0;background:#fff">${svg}</body></html>`);
const el=await p.$('svg');await el.screenshot({path:process.argv[3]});
if(process.argv[5]){await p.emulateMedia({});await p.addStyleTag({content:'svg{filter:grayscale(1)}'});await el.screenshot({path:process.argv[5]});}
await b.close();})();
