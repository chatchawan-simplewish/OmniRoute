"""Create one offline OmniRoute candidate from a native SQLite clone.

Preparation only until exact bytes and the completed R4 transfer result receive
independent review. Secret values stay inside the remote root process and the
candidate's private server.env.
"""
import ast
import base64
import hashlib
import importlib.util
import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "docs/auto-switch-candidate-start-contract-20260912.md"
BINDINGS = ROOT / "docs/auto-switch-bindings-candidate-20260912.json"
TRANSFER_RESULT = ROOT / "docs/auto-switch-image-transfer-result-r4-20260912.md"
HELPER = ROOT / "scripts/auto-switch-image-transfer-20260912.py"
HELPER_HASH = "7776a680ade8940ece3a47dc5feb154e0ef27209a07897674d309ea6f7822279"
BINDINGS_HASH = "c30aa56eba04d15a50c766a20ba44e88792c60bcddbdf25670fafd5955286e58"
TRANSFER_RESULT_HASH = "4b0eda575ecf465d184c654e95ed5eee58e2ebfa4696797236bba3e5d2f05736"
SOURCE = "dc53bcfed67b3bbea7d2fbf82468342e573dadb3"
CANDIDATE_IID = "sha256:a91994bf883698d4520ff048d16be999d4614331a528c76c0b95bc6dc8bec803"
CANDIDATE_TAG = "omniroute-auto-switch-r2:" + SOURCE

