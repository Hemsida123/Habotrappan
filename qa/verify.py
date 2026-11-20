import runpy,json,re,hashlib,base64,subprocess,tempfile,zipfile,sys
from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1]
def main():
 build=runpy.run_path(str(R/'qa/build.py'))
 html=(Path(sys.argv[1]) if len(sys.argv)>1 else R/'index.html').read_text();s=BeautifulSoup(html,'html.parser')
 assert s.html['lang']=='sv' and s.select_one('meta[name=viewport]') and s.select_one('main#main')
 assert len(s.select('h1'))==1
 assert not s.select('script[src],link[rel=stylesheet],iframe')
 assert not build['ASSET_RE'].search(html)
 assert all(i['src'].startswith('data:') for i in s.select('img[src]'))
 assert any(a.get_text(strip=True)=='Designed by Ekom' for a in s.select('a[href="https://ekom.se"]'))
 assert not re.search(r'localStorage|sessionStorage|XMLHttpRequest|sendBeacon|\bfetch\s*\(',html)
 assert not re.search(r'url\(\s*[\'"]?https?://',html)
 script='\n'.join(t.string or '' for t in s.find_all('script'))
 with tempfile.NamedTemporaryFile(mode='w',suffix='.js') as f:
  f.write(script);f.flush();r=subprocess.run(['node','--check',f.name],capture_output=True,text=True);assert r.returncode==0,r.stderr[:500]
 inv=build['inventory']();pages=inv['pages'];routes={p['route'] for p in pages};assert len(routes)==len(pages) and len(routes)>=12
 valid=routes|set(inv['aliases']);alltext=[]
 for p in pages:
  soup=BeautifulSoup(p['html'],'html.parser');assert len(soup.select('h1'))==1,p['route']
  ids=[e['id'] for e in soup.select('[id]')];assert len(ids)==len(set(ids)),p['route']
  for a in soup.select('a[href]'):
   h=a['href']
   if h.startswith('#/'):assert h[1:].split('?')[0] in valid,(p['route'],h)
  for i in soup.select('img[src]'):assert (R/i['src']).is_file(),i['src']
  alltext.append(soup.get_text(' ',strip=True))
 text=' '.join(alltext);c=json.loads((R/'qa/content.json').read_text())['company']
 for v in [c['legal'],c['email'],c['street']]:assert v in text,v
 media=json.loads((R/'research/media.json').read_text());assert len(media['images'])==9 and media['portrait']['title']=='Jan Englöf'
 assert '/bildgalleri' in routes
 assert all('/trappor/'+s['id'] in routes for s in json.loads((R/'qa/content.json').read_text())['services'])
 hashes={hashlib.sha256(base64.b64decode(payload,validate=True)).hexdigest() for payload in set(re.findall(r'data:[^\s"\'<>;,]+(?:;[^\s"\'<>;,]+)*;base64,([A-Za-z0-9+/=]+)',html))}
 for e in json.loads((R/'bildkallor.json').read_text()):assert e['sha256'] in hashes,e['file']
 for e in json.loads((R/'typsnitt.json').read_text()):assert e['sha256'] in hashes,e['file']
 package=json.loads((R/'qa/package-result.json').read_text());a=Path(package['archive']);assert hashlib.sha256(a.read_bytes()).hexdigest()==package['sha256']
 with zipfile.ZipFile(a) as z:
  assert z.testzip() is None
  assert z.read('index.html')==(R/'index.html').read_bytes()
  assert z.read('redigerbar.html')==(R/'redigerbar.html').read_bytes()
  for n in z.namelist():
   if (R/n).is_file():assert z.read(n)==(R/n).read_bytes(),n
 assert (R/'LAS-MIG.md').is_file()
 print('SITE_VERIFIED')
if __name__=='__main__':main()
