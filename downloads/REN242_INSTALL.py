# RenPyVN Studio 2.4.2 - Pair Search (upgrade only official 2.4.1)
from pathlib import Path
import ast,base64,hashlib,os,re,shutil,time,zlib

PATCH = """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"""
OLD_GUI = "2fff904a2ff9f69ad50de71bd160c9af22da1ea3935fee57defdb7b63711358f"
NEW_GUI = "7639cdda3aa014d17ed51afdaeea075542bb0aada04c5c15a2b48594062b83e9"
OLD_VERSION = b'__version__ = "2.4.1-PronounConflictReview"\n'
NEW_VERSION = b'__version__ = "2.4.2-PairSearch"\n'

def digest(data): return hashlib.sha256(data).hexdigest()

def apply_unified(source, diff):
    original=source.splitlines(keepends=True)
    lines=diff.splitlines(keepends=True)
    if len(lines)<3 or not (lines[0].startswith('--- ') and lines[1].startswith('+++ ')):
        raise ValueError('Bad patch header')
    out=[];position=0;idx=2
    while idx<len(lines):
        match=re.match(r'@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@',lines[idx])
        if not match: raise ValueError('Bad patch hunk')
        start=int(match.group(1))-1
        if start<position: raise ValueError('Overlapping patch hunks')
        out.extend(original[position:start]);position=start
        old_count=int(match.group(2) or 1);new_count=int(match.group(4) or 1)
        count_old=count_new=0;idx+=1
        while idx<len(lines) and not lines[idx].startswith('@@ '):
            item=lines[idx];idx+=1
            if not item or item[0] not in ' +-': raise ValueError('Malformed patch line')
            if item[0] in ' -':
                if position>=len(original) or original[position]!=item[1:]:
                    raise ValueError('Current source does not match patch')
                position+=1;count_old+=1
            if item[0] in ' +':out.append(item[1:]);count_new+=1
        if (count_old,count_new)!=(old_count,new_count):raise ValueError('Patch hunk length mismatch')
    out.extend(original[position:]);return ''.join(out)

def main():
    here=Path(__file__).resolve().parent
    root=next((d for d in (here,here.parent,Path.cwd()) if
        (d/'RenPyVN_Studio.exe').is_file() and (d/'renpyvn/gui.py').is_file()),None)
    if root is None:raise SystemExit('STOP: Put this installer in the application folder or downloads subfolder.')
    gui=root/'renpyvn/gui.py';version=root/'renpyvn/__init__.py'
    old_gui=gui.read_bytes();old_version=version.read_bytes()
    if digest(old_gui)==NEW_GUI and old_version==NEW_VERSION:
        print('2.4.2 already installed.');return
    if digest(old_gui)!=OLD_GUI or old_version!=OLD_VERSION:
        raise SystemExit('STOP: Requires unmodified RenPyVN 2.4.1; application files were not changed.')
    try:
        patch=zlib.decompress(base64.b64decode(PATCH,validate=True)).decode('utf8')
        new_gui=apply_unified(old_gui.decode('utf8'),patch).encode('utf8')
        if digest(new_gui)!=NEW_GUI:raise ValueError('Patched file checksum mismatch')
        ast.parse(new_gui.decode('utf8'),filename='renpyvn/gui.py')
    except (ValueError,UnicodeError,Exception) as ex:
        raise SystemExit('STOP: Patch validation failed: '+str(ex))
    backup=root/('BACKUP_BEFORE_242_'+time.strftime('%Y%m%d-%H%M%S'))/'renpyvn'
    backup.mkdir(parents=True,exist_ok=False)
    shutil.copy2(gui,backup/'gui.py');shutil.copy2(version,backup/'__init__.py')
    try:
        for path,data in ((gui,new_gui),(version,NEW_VERSION)):
            temp=path.with_name(path.name+'.242.tmp');temp.write_bytes(data);os.replace(temp,path)
    except Exception:
        shutil.copy2(backup/'gui.py',gui);shutil.copy2(backup/'__init__.py',version)
        raise
    print('RenPyVN Studio 2.4.2 installed. Backup:',backup.parent)
    print('Search only filters displayed pairs; project rules, listener JSON and progress were not modified.')

if __name__=='__main__':main()
