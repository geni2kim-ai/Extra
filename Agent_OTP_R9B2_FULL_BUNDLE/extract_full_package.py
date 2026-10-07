#!/usr/bin/env python3
from pathlib import Path
import base64,gzip,hashlib,io,json,tarfile
HERE=Path(__file__).resolve().parent
m=json.loads((HERE/'PACKAGE_MANIFEST.json').read_text(encoding='utf-8'))
parts=[]
for i in range(m['part_count']):
    parts.append((HERE/f"payload.b64.part{i:02d}").read_text(encoding='ascii').strip())
gz=base64.b64decode(''.join(parts),validate=True)
if hashlib.sha256(gz).hexdigest()!=m['archive_sha256']:
    raise SystemExit('ARCHIVE_SHA256_MISMATCH')
tar=gzip.decompress(gz)
if hashlib.sha256(tar).hexdigest()!=m['tar_sha256']:
    raise SystemExit('TAR_SHA256_MISMATCH')
out=HERE/'reconstructed'
out.mkdir(exist_ok=True)
with tarfile.open(fileobj=io.BytesIO(tar),mode='r:') as tf:
    for member in tf.getmembers():
        target=(out/member.name).resolve()
        if out.resolve() not in target.parents and target!=out.resolve():
            raise SystemExit('UNSAFE_ARCHIVE_PATH')
    tf.extractall(out)
print(out/'Agent_OTP_R9B2_FULL')
