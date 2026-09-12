"""Candidate packaging: reuse accepted B1 exact Git-blob export."""
import argparse, hashlib, io, json, pathlib, re, subprocess, tarfile

parser = argparse.ArgumentParser()
parser.add_argument("commit")
args = parser.parse_args()
assert re.fullmatch(r"[0-9a-f]{40}", args.commit), "full commit required"
SHA = args.commit
REPO = pathlib.Path(__file__).resolve().parents[2] / "omniroute-auto-switch-runtime-20260912"
OUT = pathlib.Path(__file__).resolve().parent / "auto-switch-build-20260912" / SHA
OUT.mkdir(parents=True, exist_ok=False)

def git(*args):
    return subprocess.check_output(['git', '-C', str(REPO), *args])
assert git('rev-parse', 'HEAD').decode().strip() == SHA
assert not git('status', '--porcelain')
assert not (OUT / 'source.tar').exists()
roots = {'src', 'open-sse', 'scripts', 'public', 'docs', 'config', 'bin', '@omniroute', 'skills'}
rootfiles = {'.dockerignore', '.npmrc', '.node-version', '.nvmrc', 'Dockerfile', 'LICENSE', 'README.md'}
forbidden = {'.git', '.superpowers', '.worktrees', '.planning', 'node_modules', '.next', '.build', '.ssh', 'data', 'logs', 'handoffs', 'evidence', 'test-results'}
rows = []
excluded = []
for record in git('ls-tree', '-rz', SHA).split(b'\0'):
    if not record:
        continue
    meta, pathraw = record.split(b'\t', 1)
    mode, kind, oid = meta.decode().split()
    name = pathraw.decode()
    p = pathlib.PurePosixPath(name)
    selected = p.parts[0] in roots or name in rootfiles or (len(p.parts) == 1 and p.suffix in {'.json', '.mjs', '.ts'})
    selected = selected and not any(x in forbidden for x in p.parts)
    selected = selected and not any(x.startswith('.env') for x in p.parts)
    selected = selected and not name.startswith(('docs/i18n/', 'docs/routing-completion-report-', 'docs/tls-native-build-fix-report-', 'docs/docker-bundler-override-report-', 'docs/plans/', 'docs/research/'))
    selected = selected and not re.search(r'\.(sqlite(?:-\w+)?|db|pem|key|p12|pfx|log|tar|tgz|zip)$', name, re.I)
    if not selected:
        excluded.append(name)
        continue
    assert not p.is_absolute() and '..' not in p.parts and '\\' not in name and ':' not in name
    assert kind == 'blob' and mode in {'100644', '100755'}, 'nonregular archive entry: ' + name
    rows.append((mode, oid, name))
batch = subprocess.Popen(['git', '-C', str(REPO), 'cat-file', '--batch'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
manifest = []
suspects = []
secret = re.compile(rb'-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----|\bAKIA[A-Z0-9]{16}\b|\bgh[pousr]_[A-Za-z0-9]{30,}\b|\bsk-(?:proj-|or-v1-)[A-Za-z0-9_-]{40,}')
with tarfile.open(OUT / 'source.tar', 'w', format=tarfile.PAX_FORMAT) as archive:
    for mode, oid, name in rows:
        batch.stdin.write((oid + '\n').encode()); batch.stdin.flush()
        header = batch.stdout.readline().decode().split()
        assert header[0] == oid and header[1] == 'blob'
        data = batch.stdout.read(int(header[2])); assert batch.stdout.read(1) == b'\n'
        if secret.search(data): suspects.append(name)
        member = tarfile.TarInfo(name)
        member.size = len(data); member.mode = int(mode, 8) & 0o777; member.mtime = 0
        member.uid = member.gid = 0
        archive.addfile(member, io.BytesIO(data))
        manifest.append({'path': name, 'git_blob': oid, 'mode': mode, 'sha256': hashlib.sha256(data).hexdigest()})
batch.stdin.close(); batch.wait(); assert batch.returncode == 0
(OUT / 'source-manifest.json').write_text(json.dumps({'commit': SHA, 'files': manifest, 'excluded': excluded}, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'selected': len(rows), 'excluded': len(excluded), 'archive_bytes': (OUT / 'source.tar').stat().st_size, 'archive_sha256': hashlib.sha256((OUT / 'source.tar').read_bytes()).hexdigest(), 'secret_pattern_paths': suspects}))
assert not suspects, 'content scanner found possible credentials; do not transfer archive'
with tarfile.open(OUT / 'source.tar') as archive:
    assert [x.name for x in archive] == [x[2] for x in rows]
assert git('rev-parse', 'HEAD').decode().strip() == SHA and not git('status', '--porcelain')
