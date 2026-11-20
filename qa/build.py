import json,re,base64,mimetypes,subprocess,zipfile,hashlib,html
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
ASSET_RE=re.compile(r'(?<![A-Za-z0-9_./:\-])(?:assets|fonts)/[A-Za-z0-9_./\-]+\.(?:avif|webp|png|jpg|jpeg|woff2|ttf)(?![A-Za-z0-9_.\-])')
def read(name):return (ROOT/name).read_text()
def jsjson(v):return json.dumps(v,ensure_ascii=False,separators=(',',':')).replace('<','\\u003c')
def prefix():return 'const CONTENT='+jsjson(json.loads(read('qa/content.json')))+';\nconst MEDIA='+jsjson(json.loads(read('research/media.json')))+';\n'
def pure():return read('qa/site.js').split('//__BROWSER__')[0]
def node(code):
 r=subprocess.run(['node'],input=code,capture_output=True,text=True)
 if r.returncode:raise RuntimeError(r.stderr[:2000])
 return r.stdout
def inventory():return json.loads(node(prefix()+pure()+"\nprocess.stdout.write(JSON.stringify({pages:pageEntries().map(p=>({route:p.route,title:p.title,html:p.render()})),aliases:ALIASES}));"))
def build():
 m=json.loads(read('research/media.json'));logo=m['logo'];img=f'<img src="{logo["file"]}" alt="Habotrappan" width="{logo["width"]}" height="{logo["height"]}">'
 hero=node(prefix()+pure()+'\nprocess.stdout.write(hero());')
 editable=read('qa/template.html').replace('<!--__LOGO__-->',img).replace('<!--__HERO__-->',hero).replace('/*__CSS__*/',read('qa/site.css')).replace('/*__DATA__*/',prefix()).replace('/*__JS__*/',read('qa/site.js'))
 assert '/*__' not in editable
 (ROOT/'redigerbar.html').write_text(editable)
 used=sorted(set(ASSET_RE.findall(editable)))
 data={f:'data:'+(mimetypes.guess_type(f)[0] or 'application/octet-stream')+';base64,'+base64.b64encode((ROOT/f).read_bytes()).decode() for f in used}
 portable=ASSET_RE.sub(lambda m:data[m[0]],editable);assert not ASSET_RE.search(portable)
 (ROOT/'index.html').write_text(portable)
 sources=json.loads(read('research/assets.json'))
 selected=[e for e in sources if e['file'] in used]
 assert {e['file'] for e in selected}=={f for f in used if f.startswith('assets/')}
 (ROOT/'bildkallor.json').write_text(json.dumps(selected,ensure_ascii=False,indent=2))
 fonts=json.loads(read('qa/fonts.json'))
 for f in fonts:f['sha256']=hashlib.sha256((ROOT/f['file']).read_bytes()).hexdigest()
 (ROOT/'typsnitt.json').write_text(json.dumps(fonts,ensure_ascii=False,indent=2))
 inv=inventory();routes={p['route'] for p in inv['pages']};redirects={r:r for r in routes if r!='/'}|inv['aliases']
 (ROOT/'qa/routes-to-check.json').write_text(json.dumps(sorted(routes),ensure_ascii=False,indent=2))
 archive=ROOT.parent/'Habotrappan-Premium.zip'
 fixed=['index.html','redigerbar.html','LAS-MIG.md','bildkallor.json','typsnitt.json','research/facts.json','research/SOURCES.md','research/media.json','research/assets.json','research/asset-notes.md','qa/build.py','qa/verify.py','qa/site.css','qa/site.js','qa/template.html','qa/content.json','qa/fonts.json']
 fixed += [str(p.relative_to(ROOT)) for p in (ROOT/'fonts').glob('*LICENSE*')]
 with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED,compresslevel=7) as z:
  for f in fixed+used:z.write(ROOT/f,f)
  for old,target in sorted(redirects.items()):
   path=old.strip('/');url='../'*len(path.split('/'))+'redigerbar.html#'+target
   z.writestr(path+'/index.html',f'<!doctype html><html lang="sv"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta http-equiv="refresh" content="0;url={html.escape(url,quote=True)}"><title>Habotrappan</title><a href="{html.escape(url,quote=True)}">Fortsätt till sidan</a></html>')
 with zipfile.ZipFile(archive) as z:
  assert z.testzip() is None
  for f in fixed+used:assert z.read(f)==(ROOT/f).read_bytes(),f
  entries=len(z.namelist())
 result=dict(archive=str(archive),archive_bytes=archive.stat().st_size,sha256=hashlib.sha256(archive.read_bytes()).hexdigest(),entries=entries,standalone_bytes=(ROOT/'index.html').stat().st_size,editable_bytes=(ROOT/'redigerbar.html').stat().st_size,used_assets=len(used),routes=len(routes),aliases=len(redirects),crc='pass',files_match='pass')
 (ROOT/'qa/package-result.json').write_text(json.dumps(result,indent=2));print(json.dumps(result))
if __name__=='__main__':build()
