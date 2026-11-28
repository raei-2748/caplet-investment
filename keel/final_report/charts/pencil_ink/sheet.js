const { chromium } = require('playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage({deviceScaleFactor:2});
const parts=['option_a_columns','option_b_range','option_c_bars'].map((n,i)=>`<div style="margin:0 0 28px"><div style="font:bold 15px 'Liberation Serif';color:#555;margin-bottom:6px">${'ABC'[i]}</div>${fs.readFileSync(n+'.svg','utf8')}</div>`).join('');
await p.setContent(`<body style="margin:0;padding:20px;background:#fff;width:640px;display:inline-block">${parts}</body>`);
await (await p.$('body')).screenshot({path:'options_sheet.png'});await b.close();})();