REMOTE_TEMPLATE = r'''
import base64,hashlib,json,os,pathlib,re,sqlite3,stat,subprocess,time,urllib.parse

LIVE_NAME='omniroute'
LIVE_ID='7b20ca195e3c9e875d0a1ce98832ca469c2a114886335b8466b1467b3ed139bc'
LIVE_IMAGE='sha256:60ab56311d1c9873416dc53683148d314465370312547b8ce87c442ce084c6a5'
LIVE_VOLUME='omniroute-data-mcp-audit-20260910-r3'
SOURCE='dc53bcfed67b3bbea7d2fbf82468342e573dadb3'
CANDIDATE_IID='sha256:a91994bf883698d4520ff048d16be999d4614331a528c76c0b95bc6dc8bec803'
CANDIDATE_TAG='omniroute-auto-switch-r2:'+SOURCE
CANDIDATE_NAME='omniroute-auto-switch-candidate-20260912'
CANDIDATE_VOLUME='omniroute-auto-switch-candidate-data-20260912'
BINDINGS=json.loads(base64.b64decode('__BINDINGS_B64__',validate=True))
STAGES={'preflight','live_identity','image_prerequisite','secret_sources','clone_absence',
        'volume_create','volume_identity','sqlite_backup','clone_cloud','candidate_secret_file',
        'container_create','container_identity','container_start','server_health','post_start_sql'}
stage='preflight'
candidate_id=None

class Stop(Exception): pass

def run(args,payload=None,timeout=30):
 r=subprocess.run(args,input=payload,capture_output=True,timeout=timeout)
 if r.returncode: raise Stop()
 return r.stdout

def docker(args,payload=None,timeout=30): return run(['docker',*args],payload,timeout)

def one_json(raw):
 value=json.loads(raw)
 if not isinstance(value,list) or len(value)!=1 or not isinstance(value[0],dict): raise Stop()
 return value[0]

def env_map(rows):
 if not isinstance(rows,list): raise Stop()
 out={}
 for row in rows:
  if not isinstance(row,str) or '=' not in row: raise Stop()
  key,value=row.split('=',1)
  if not key or key in out: raise Stop()
  out[key]=value
 return out

def exact_secret(value):
 if not isinstance(value,str) or not value or value!=value.strip() or '\n' in value or '\r' in value: raise Stop()
 return value

def safe_dir(path):
 path=pathlib.Path(path)
 item=os.lstat(path)
 if not stat.S_ISDIR(item.st_mode) or stat.S_ISLNK(item.st_mode) or pathlib.Path(os.path.realpath(path))!=path: raise Stop()
 return path

def read_regular(path,limit):
 path=pathlib.Path(path)
 before=os.lstat(path)
 if not stat.S_ISREG(before.st_mode) or stat.S_ISLNK(before.st_mode) or before.st_size>limit: raise Stop()
 if pathlib.Path(os.path.realpath(path))!=path: raise Stop()
 fd=os.open(path,os.O_RDONLY|os.O_NOFOLLOW)
 try:
  opened=os.fstat(fd)
  if (opened.st_dev,opened.st_ino,opened.st_size)!=(before.st_dev,before.st_ino,before.st_size): raise Stop()
  chunks=[]; total=0
  while True:
   raw=os.read(fd,min(4096,limit+1-total))
   if not raw: break
   total+=len(raw)
   if total>limit: raise Stop()
   chunks.append(raw)
  after=os.fstat(fd)
  if (after.st_dev,after.st_ino,after.st_size,after.st_mtime_ns)!=(opened.st_dev,opened.st_ino,opened.st_size,opened.st_mtime_ns): raise Stop()
  return b''.join(chunks)
 finally: os.close(fd)

def parse_env(raw):
 result={}
 for line in raw.decode('utf8').splitlines():
  value=line.strip()
  if not value or value.startswith('#') or '=' not in value: continue
  key,item=value.split('=',1); key=key.strip(); item=item.strip()
  if len(item)>=2 and item[0] in ('\"',"'") and item[-1]==item[0]: item=item[1:-1]
  result[key]=item
 return result

def volume(name): return one_json(docker(['volume','inspect',name]))

def db_uri(path): return 'file:'+urllib.parse.quote(str(path),safe='/')+'?mode=ro'

def db_stats(path,require_cloud):
 db=sqlite3.connect(db_uri(path),uri=True,timeout=10)
 try:
  db.execute('PRAGMA query_only=ON'); db.execute('BEGIN')
  if db.execute('PRAGMA quick_check').fetchall()!=[('ok',)]: raise Stop()
  columns={row[1] for row in db.execute('PRAGMA table_info(provider_connections)')}
  fields=['api_key','access_token','refresh_token','id_token']
  if not set(fields).issubset(columns): raise Stop()
  encrypted=plain=empty=providers=0
  for row in db.execute('SELECT '+','.join(fields)+' FROM provider_connections'):
   providers+=1
   for value in row:
    if value is None or value=='': empty+=1
    elif isinstance(value,str) and value.startswith('enc:v1:'): encrypted+=1
    else: plain+=1
  cloud=db.execute("SELECT value FROM key_value WHERE namespace='settings' AND key='cloudEnabled'").fetchall()
  cloud_false=len(cloud)==1 and json.loads(cloud[0][0]) is False
  if require_cloud and not cloud_false: raise Stop()
  result={'provider_rows':providers,'encrypted_fields':encrypted,'plain_fields':plain,'empty_fields':empty,
          'key_value_rows':db.execute('SELECT count(*) FROM key_value').fetchone()[0],
          'user_version':db.execute('PRAGMA user_version').fetchone()[0],'cloud_false':cloud_false}
  db.execute('ROLLBACK')
  return result
 finally: db.close()

def missing_container(name):
 names=docker(['container','ls','--all','--format','{{.Names}}']).decode().splitlines()
 if name in names: raise Stop()

def missing_volume(name):
 names=docker(['volume','ls','--format','{{.Name}}']).decode().splitlines()
 if name in names: raise Stop()

def inspect_candidate():
 row=one_json(docker(['container','inspect',CANDIDATE_NAME]))
 if row['Id']!=candidate_id or row['Image']!=CANDIDATE_IID or row['Name']!='/'+CANDIDATE_NAME: raise Stop()
 host=row['HostConfig']
 if host['NetworkMode']!='none' or host['ReadonlyRootfs'] is not True or host['RestartPolicy']['Name']!='no': raise Stop()
 if host.get('CapDrop')!=['ALL'] or 'no-new-privileges' not in (host.get('SecurityOpt') or []): raise Stop()
 if host.get('PortBindings') not in (None,{}): raise Stop()
 tmpfs=host.get('Tmpfs') or {}
 options=set((tmpfs.get('/tmp') or '').split(','))
 if not {'rw','noexec','nosuid','nodev','size=67108864','mode=1777'}.issubset(options): raise Stop()
 mounts=[m for m in row['Mounts'] if m['Destination']=='/app/data']
 if len(row['Mounts'])!=1 or len(mounts)!=1 or mounts[0]['Type']!='volume' or mounts[0]['Name']!=CANDIDATE_VOLUME: raise Stop()
 if row['Config']['User']!='node': raise Stop()
 effective=env_map(row['Config']['Env'])
 fixed={'DATA_DIR':'/app/data','OMNIROUTE_AGENT_ROUTE_BINDINGS_JSON':json.dumps(BINDINGS,separators=(',',':'),sort_keys=True),
        'OMNIROUTE_DISABLE_BACKGROUND_SERVICES':'1','OMNIROUTE_DISABLE_CREDENTIAL_HEALTH_CHECK':'1',
        'PROXY_HEALTH_ENABLED':'false','FREE_PROXY_AUTO_SYNC_ENABLED':'false','OMNIROUTE_ENABLE_LIVE_WS':'0',
        'OMNIROUTE_DB_HEALTHCHECK_INTERVAL_MS':'0','OMNIROUTE_WAL_TRUNCATE_INTERVAL_MS':'0'}
 for key,value in fixed.items():
  if effective.get(key)!=value: raise Stop()
 denied_exact={'STORAGE_ENCRYPTION_KEY','STORAGE_ENCRYPTION_KEY_VERSION','JWT_SECRET','API_KEY_SECRET',
               'CLOUD_URL','NEXT_PUBLIC_CLOUD_URL','OMNIROUTE_CLOUD_SYNC_SECRETS','INITIAL_PASSWORD',
               'HTTP_PROXY','HTTPS_PROXY','ALL_PROXY','NO_PROXY','http_proxy','https_proxy','all_proxy','no_proxy',
               'OMNIROUTE_API_KEY','ROUTER_API_KEY','REDIS_URL'}
 denied_prefix=('OPENAI_','OPENROUTER_','ANTHROPIC_','CLAUDE_','CODEX_','GEMINI_','GOOGLE_','AZURE_','AWS_',
                'QDRANT_','BIFROST_')
 if any(key in denied_exact or key.startswith(denied_prefix) for key in effective): raise Stop()
 return row

def stop_candidate():
 if not candidate_id: return True
 try:
  row=one_json(docker(['container','inspect',CANDIDATE_NAME]))
  if row['Id']!=candidate_id or row['Image']!=CANDIDATE_IID: return False
  if row['State']['Running']:
   docker(['container','stop','--time','10',CANDIDATE_NAME],timeout=20)
  row=one_json(docker(['container','inspect',CANDIDATE_NAME]))
  return row['Id']==candidate_id and row['State']['Running'] is False
 except Exception: return False

try:
 stage='live_identity'
 live=one_json(docker(['container','inspect',LIVE_NAME]))
 if live['Id']!=LIVE_ID or live['Image']!=LIVE_IMAGE or live['State']['Running'] is not True: raise Stop()
 mounts=[m for m in live['Mounts'] if m['Destination']=='/app/data']
 if len(mounts)!=1 or mounts[0]['Type']!='volume' or mounts[0]['Name']!=LIVE_VOLUME: raise Stop()
 live_env=env_map(live['Config']['Env'])
 if live_env.get('STORAGE_ENCRYPTION_KEY','').strip(): raise Stop()

 stage='image_prerequisite'
 image=one_json(docker(['image','inspect',CANDIDATE_TAG]))
 if image['Id']!=CANDIDATE_IID or image.get('RepoTags')!=[CANDIDATE_TAG]: raise Stop()
 if image.get('Os')!='linux' or image.get('Architecture')!='amd64' or image['Config'].get('User')!='node': raise Stop()
 if (image['Config'].get('Labels') or {}).get('org.opencontainers.image.revision')!=SOURCE: raise Stop()
 image_env=env_map(image['Config']['Env'])
 fixed_names={'DATA_DIR','OMNIROUTE_AGENT_ROUTE_BINDINGS_JSON','OMNIROUTE_DISABLE_BACKGROUND_SERVICES',
              'OMNIROUTE_DISABLE_CREDENTIAL_HEALTH_CHECK','PROXY_HEALTH_ENABLED','FREE_PROXY_AUTO_SYNC_ENABLED',
              'OMNIROUTE_ENABLE_LIVE_WS','OMNIROUTE_DB_HEALTHCHECK_INTERVAL_MS','OMNIROUTE_WAL_TRUNCATE_INTERVAL_MS'}
 denied={'STORAGE_ENCRYPTION_KEY','STORAGE_ENCRYPTION_KEY_VERSION','JWT_SECRET','API_KEY_SECRET','CLOUD_URL',
         'NEXT_PUBLIC_CLOUD_URL','OMNIROUTE_CLOUD_SYNC_SECRETS','INITIAL_PASSWORD','HTTP_PROXY','HTTPS_PROXY',
         'ALL_PROXY','NO_PROXY','http_proxy','https_proxy','all_proxy','no_proxy','OMNIROUTE_API_KEY',
         'ROUTER_API_KEY','REDIS_URL'}
 prefixes=('OPENAI_','OPENROUTER_','ANTHROPIC_','CLAUDE_','CODEX_','GEMINI_','GOOGLE_','AZURE_','AWS_','QDRANT_','BIFROST_')
 if any(k in denied or k.startswith(prefixes) for k in image_env): raise Stop()

 stage='secret_sources'
 jwt=exact_secret(live_env.get('JWT_SECRET'))
 api=exact_secret(live_env.get('API_KEY_SECRET'))
 source_volume=volume(LIVE_VOLUME)
 if (source_volume.get('Name')!=LIVE_VOLUME or source_volume.get('Driver')!='local'
     or source_volume.get('Scope')!='local'): raise Stop()
 source_root=safe_dir(source_volume['Mountpoint'])
 persisted=parse_env(read_regular(source_root/'server.env',65536))
 storage=exact_secret(persisted.get('STORAGE_ENCRYPTION_KEY'))
 version=persisted.get('STORAGE_ENCRYPTION_KEY_VERSION')
 if version is not None and version!='': version=exact_secret(version)
 else: version=None

 stage='clone_absence'
 missing_container(CANDIDATE_NAME); missing_volume(CANDIDATE_VOLUME)

 stage='volume_create'
 created=docker(['volume','create','--driver','local','--label','com.simplewish.purpose=omniroute-auto-switch-candidate',CANDIDATE_VOLUME]).decode().strip()
 if created!=CANDIDATE_VOLUME: raise Stop()

 stage='volume_identity'
 target_volume=volume(CANDIDATE_VOLUME)
 if target_volume['Name']!=CANDIDATE_VOLUME or target_volume['Driver']!='local': raise Stop()
 target_root=safe_dir(target_volume['Mountpoint'])
 if list(target_root.iterdir()): raise Stop()
 os.chown(target_root,1000,1000); os.chmod(target_root,0o700)
 if (os.stat(target_root).st_uid,os.stat(target_root).st_gid,stat.S_IMODE(os.stat(target_root).st_mode))!=(1000,1000,0o700): raise Stop()

 stage='sqlite_backup'
 source_db=source_root/'storage.sqlite'; target_db=target_root/'storage.sqlite'
 source_stat=os.lstat(source_db)
 if not stat.S_ISREG(source_stat.st_mode) or stat.S_ISLNK(source_stat.st_mode) or pathlib.Path(os.path.realpath(source_db))!=source_db: raise Stop()
 source=sqlite3.connect(db_uri(source_db),uri=True,timeout=20)
 target=sqlite3.connect(target_db,timeout=20)
 try:
  source.execute('PRAGMA query_only=ON')
  if source.execute('PRAGMA quick_check').fetchall()!=[('ok',)]: raise Stop()
  source.backup(target)
  target.commit()
 finally:
  target.close(); source.close()
 os.chown(target_db,1000,1000); os.chmod(target_db,0o600)

 stage='clone_cloud'
 clone=sqlite3.connect(target_db,timeout=20)
 try:
  clone.execute('BEGIN IMMEDIATE')
  clone.execute("INSERT OR REPLACE INTO key_value(namespace,key,value) VALUES('settings','cloudEnabled','false')")
  clone.commit()
 finally: clone.close()
 before=db_stats(target_db,True)
 if before['encrypted_fields']!=18 or before['plain_fields']!=0 or before['empty_fields']!=34: raise Stop()

 stage='candidate_secret_file'
 secret_path=target_root/'server.env'
 values={'STORAGE_ENCRYPTION_KEY':storage,'JWT_SECRET':jwt,'API_KEY_SECRET':api}
 if version: values['STORAGE_ENCRYPTION_KEY_VERSION']=version
 payload=('\n'.join(key+"='"+value+"'" for key,value in values.items())+'\n').encode('utf8')
 fd=os.open(secret_path,os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW,0o600)
 try:
  if os.write(fd,payload)!=len(payload): raise Stop()
  os.fsync(fd); os.fchmod(fd,0o600); os.fchown(fd,1000,1000)
  info=os.fstat(fd)
  if not stat.S_ISREG(info.st_mode) or info.st_uid!=1000 or info.st_gid!=1000 or stat.S_IMODE(info.st_mode)!=0o600: raise Stop()
 finally: os.close(fd)
 if {k:parse_env(read_regular(secret_path,65536)).get(k) for k in values}!=values: raise Stop()
 del payload,storage,jwt,api,persisted,values

 stage='container_create'
 fixed={'DATA_DIR':'/app/data','OMNIROUTE_AGENT_ROUTE_BINDINGS_JSON':json.dumps(BINDINGS,separators=(',',':'),sort_keys=True),
        'OMNIROUTE_DISABLE_BACKGROUND_SERVICES':'1','OMNIROUTE_DISABLE_CREDENTIAL_HEALTH_CHECK':'1',
        'PROXY_HEALTH_ENABLED':'false','FREE_PROXY_AUTO_SYNC_ENABLED':'false','OMNIROUTE_ENABLE_LIVE_WS':'0',
        'OMNIROUTE_DB_HEALTHCHECK_INTERVAL_MS':'0','OMNIROUTE_WAL_TRUNCATE_INTERVAL_MS':'0'}
 args=['container','create','--name',CANDIDATE_NAME,'--user','node','--network','none','--read-only',
       '--tmpfs','/tmp:rw,noexec,nosuid,nodev,size=67108864,mode=1777','--cap-drop','ALL',
       '--security-opt','no-new-privileges','--restart','no','--mount',
       'type=volume,src='+CANDIDATE_VOLUME+',dst=/app/data']
 for key in sorted(fixed): args.extend(['--env',key+'='+fixed[key]])
 raw=docker([*args,CANDIDATE_TAG],timeout=60).decode().strip()
 if not re.fullmatch(r'[0-9a-f]{64}',raw): raise Stop()
 candidate_id=raw

 stage='container_identity'
 inspect_candidate()

 stage='container_start'
 if docker(['container','start',CANDIDATE_NAME],timeout=60).decode().strip()!=CANDIDATE_NAME: raise Stop()

 stage='server_health'
 healthy=False
 for _ in range(30):
  check=subprocess.run(['docker','exec','--user','node',CANDIDATE_NAME,'node','healthcheck.mjs'],capture_output=True,timeout=10)
  if check.returncode==0: healthy=True; break
  time.sleep(2)
 if not healthy: raise Stop()
 running=inspect_candidate()
 if running['State']['Running'] is not True: raise Stop()

 stage='post_start_sql'
 after=db_stats(target_db,True)
 for key in ('provider_rows','encrypted_fields','plain_fields','empty_fields'):
  if after[key]!=before[key]: raise Stop()
 result={'status':'CANDIDATE_START_PASS','candidate_id':candidate_id,'candidate_image':CANDIDATE_IID,
         'candidate_volume':CANDIDATE_VOLUME,'network_none':True,'published_ports':0,'health':True,
         'cloud_false':True,'db_bytes':os.stat(target_db).st_size,
         'provider_rows':after['provider_rows'],'encrypted_fields':after['encrypted_fields'],
         'plain_fields':after['plain_fields'],'empty_fields':after['empty_fields'],
         'key_value_rows_before':before['key_value_rows'],'key_value_rows_after':after['key_value_rows'],
         'user_version_before':before['user_version'],'user_version_after':after['user_version']}
 print(json.dumps(result,sort_keys=True))
except Exception:
 stopped=stop_candidate()
 print(json.dumps({'status':'CANDIDATE_START_STOP','stage':stage if stage in STAGES else 'preflight',
                   'candidate_stopped':stopped},sort_keys=True))
 raise SystemExit(1)
'''


