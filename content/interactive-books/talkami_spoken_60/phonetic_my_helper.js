/* Talkami phonetic_my: keep standard pinyin; Myanmar-script sound cues are approximate.
   Existing 47/48 transcription takes precedence. Validate before publishing. */
const TalkamiPhonetics=(()=>{
 const clean=s=>String(s||'').toLowerCase().replace(/[üǖǘǚǜ]/g,'v').replace(/u:/g,'v').normalize('NFD').replace(/[\u0300-\u036f]/g,'').replace(/[^a-zv]/g,'');
 const manual=Object.fromEntries(('a:အာ|ai:အိုင်|an:အန်|ang:အန်း|ao:အော|e:အဲ|ei:အေး|er:အာ|ou:အိုး|bai:ပိုင်|bei:ပေ|ben:ပန်|bing:ပင်း|biao:ပြောင်|cha:ချာ|chang:ချန်း|chi:ချီး|chuang:ချွန်း|chuan:ချွန်|chou:ချိုး|chuai:ချွိုင်|cang:ဆန်း|can:ဆန်|ceng:ဆင်|ce:ဆယ်|cuo:ဆွေါ|dang:တန်း|diao:တျောင်|diu:တျိုး|dui:တွေး|duan:တွန်|dun:တွင်|dei:တေး|fa:ဖာ|fang:ဖန်း|feng:ဖင်း|gao:ကောင်|geng:ကင်|gou:ကိုး|hang:ဟန်း|hei:ဟေး|huir:ဟွေးရ်|jia:ကျာ|jiang:ကျန်း|jue:ကျွဲ|jun:ကျွင်|ka:ခါ|kao:ခေါင်|kui:ခွေး|leng:လင်|lin:လင်|liao:လျောင်|lao:လောင်|lv:လျွီ|mang:မန်း|mian:မျန်|mi:မီ|min:မင်|mao:မောင်|miao:မျောင်|mu:မူး|mai:မိုင်|nao:နောင်|nan:နန်|ne:န|nei:နေး|nong:နုန်း|niu:နျိုး|nv:နျွီ|pang:ဖန်း|pian:ဖျန်|piao:ဖျောင်|peng:ဖင်|ping:ဖင်း|que:ချွဲ|ran:ရန်|rang:ရန်း|re:ရယ်|ri:ရီ|se:ဆ|she:ရှဲ|song:ဆုန်း|suo:ဆွေါ|sui:ဆွေး|shun:ရှွင်|shuang:ရှွန်း|shuan:ရှွန်|shuai:ရှွိုင်|ta:ထာ|tai:ထိုင်|te:ထဲ|tang:ထန်း|tu:ထူး|xuan:ရှျွန်|xiong:ရှျုန်း|xue:ရှျွဲ|zan:ဇန်|ze:ဇဲ|zher:ကျဲရ်|zhuo:ကျွေါ|zhuan:ကျွန်|zhang:ကျန်း|zhen:ကျန်|zhun:ကျွင်|zong:ဇုန်း|zhua:ကျွာ|zhuai:ကျွိုင်|cuan:ဆွန်|chun:ချွင်|chuo:ချွေါ|ba:ပါ|ma:မာ|de:တ|le:လ|ge:က|yi:ယီ|wu:ဝူ|wo:ဝေါ|zhong:ကျုန်း|zhi:ကျီး|zhui:ကျွေး|zhu:ကျူး|zui:ဇွေး|zun:ဇွင်|xiao:ရှျောင်|huo:ဟွေါ|shao:ရှောင်|la:လာ|pi:ဖီ|qi:ချီ|qian:ချန်|qiang:ချန်း|qiao:ချောင်|qie:ချဲ|qiu:ချိုး|qiong:ချုန်း|qu:ချွီ|guang:ကွန်း|guo:ကွေါ|ruo:ရွေါ|cui:ဆွေး|cu:ဆူး|pu:ဖူး|luo:လွေါ|nve:နွဲ|nuan:နွန်|pou:ဖိုး|tui:ထွေး|tong:ထုန်း|lou:လိုး|zhou:ကျိုး|sang:ဆန်း|tuan:ထွန်|tou:ထိုး|nie:နျဲ').split('|').map(x=>x.split(':')));
 const pref={zh:'ကျ',ch:'ချ',sh:'ရှ',b:'ပ',p:'ဖ',m:'မ',f:'ဖ',d:'တ',t:'ထ',n:'န',l:'လ',g:'က',k:'ခ',h:'ဟ',j:'ကျ',q:'ချ',x:'ရှ',r:'ရ',z:'ဇ',c:'ဆ',s:'စ',y:'ယ',w:'ဝ'};
 const fin={a:'ာ',o:'ေါ',e:'ဲ',i:'ီ',u:'ူ',v:'ျွီ',ai:'ိုင်',ei:'ေး',ao:'ောင်',ou:'ိုး',an:'န်',en:'င်',ang:'န်း',eng:'င်',ong:'ုန်း',ia:'ျာ',ie:'ျဲ',iao:'ျောင်',iu:'ျိုး',ian:'ျန်',in:'င်',iang:'ျန်း',ing:'င်း',iong:'ျုန်း',ua:'ွာ',uo:'ွေါ',uai:'ွိုင်',ui:'ွေး',uan:'ွန်',un:'ွင်',uang:'ွန်း',ue:'ွဲ',ve:'ွဲ',van:'ွန်',vn:'ွင်',er:'ာ'};
 const initials=Object.keys(pref).sort((a,b)=>b.length-a.length);
 function fallback(k){let q=initials.find(x=>k.startsWith(x));if(!q)return '';let f=k.slice(q.length);if(q==='y'&&['u','ue','uan','un'].includes(f))f={u:'v',ue:'ve',uan:'van',un:'vn'}[f];return fin[f]?pref[q]+fin[f]:''}
 function dictionary(packs){
  const counts=new Map(),conflicts=[];
  for(const pack of packs)for(const p of pack.lessons.flatMap(l=>l.phrases)){
   if(!p.pinyin||!p.phonetic_my)continue;const a=p.pinyin.trim().split(/\s+/),b=p.phonetic_my.trim().split(/\s+/);if(a.length!==b.length)continue;
   for(let i=0;i<a.length;i++){const k=clean(a[i]);if(!k)continue;let m=counts.get(k);if(!m){m=new Map();counts.set(k,m)}m.set(b[i],(m.get(b[i])||0)+1)}
  }
  const map=new Map();for(const [k,m]of counts){if(m.size>1)conflicts.push(k);map.set(k,[...m].sort((a,b)=>b[1]-a[1])[0][0])}
  return {map,conflicts}
 }
 const newTrace=()=>({manual:new Set(),fallback:new Set(),unhandled:new Set(),ambiguities:new Set(),latin:new Set()});
 function transcribe(pinyin,map,trace){
  return pinyin.trim().split(/\s+/).map(py=>{const k=clean(py);if(!k)throw Error('Bad syllable '+py);if(map.has(k))return map.get(k);if(manual[k]){trace.manual.add(k);return manual[k]}
   const s=fallback(k);if(s){trace.fallback.add(k);return s}trace.unhandled.add(k);throw Error('Unknown syllable '+k)}).join(' ');
 }
 function charsDict(text){const a=new Map();for(const l of text.split(/\r?\n/)){const m=/^U\+([0-9A-F]+):\s*([^#]+)/.exec(l);if(m)a.set(String.fromCodePoint(parseInt(m[1],16)),m[2].trim().split(',').map(x=>x.trim()).filter(Boolean))}return a}
 function phrasesDict(text){const a=new Map();for(const l of text.split(/\r?\n/)){let p=l.indexOf(': ');if(p<1||l.startsWith('#'))continue;const s=l.slice(0,p),r=l.slice(p+2).trim().split(/\s+/);if(s.length>18||[...s].length!==r.length||![...s].every(x=>/\p{Script=Han}/u.test(x)))continue;a.set(s,r)}return a}
 const latin={AA:['ēi','ēi'],'Type-C':['tài','pǔ','xī'],A:['ēi'],C:['xī'],G:['jī']};
 function pinyinOf(text,chars,phrases,trace){
  const input=[...text],out=[],source=[];
  for(let i=0;i<input.length;){
   if(/\p{Script=Han}/u.test(input[i])){
    let hit=null;for(let n=Math.min(9,input.length-i);n>=2;n--){let ph=phrases.get(input.slice(i,i+n).join(''));if(ph&&ph.length===n){hit=ph;break}}
    if(hit){out.push(...hit);source.push(...input.slice(i,i+hit.length));i+=hit.length;continue}
    const vals=chars.get(input[i]);if(!vals?.length)throw Error('Unknown Hanzi '+input[i]+' in '+text);
    if(vals.length>1)trace.ambiguities.add(input[i]+': '+vals.join('/'));out.push(vals[0]);source.push(input[i]);i++;continue
   }
   const tok=Object.keys(latin).sort((a,b)=>b.length-a.length).find(k=>text.startsWith(k,i));
   if(tok){out.push(...latin[tok]);source.push(...latin[tok].map(()=>'◌'));trace.latin.add(text);i+=tok.length;continue}
   if(/[a-zA-Z0-9]/.test(input[i]))throw Error('Unrecognized Latin/digit in '+text);
   i++;
  }
  if(!out.length)throw Error('No Hanzi in '+text);
  const isFourth=x=>/[àèìòùǜ]/.test(x);
  for(let i=0;i<out.length-1;i++){
   if(source[i]==='不'&&clean(out[i])==='bu'&&isFourth(out[i+1]))out[i]='bú';
   if(source[i]==='一'&&clean(out[i])==='yi'&&source[i-1]!=='第')out[i]=isFourth(out[i+1])?'yí':'yì';
  }
  return out.join(' ')
 }
 function upgrade(pack,opts){
  const cards=pack.lessons.flatMap(l=>l.phrases),ids=cards.map(x=>x.id).join('|');let py=0,ph=0;
  for(const c of cards){if(!c.pinyin?.trim()){if(!opts.chars||!opts.phrases)throw Error('missing reading dictionaries');c.pinyin=pinyinOf(c.text,opts.chars,opts.phrases,opts.trace);py++}
   if(!c.phonetic_my?.trim()){c.phonetic_my=transcribe(c.pinyin,opts.map,opts.trace);ph++}
   const pp=c.pinyin.trim().split(/\s+/),mm=c.phonetic_my.trim().split(/\s+/);
   if(pp.length!==mm.length||mm.some(x=>!(/[\u1000-\u109f]/.test(x)))||/[A-Za-z]/.test(c.phonetic_my))throw Error('Bad alignment '+c.id)
  }
  if(cards.map(x=>x.id).join('|')!==ids)throw Error('ID changed');
  pack.version=Number(pack.version||1)+1;
  pack.updated_at='2026-10-11T12:45:00Z';
  return {cards:cards.length,added_pinyin:py,added_phonetic_my:ph}
 }
 function utf8(s){const b=[];for(let i=0;i<s.length;i++){let c=s.charCodeAt(i);if(c<128)b.push(c);else if(c<2048)b.push(192|c>>6,128|c&63);else if(c>=55296&&c<=56319&&i+1<s.length){let d=s.charCodeAt(++i),p=65536+((c-55296)<<10)+(d-56320);b.push(240|p>>18,128|p>>12&63,128|p>>6&63,128|p&63)}else b.push(224|c>>12,128|c>>6&63,128|c&63)}return new Uint8Array(b)}
 function sha256(s){
  const arr=Array.from(utf8(s)),bits=arr.length*8;arr.push(128);while(arr.length%64!==56)arr.push(0);for(let i=7;i>=0;i--)arr.push(Math.floor(bits/2**(i*8))&255);
  const primes=[];for(let i=2;primes.length<64;i++)if(primes.every(x=>i%x))primes.push(i);
  let h=primes.slice(0,8).map(x=>((Math.sqrt(x)%1)*2**32)>>>0),K=primes.map(x=>((Math.cbrt(x)%1)*2**32)>>>0);
  const rr=(x,n)=>x>>>n|x<<32-n;
  for(let i=0;i<arr.length;i+=64){const w=new Uint32Array(64);for(let j=0;j<16;j++)w[j]=(arr[i+j*4]<<24|arr[i+j*4+1]<<16|arr[i+j*4+2]<<8|arr[i+j*4+3])>>>0;
   for(let j=16;j<64;j++)w[j]=(w[j-16]+(rr(w[j-15],7)^rr(w[j-15],18)^w[j-15]>>>3)+w[j-7]+(rr(w[j-2],17)^rr(w[j-2],19)^w[j-2]>>>10))>>>0;
   let [a,b,c,d,e,f,g,z]=h;for(let j=0;j<64;j++){let x=(z+(rr(e,6)^rr(e,11)^rr(e,25))+((e&f)^(~e&g))+K[j]+w[j])>>>0,y=((rr(a,2)^rr(a,13)^rr(a,22))+((a&b)^(a&c)^(b&c)))>>>0;z=g;g=f;f=e;e=(d+x)>>>0;d=c;c=b;b=a;a=(x+y)>>>0}h=h.map((v,j)=>(v+[a,b,c,d,e,f,g,z][j])>>>0)
  }return h.map(x=>x.toString(16).padStart(8,'0')).join('')
 }
 return {clean,manual,dictionary,newTrace,transcribe,charsDict,phrasesDict,pinyinOf,upgrade,utf8,sha256};
})();
