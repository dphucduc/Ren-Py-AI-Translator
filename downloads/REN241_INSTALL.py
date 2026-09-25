# RenPyVN Studio 2.4.1 - restore pronoun-change warning on Rule JSON import.
# Target: official 2.4.0 Smart Translation QA / GitHub patch from 2.3.6.
from pathlib import Path
import re,json,zlib,base64,hashlib,shutil,os,time,ast

PAYLOAD = "".join((Path(__file__).resolve().parent / f"REN241_PAYLOAD_{i}.txt").read_text(encoding="ascii") for i in range(1,6))
if hashlib.sha256(PAYLOAD.encode("ascii")).hexdigest() != "7d1e26a632abc41da40625625f5d56f024b2fc11678637d9d84c73956105de80":
    raise SystemExit("STOP: GitHub payload checksum mismatch. Download all five payload files.")

def sha(raw):return hashlib.sha256(raw).hexdigest()
def patch(src,diff):
    a=src.splitlines(keepends=True);d=diff.splitlines(keepends=True);out=[];j=0;i=2
    if len(d)<2 or not (d[0].startswith('--- ') and d[1].startswith('+++ ')):raise ValueError('Bad header')
    while i<len(d):
        m=re.match(r'@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@',d[i])
        if not m:raise ValueError('Bad diff hunk')
        start=int(m.group(1))-1;oc=nc=0;i+=1
        if start<j:raise ValueError('Overlapping hunks')
        out.extend(a[j:start]);j=start
        old_count=int(m.group(2) or 1);new_count=int(m.group(4) or 1)
        while i<len(d) and not d[i].startswith('@@ '):
            line=d[i];i+=1
            if not line or line[0] not in ' +-':raise ValueError('Bad diff line')
            if line[0]==' ':
                if j>=len(a) or a[j]!=line[1:]:raise ValueError('Context mismatch')
                out.append(a[j]);j+=1;oc+=1;nc+=1
            elif line[0]=='-':
                if j>=len(a) or a[j]!=line[1:]:raise ValueError('Remove mismatch')
                j+=1;oc+=1
            else:out.append(line[1:]);nc+=1
        if oc!=old_count or nc!=new_count:raise ValueError('Line count mismatch')
    return ''.join(out+a[j:])

here=Path(__file__).resolve().parent
root=next((x for x in (here,here.parent,Path.cwd()) if
           (x/'RenPyVN_Studio.exe').is_file() and (x/'renpyvn/external_rules.py').is_file()),None)
if root is None:raise SystemExit('STOP: Copy this file into the folder with RenPyVN_Studio.exe and renpyvn, then run via runtime\\python.exe.')
data=json.loads(zlib.decompress(base64.b64decode(PAYLOAD)).decode('utf8'))
manifest=json.loads(data.pop('manifest.json'))
changes={}
for rel,checks in manifest.items():
    dest=root/rel
    if not dest.is_file():raise SystemExit('STOP: Missing '+rel)
    old=dest.read_bytes();current=sha(old)
    if current==checks['new']:continue
    if current!=checks['old']:raise SystemExit('STOP: Custom/different app source: '+rel+'; no files changed.')
    modified=patch(old.decode('utf8'),data[Path(rel).name+'.diff']).encode('utf8')
    if sha(modified)!=checks['new']:raise SystemExit('STOP: Checksum mismatch: '+rel)
    ast.parse(modified.decode('utf8'),filename=rel)
    changes[rel]=modified
if not changes:print('2.4.1 already installed.');raise SystemExit(0)
backup=root/('BACKUP_BEFORE_241_'+time.strftime('%Y%m%d-%H%M%S'))
for rel in changes:
    dest=backup/rel;dest.parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(root/rel,dest)
for rel,new in changes.items():
    dest=root/rel;temp=dest.with_name(dest.name+'.241.tmp')
    temp.write_bytes(new);os.replace(temp,dest)
print('RenPyVN 2.4.1 INSTALLED. Code backup:',backup)
print('Project rules.json, progress.sqlite3 and game scripts were not touched.')