def digest(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def regular(path):
    return path.is_file() and not path.is_symlink()


def offline_check():
    assert regular(BINDINGS) and digest(BINDINGS) == BINDINGS_HASH
    bindings = json.loads(BINDINGS.read_text(encoding="utf-8"))
    assert isinstance(bindings, dict) and REMOTE_TEMPLATE.count("__BINDINGS_B64__") == 1
    payload = REMOTE_TEMPLATE.replace(
        "__BINDINGS_B64__", base64.b64encode(json.dumps(bindings).encode("utf-8")).decode("ascii")
    )
    ast.parse(payload)
    assert "--network','none" in payload and "container','create" in payload
    assert "source_volume.get('Name')!=LIVE_VOLUME" in payload
    assert "source_volume.get('Driver')!='local'" in payload
    assert "source_volume.get('Scope')!='local'" in payload
    assert "container','rm" not in payload and "volume','rm" not in payload
    print("CANDIDATE_START_OFFLINE_CHECK_PASS")


def validate_result(value, returncode):
    if returncode:
        assert isinstance(value, dict) and set(value) == {"status", "stage", "candidate_stopped"}
        assert value["status"] == "CANDIDATE_START_STOP" and value["stage"] in {
            "preflight", "live_identity", "image_prerequisite", "secret_sources", "clone_absence",
            "volume_create", "volume_identity", "sqlite_backup", "clone_cloud",
            "candidate_secret_file", "container_create", "container_identity", "container_start",
            "server_health", "post_start_sql",
        }
        assert type(value["candidate_stopped"]) is bool
        return value
    fields = {
        "status", "candidate_id", "candidate_image", "candidate_volume", "network_none",
        "published_ports", "health", "cloud_false", "db_bytes", "provider_rows",
        "encrypted_fields", "plain_fields", "empty_fields", "key_value_rows_before",
        "key_value_rows_after", "user_version_before", "user_version_after",
    }
    assert isinstance(value, dict) and set(value) == fields and value["status"] == "CANDIDATE_START_PASS"
    assert re.fullmatch(r"[0-9a-f]{64}", value["candidate_id"])
    assert value["candidate_image"] == CANDIDATE_IID
    assert value["candidate_volume"] == "omniroute-auto-switch-candidate-data-20260912"
    assert value["network_none"] is True and value["health"] is True and value["cloud_false"] is True
    assert value["published_ports"] == 0 and value["plain_fields"] == 0
    numeric = fields - {"status", "candidate_id", "candidate_image", "candidate_volume",
                        "network_none", "health", "cloud_false"}
    assert all(type(value[key]) is int and value[key] >= 0 for key in numeric)
    return value


def main():
    if sys.argv[1:] == ["--self-check"]:
        offline_check()
        return 0
    assert len(sys.argv) == 2
    pins_path = pathlib.Path(sys.argv[1])
    pins = json.loads(pins_path.read_text(encoding="utf-8"))
    assert set(pins) == {"launcher_sha256", "contract_sha256", "helper_sha256",
                         "bindings_sha256", "transfer_result_sha256"}
    assert pins["launcher_sha256"] == digest(pathlib.Path(__file__))
    assert regular(CONTRACT) and pins["contract_sha256"] == digest(CONTRACT)
    assert regular(HELPER) and pins["helper_sha256"] == HELPER_HASH == digest(HELPER)
    assert regular(BINDINGS) and pins["bindings_sha256"] == BINDINGS_HASH == digest(BINDINGS)
    assert regular(TRANSFER_RESULT) and re.fullmatch(r"[0-9a-f]{64}", pins["transfer_result_sha256"])
    assert pins["transfer_result_sha256"] == TRANSFER_RESULT_HASH == digest(TRANSFER_RESULT)
    transfer_text = TRANSFER_RESULT.read_text(encoding="utf-8")
    assert "IMAGE_TRANSFER_R4_PASS" in transfer_text and CANDIDATE_IID in transfer_text and CANDIDATE_TAG in transfer_text
    spec = importlib.util.spec_from_file_location("transport", HELPER)
    transport = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(transport)
    bindings = json.loads(BINDINGS.read_text(encoding="utf-8"))
    assert REMOTE_TEMPLATE.count("__BINDINGS_B64__") == 1
    payload = REMOTE_TEMPLATE.replace(
        "__BINDINGS_B64__", base64.b64encode(json.dumps(bindings).encode("utf-8")).decode("ascii")
    ).encode("utf-8")
    result = subprocess.run(
        [transport.SSH, "-T", *transport.options("192.168.1.68"), "belladmin@192.168.1.68", "sudo -n python3 -"],
        input=payload, capture_output=True, timeout=300,
    )
    value = validate_result(json.loads(result.stdout), result.returncode)
    print(json.dumps(value, sort_keys=True))
    return 1 if result.returncode else 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception:
        print(json.dumps({"status": "CANDIDATE_START_STOP", "stage": "local_validation", "candidate_stopped": True}))
        raise SystemExit(1)
