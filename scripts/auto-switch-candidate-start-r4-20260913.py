"""Prepare one bounded offline OmniRoute R4 candidate from a native SQLite clone.

Preparation only until exact bytes and the completed R3 transfer result receive
independent review. Secret values stay inside the remote root process and the
candidate's private server.env.
"""
import ast
import base64
import hashlib
import importlib.util
import inspect
import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
COORDINATOR_ROOT = pathlib.Path(r"C:\ChatGPT Projects\SW-Selfhosted-Network\.worktrees\omniroute-auto-switch-20260912")
CONTRACT = ROOT / "docs/auto-switch-candidate-start-r4-contract-20260913.md"
BINDINGS = COORDINATOR_ROOT / "docs/auto-switch-bindings-candidate-20260912.json"
TRANSFER_RESULT = COORDINATOR_ROOT / "docs/auto-switch-image-transfer-r3-result-20260913.md"
R1_START_RESULT = COORDINATOR_ROOT / "docs/auto-switch-candidate-start-result-20260912.md"
R1_DIAGNOSIS_RESULT = COORDINATOR_ROOT / "docs/auto-switch-candidate-diagnosis-v2-result-20260912.md"
R2_START_RESULT = COORDINATOR_ROOT / "docs/auto-switch-candidate-start-r2-result-20260912.md"
R3_START_RESULT = COORDINATOR_ROOT / "docs/auto-switch-candidate-start-r3-result-20260912.md"
ROOT_CAUSE_RESULT = COORDINATOR_ROOT / "docs/auto-switch-candidate-start-root-cause-20260912.md"
TRANSPORT_HELPER = COORDINATOR_ROOT / "scripts/auto-switch-image-transfer-r3-20260913.py"
TRANSPORT_HELPER_HASH = "78bb97e57d6229aae84c2f0d0caaf68eeb71ba6b92e69415d83af2a869b8224a"
BINDINGS_HASH = "c30aa56eba04d15a50c766a20ba44e88792c60bcddbdf25670fafd5955286e58"
TRANSFER_RESULT_HASH = "1146ddb26372878193223babc726db9764f367d41604660760b0640f6003261f"
R1_START_RESULT_HASH = "cd9dcb70213a9280859e15e1ef06054623ef1cd9559eb5b276773227018ecf48"
R1_DIAGNOSIS_RESULT_HASH = "0cf8c9052fc90a9f3e3613bd96cce0c6c71c50b72ebb075a1f63a3ce462481f0"
R2_START_RESULT_HASH = "5a3a134390414f34f8670c39361926c6463aa46f6d5b60781099020c70ef2535"
R3_START_RESULT_HASH = "be622186c4f63a901d626f0ca7e7e5442ebc418e0babc3458874189d37c72aad"
ROOT_CAUSE_RESULT_HASH = "4332de225d868dc78b382c604f678d3b2c5a7d07c3d6af6ee287b70892b195a5"
SOURCE = "e53d895e9a5e38a7f06ce59de254835f10e829c1"
CANDIDATE_IID = "sha256:8211e1071a3b68eac01673d76129150eb0c0fea329dd222bc8bf0394b13fc844"
CANDIDATE_TAG = "omniroute-auto-switch-r3:" + SOURCE
STARTUP_DEADLINE_SECONDS = 180
PROBE_TIMEOUT_SECONDS = 15
TIMEOUT_COOLDOWN_SECONDS = 12
STOP_TIMEOUT_SECONDS = 20
TRANSPORT_TIMEOUT_SECONDS = 480


class Stop(Exception):
    pass


REMOTE_TEMPLATE = r'''
import base64,hashlib,json,os,pathlib,re,sqlite3,stat,subprocess,threading,time,urllib.parse
__BOUNDED_CAPTURE__

LIVE_NAME='omniroute'
LIVE_ID='7b20ca195e3c9e875d0a1ce98832ca469c2a114886335b8466b1467b3ed139bc'
LIVE_IMAGE='sha256:60ab56311d1c9873416dc53683148d314465370312547b8ce87c442ce084c6a5'
LIVE_VOLUME='omniroute-data-mcp-audit-20260910-r3'
RETAINED_R1_ID='a710a83e3310cb40c41fba7fba49e5fe700cde84a26b431c919f5570d549d164'
RETAINED_R1_NAME='omniroute-auto-switch-candidate-20260912'
RETAINED_R1_VOLUME='omniroute-auto-switch-candidate-data-20260912'
RETAINED_R2_ID='e55a92e3645f899b4f59516c7227b9cb859138a8237a838ac0f057c5c4bc2827'
RETAINED_R2_NAME='omniroute-auto-switch-candidate-r2-20260912'
RETAINED_R2_VOLUME='omniroute-auto-switch-candidate-data-r2-20260912'
RETAINED_R3_ID='6b1089d2b14c175448ca48437e63a7ea0f880deb6374eee26ebf8bc96f498663'
RETAINED_R3_NAME='omniroute-auto-switch-candidate-r3-20260912'
RETAINED_R3_VOLUME='omniroute-auto-switch-candidate-data-r3-20260912'
RETAINED_OLD_IID='sha256:a91994bf883698d4520ff048d16be999d4614331a528c76c0b95bc6dc8bec803'
SOURCE='e53d895e9a5e38a7f06ce59de254835f10e829c1'
CANDIDATE_IID='sha256:8211e1071a3b68eac01673d76129150eb0c0fea329dd222bc8bf0394b13fc844'
CANDIDATE_TAG='omniroute-auto-switch-r3:'+SOURCE
CANDIDATE_NAME='omniroute-auto-switch-candidate-r4-20260913'
CANDIDATE_VOLUME='omniroute-auto-switch-candidate-data-r4-20260913'
MIGRATION_170='170_agent_route_runs'
MIGRATION_171='171_agent_route_deferred_metrics'
BINDINGS=json.loads(base64.b64decode('__BINDINGS_B64__',validate=True))
STAGES={'preflight','retained_candidates_identity','live_identity','image_prerequisite','secret_sources','clone_absence',
        'volume_create','volume_identity','sqlite_backup','clone_cloud','candidate_secret_file',
        'container_create','container_identity','container_start','server_health','post_start_sql'}
stage='preflight'
candidate_id=None
health_evidence={'ready':False,'attempts':0,'timeouts':0,'nonzero':0,'successes':0,
                 'container_stopped':False,'deadline_expired':False,'last_probe_category':'not_started'}

class Stop(Exception): pass

def run(args,payload=None,timeout=30):
 try: code,out,_=bounded_capture(args,payload,timeout)
 except RuntimeError: raise Stop()
 if code: raise Stop()
 return out

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

def db_stats(path,require_cloud,require_routes=False):
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
  tables={row[0] for row in db.execute("SELECT name FROM sqlite_master WHERE type='table'")}
  route_tables=('agent_route_runs','agent_route_turns','agent_route_events')
  route_counts={name:(db.execute('SELECT count(*) FROM '+name).fetchone()[0] if name in tables else 0)
                for name in route_tables}
  migration_rows=(set(db.execute("SELECT version,name FROM _omniroute_migrations WHERE version IN ('170','171')"))
                  if '_omniroute_migrations' in tables else set())
  def table_columns(name): return {row[1] for row in db.execute('PRAGMA table_info('+name+')')}
  runs={'run_id','api_key_id','task_id','effective_review_class','created_at','updated_at'}
  turns={'run_id','turn_id','idempotency_key','virtual_route','state','output_started','tool_started',
         'dispatch_claimed','created_at','updated_at'}
  events={'event_id','run_id','turn_id','idempotency_key','kind','busy_slots','processing_requests'}
  schema_170=(tuple(MIGRATION_170.split('_',1)) in migration_rows and set(route_tables).issubset(tables)
              and runs.issubset(table_columns('agent_route_runs'))
              and turns.issubset(table_columns('agent_route_turns'))
              and events.issubset(table_columns('agent_route_events')))
  schema_171=(tuple(MIGRATION_171.split('_',1)) in migration_rows and 'agent_route_events' in tables
              and 'deferred_requests' in table_columns('agent_route_events'))
  if require_routes and not (schema_170 and schema_171): raise Stop()
  result={'provider_rows':providers,'encrypted_fields':encrypted,'plain_fields':plain,'empty_fields':empty,
           'key_value_rows':db.execute('SELECT count(*) FROM key_value').fetchone()[0],
           'user_version':db.execute('PRAGMA user_version').fetchone()[0],'cloud_false':cloud_false,
           'route_runs':route_counts['agent_route_runs'],'route_turns':route_counts['agent_route_turns'],
           'route_events':route_counts['agent_route_events'],'migration_170':schema_170,
           'migration_171':schema_171,'deferred_requests_column':schema_171}
  db.execute('ROLLBACK')
  return result
 finally: db.close()

def missing_container(name):
 names=docker(['container','ls','--all','--format','{{.Names}}']).decode().splitlines()
 if name in names: raise Stop()

def missing_volume(name):
 names=docker(['volume','ls','--format','{{.Name}}']).decode().splitlines()
 if name in names: raise Stop()

def verify_retained(candidate_id,name,volume_name,image_id):
 row=one_json(docker(['container','inspect',candidate_id]))
 if row['Id']!=candidate_id or row['Name']!='/'+name or row['Image']!=image_id: raise Stop()
 if row['State']['Running'] is not False or len(row['Mounts'])!=1: raise Stop()
 mount=row['Mounts'][0]
 if (mount['Type']!='volume' or mount['Name']!=volume_name or
     mount['Destination']!='/app/data' or mount['RW'] is not True): raise Stop()
 retained_volume=volume(volume_name)
 if (retained_volume.get('Name')!=volume_name or retained_volume.get('Driver')!='local'
     or retained_volume.get('Scope')!='local'): raise Stop()

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
        'OMNIROUTE_DISABLE_BACKGROUND_SERVICES':'true','OMNIROUTE_DISABLE_CREDENTIAL_HEALTH_CHECK':'1',
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

def probe_category(returncode,stderr):
 if returncode==0: return 'success'
 text=stderr.decode('utf-8','replace')
 patterns=(
  ('http_4xx',r'\bHTTP\s+4[0-9]{2}\b'),
  ('http_5xx',r'\bHTTP\s+5[0-9]{2}\b'),
  ('connection_refused',r'\bECONNREFUSED\b|connection refused'),
  ('timeout',r'\bETIMEDOUT\b|\bTimeoutError\b|timed?\s*out|\btimeout\b'),
  ('module_error',r'\bERR_MODULE_NOT_FOUND\b|\bERR_REQUIRE_ESM\b|\bERR_DLOPEN_FAILED\b|cannot find module'),
 )
 for name,pattern in patterns:
  if re.search(pattern,text,re.IGNORECASE): return name
 return 'other'

def wait_for_health(probe,running,monotonic,sleep,deadline_seconds,probe_timeout,timeout_cooldown,retry_delay):
 result={'ready':False,'attempts':0,'timeouts':0,'nonzero':0,'successes':0,
         'container_stopped':False,'deadline_expired':False,'last_probe_category':'not_started'}
 deadline=monotonic()+deadline_seconds
 while deadline-monotonic()>=probe_timeout:
  result['attempts']+=1
  try:
   returncode,category=probe(probe_timeout)
  except subprocess.TimeoutExpired:
   result['timeouts']+=1
   result['last_probe_category']='timeout'
   remaining=max(0,deadline-monotonic())
   if remaining: sleep(min(timeout_cooldown,remaining))
   continue
  result['last_probe_category']=category
  if returncode==0:
   result['successes']+=1
   if running():
    result['ready']=True
    return result
   result['container_stopped']=True
   return result
  result['nonzero']+=1
  if not running():
   result['container_stopped']=True
   return result
  remaining=max(0,deadline-monotonic())
  if remaining: sleep(min(retry_delay,remaining))
 result['deadline_expired']=True
 return result

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
 stage='retained_candidates_identity'
 verify_retained(RETAINED_R1_ID,RETAINED_R1_NAME,RETAINED_R1_VOLUME,RETAINED_OLD_IID)
 verify_retained(RETAINED_R2_ID,RETAINED_R2_NAME,RETAINED_R2_VOLUME,RETAINED_OLD_IID)
 verify_retained(RETAINED_R3_ID,RETAINED_R3_NAME,RETAINED_R3_VOLUME,RETAINED_OLD_IID)

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
 if (target_volume['Name']!=CANDIDATE_VOLUME or target_volume['Driver']!='local'
     or target_volume.get('Scope')!='local'): raise Stop()
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
        'OMNIROUTE_DISABLE_BACKGROUND_SERVICES':'true','OMNIROUTE_DISABLE_CREDENTIAL_HEALTH_CHECK':'1',
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
 def native_probe(timeout):
  try:
   returncode,_,stderr=bounded_capture(['docker','exec','--user','node',CANDIDATE_NAME,'node','healthcheck.mjs'],timeout=timeout)
  except RuntimeError as error:
   if str(error)=='COMMAND_TIMEOUT':
    raise subprocess.TimeoutExpired('candidate-health',timeout) from error
   raise Stop() from error
  return returncode,probe_category(returncode,stderr)
 def candidate_running(): return inspect_candidate()['State']['Running'] is True
 health_evidence=wait_for_health(native_probe,candidate_running,time.monotonic,time.sleep,180,15,12,2)
 if not health_evidence['ready']: raise Stop()
 running=inspect_candidate()
 if running['State']['Running'] is not True: raise Stop()

 stage='post_start_sql'
 after=db_stats(target_db,True,True)
 for key in ('provider_rows','encrypted_fields','plain_fields','empty_fields','key_value_rows',
             'user_version','route_runs','route_turns','route_events'):
  if after[key]!=before[key]: raise Stop()
 result={'status':'CANDIDATE_START_R4_PASS','candidate_id':candidate_id,'candidate_image':CANDIDATE_IID,
         'candidate_volume':CANDIDATE_VOLUME,'network_none':True,'published_ports':0,'health':True,
         'cloud_false':True,'db_bytes':os.stat(target_db).st_size,
         'provider_rows':after['provider_rows'],'encrypted_fields':after['encrypted_fields'],
         'plain_fields':after['plain_fields'],'empty_fields':after['empty_fields'],
          'key_value_rows_before':before['key_value_rows'],'key_value_rows_after':after['key_value_rows'],
          'user_version_before':before['user_version'],'user_version_after':after['user_version'],
          'route_runs_before':before['route_runs'],'route_runs_after':after['route_runs'],
          'route_turns_before':before['route_turns'],'route_turns_after':after['route_turns'],
          'route_events_before':before['route_events'],'route_events_after':after['route_events'],
          'migration_170':after['migration_170'],'migration_171':after['migration_171'],
          'deferred_requests_column':after['deferred_requests_column'],
         'health_probe_attempts':health_evidence['attempts'],'health_probe_timeouts':health_evidence['timeouts'],
         'health_probe_nonzero':health_evidence['nonzero'],'health_probe_successes':health_evidence['successes'],
         'health_deadline_expired':health_evidence['deadline_expired'],
         'health_container_stopped':health_evidence['container_stopped'],
         'health_last_probe_category':health_evidence['last_probe_category']}
 print(json.dumps(result,sort_keys=True))
except Exception:
 stopped=stop_candidate()
 print(json.dumps({'status':'CANDIDATE_START_R4_STOP','stage':stage if stage in STAGES else 'preflight',
                   'candidate_stopped':stopped,'health_probe_attempts':health_evidence['attempts'],
                   'health_probe_timeouts':health_evidence['timeouts'],'health_probe_nonzero':health_evidence['nonzero'],
                   'health_probe_successes':health_evidence['successes'],
                   'health_deadline_expired':health_evidence['deadline_expired'],
                   'health_container_stopped':health_evidence['container_stopped'],
                   'health_last_probe_category':health_evidence['last_probe_category']},sort_keys=True))
 raise SystemExit(1)
'''


def digest(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def regular(path):
    return path.is_file() and not path.is_symlink()


def load_transport():
    assert regular(TRANSPORT_HELPER) and digest(TRANSPORT_HELPER) == TRANSPORT_HELPER_HASH
    spec = importlib.util.spec_from_file_location("candidate_r4_transport", TRANSPORT_HELPER)
    transport = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(transport)
    return transport


def render_remote():
    assert regular(BINDINGS) and digest(BINDINGS) == BINDINGS_HASH
    bindings = json.loads(BINDINGS.read_text(encoding="utf-8"))
    assert isinstance(bindings, dict)
    assert REMOTE_TEMPLATE.count("__BINDINGS_B64__") == 1
    assert REMOTE_TEMPLATE.count("__BOUNDED_CAPTURE__") == 1
    capture = inspect.getsource(load_transport().bounded_capture)
    payload = REMOTE_TEMPLATE.replace("__BOUNDED_CAPTURE__", capture)
    payload = payload.replace(
        "__BINDINGS_B64__", base64.b64encode(json.dumps(bindings).encode("utf-8")).decode("ascii")
    )
    ast.parse(payload)
    return payload


def offline_check():
    assert regular(BINDINGS) and digest(BINDINGS) == BINDINGS_HASH
    payload = render_remote()
    assert "subprocess.run" not in payload and "subprocess.Popen" in payload
    assert "--network','none" in payload and "container','create" in payload
    assert "source_volume.get('Name')!=LIVE_VOLUME" in payload
    assert "source_volume.get('Driver')!='local'" in payload
    assert "source_volume.get('Scope')!='local'" in payload
    assert "RETAINED_R1_ID='a710a83e3310cb40c41fba7fba49e5fe700cde84a26b431c919f5570d549d164'" in payload
    assert "RETAINED_R2_ID='e55a92e3645f899b4f59516c7227b9cb859138a8237a838ac0f057c5c4bc2827'" in payload
    assert "RETAINED_R3_ID='6b1089d2b14c175448ca48437e63a7ea0f880deb6374eee26ebf8bc96f498663'" in payload
    assert "CANDIDATE_NAME='omniroute-auto-switch-candidate-r4-20260913'" in payload
    assert "CANDIDATE_VOLUME='omniroute-auto-switch-candidate-data-r4-20260913'" in payload
    assert "171_agent_route_deferred_metrics" in payload and "deferred_requests" in payload
    assert payload.count("'OMNIROUTE_DISABLE_BACKGROUND_SERVICES':'true'") == 2
    assert "'OMNIROUTE_DISABLE_BACKGROUND_SERVICES':'1'" not in payload
    assert "wait_for_health(native_probe,candidate_running,time.monotonic,time.sleep,180,15,12,2)" in payload
    assert "return returncode,probe_category(returncode,stderr)" in payload
    assert PROBE_TIMEOUT_SECONDS >= 15
    assert TRANSPORT_TIMEOUT_SECONDS >= STARTUP_DEADLINE_SECONDS + PROBE_TIMEOUT_SECONDS + STOP_TIMEOUT_SECONDS + 120
    assert "container','rm" not in payload and "volume','rm" not in payload
    assert local_failure(Stop("transport"))["candidate_stopped"] is False
    print("CANDIDATE_START_R4_OFFLINE_CHECK_PASS")


def validate_result(value, returncode):
    health_fields = {"health_probe_attempts", "health_probe_timeouts", "health_probe_nonzero",
                     "health_probe_successes", "health_deadline_expired", "health_container_stopped",
                     "health_last_probe_category"}
    health_categories = {"not_started", "success", "http_4xx", "http_5xx", "connection_refused",
                         "timeout", "module_error", "other"}
    if returncode:
        assert isinstance(value, dict) and set(value) == {"status", "stage", "candidate_stopped"} | health_fields
        assert value["status"] == "CANDIDATE_START_R4_STOP" and value["stage"] in {
            "preflight", "retained_candidates_identity", "live_identity", "image_prerequisite", "secret_sources", "clone_absence",
            "volume_create", "volume_identity", "sqlite_backup", "clone_cloud",
            "candidate_secret_file", "container_create", "container_identity", "container_start",
            "server_health", "post_start_sql",
        }
        assert type(value["candidate_stopped"]) is bool
        assert all(type(value[key]) is int and value[key] >= 0 for key in health_fields if key.startswith("health_probe_"))
        assert value["health_probe_successes"] in {0, 1}
        assert value["health_probe_attempts"] == (value["health_probe_timeouts"] +
                                                    value["health_probe_nonzero"] +
                                                    value["health_probe_successes"])
        assert type(value["health_deadline_expired"]) is bool and type(value["health_container_stopped"]) is bool
        assert value["health_last_probe_category"] in health_categories
        return value
    fields = {
        "status", "candidate_id", "candidate_image", "candidate_volume", "network_none",
        "published_ports", "health", "cloud_false", "db_bytes", "provider_rows",
        "encrypted_fields", "plain_fields", "empty_fields", "key_value_rows_before",
        "key_value_rows_after", "user_version_before", "user_version_after",
        "health_probe_attempts", "health_probe_timeouts", "health_probe_nonzero",
        "health_probe_successes", "health_deadline_expired", "health_container_stopped",
        "health_last_probe_category", "route_runs_before", "route_runs_after",
        "route_turns_before", "route_turns_after", "route_events_before", "route_events_after",
        "migration_170", "migration_171", "deferred_requests_column",
    }
    assert isinstance(value, dict) and set(value) == fields and value["status"] == "CANDIDATE_START_R4_PASS"
    assert re.fullmatch(r"[0-9a-f]{64}", value["candidate_id"])
    assert value["candidate_image"] == CANDIDATE_IID
    assert value["candidate_volume"] == "omniroute-auto-switch-candidate-data-r4-20260913"
    assert value["network_none"] is True and value["health"] is True and value["cloud_false"] is True
    assert value["health_deadline_expired"] is False and value["health_container_stopped"] is False
    assert value["health_probe_successes"] == 1
    assert value["health_last_probe_category"] == "success"
    assert value["published_ports"] == 0 and value["plain_fields"] == 0
    assert value["migration_170"] is True and value["migration_171"] is True
    assert value["deferred_requests_column"] is True
    for name in ("route_runs", "route_turns", "route_events"):
        assert value[name + "before"] == value[name + "after"]
    numeric = fields - {"status", "candidate_id", "candidate_image", "candidate_volume",
                        "network_none", "health", "cloud_false", "health_deadline_expired",
                        "health_container_stopped", "health_last_probe_category",
                        "migration_170", "migration_171", "deferred_requests_column"}
    assert all(type(value[key]) is int and value[key] >= 0 for key in numeric)
    return value


def dispatch_reviewed(command, payload, capture):
    try:
        returncode, stdout, _ = capture(command, payload, TRANSPORT_TIMEOUT_SECONDS)
    except RuntimeError as error:
        raise Stop("transport") from error
    try:
        value = validate_result(json.loads(stdout), returncode)
    except Exception as error:
        raise Stop("remote_validation") from error
    return value, returncode


def local_failure(error):
    stage = str(error) if isinstance(error, Stop) and str(error) in {"transport", "remote_validation"} else "local_validation"
    return {"status": "CANDIDATE_START_R4_STOP", "stage": stage, "candidate_stopped": False,
            "health_probe_attempts": 0, "health_probe_timeouts": 0, "health_probe_nonzero": 0,
            "health_probe_successes": 0, "health_deadline_expired": False,
            "health_container_stopped": False, "health_last_probe_category": "not_started"}


def main():
    if sys.argv[1:] == ["--self-check"]:
        offline_check()
        return 0
    assert len(sys.argv) == 2
    pins_path = pathlib.Path(sys.argv[1])
    assert regular(pins_path)
    pins = json.loads(pins_path.read_text(encoding="utf-8"))
    assert set(pins) == {"launcher_sha256", "contract_sha256", "transport_helper_sha256", "bindings_sha256",
                          "transfer_result_sha256", "r1_start_result_sha256", "r1_diagnosis_result_sha256",
                          "r2_start_result_sha256", "r3_start_result_sha256", "root_cause_result_sha256"}
    assert pins["launcher_sha256"] == digest(pathlib.Path(__file__))
    assert regular(CONTRACT) and pins["contract_sha256"] == digest(CONTRACT)
    assert regular(TRANSPORT_HELPER)
    assert pins["transport_helper_sha256"] == TRANSPORT_HELPER_HASH == digest(TRANSPORT_HELPER)
    assert regular(BINDINGS) and pins["bindings_sha256"] == BINDINGS_HASH == digest(BINDINGS)
    assert regular(TRANSFER_RESULT) and re.fullmatch(r"[0-9a-f]{64}", pins["transfer_result_sha256"])
    assert pins["transfer_result_sha256"] == TRANSFER_RESULT_HASH == digest(TRANSFER_RESULT)
    transfer_text = TRANSFER_RESULT.read_text(encoding="utf-8")
    assert "IMAGE_TRANSFER_PASS" in transfer_text and CANDIDATE_IID in transfer_text and CANDIDATE_TAG in transfer_text
    assert regular(R1_START_RESULT) and pins["r1_start_result_sha256"] == R1_START_RESULT_HASH == digest(R1_START_RESULT)
    r1_start_text = R1_START_RESULT.read_text(encoding="utf-8")
    assert all(item in r1_start_text for item in ('"status":"CANDIDATE_START_STOP"', '"stage":"server_health"', '"candidate_stopped":true'))
    assert regular(R1_DIAGNOSIS_RESULT) and pins["r1_diagnosis_result_sha256"] == R1_DIAGNOSIS_RESULT_HASH == digest(R1_DIAGNOSIS_RESULT)
    diagnosis_text = R1_DIAGNOSIS_RESULT.read_text(encoding="utf-8")
    diagnosis_required = (
        '"status":"CANDIDATE_DIAGNOSIS_V2_PASS"',
        '"candidate_id":"a710a83e3310cb40c41fba7fba49e5fe700cde84a26b431c919f5570d549d164"',
        '"stopped":true', '"health_status":"unhealthy"', '"health_record_state":"no_records"',
        '"startup_milestones":["proxy_patch_initialized","quota_fetchers_registered"]',
        '"startup_error_categories":["no_known_startup_error"]',
    )
    assert all(item in diagnosis_text for item in diagnosis_required)
    assert regular(R2_START_RESULT) and pins["r2_start_result_sha256"] == R2_START_RESULT_HASH == digest(R2_START_RESULT)
    r2_start_text = R2_START_RESULT.read_text(encoding="utf-8")
    assert all(item in r2_start_text for item in (
        '"status":"CANDIDATE_START_R2_STOP"', '"stage":"server_health"', '"candidate_stopped":true',
        '"health_container_stopped":true', '"health_probe_nonzero":2', '"health_probe_timeouts":0'))
    assert regular(R3_START_RESULT) and pins["r3_start_result_sha256"] == R3_START_RESULT_HASH == digest(R3_START_RESULT)
    r3_start_text = R3_START_RESULT.read_text(encoding="utf-8")
    assert all(item in r3_start_text for item in (
        "CANDIDATE_START_R3_PASS", "6b1089d2b14c175448ca48437e63a7ea0f880deb6374eee26ebf8bc96f498663",
        "omniroute-auto-switch-candidate-data-r3-20260912", "network_none", "published_ports"))
    assert regular(ROOT_CAUSE_RESULT) and pins["root_cause_result_sha256"] == ROOT_CAUSE_RESULT_HASH == digest(ROOT_CAUSE_RESULT)
    cause_text = ROOT_CAUSE_RESULT.read_text(encoding="utf-8")
    assert all(item in cause_text for item in (
        'e55a92e3645f899b4f59516c7227b9cb859138a8237a838ac0f057c5c4bc2827',
        '"env_validation_failed": true', '"background_flag_invalid": true',
        'OMNIROUTE_DISABLE_BACKGROUND_SERVICES=1', 'use canonical `true`'))
    transport = load_transport()
    payload = render_remote().encode("utf-8")
    command = [transport.SSH, "-T", *transport.options("192.168.1.68"),
               "belladmin@192.168.1.68", "sudo -n python3 -"]
    value, returncode = dispatch_reviewed(command, payload, transport.bounded_capture)
    print(json.dumps(value, sort_keys=True))
    return 1 if returncode else 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:
        print(json.dumps(local_failure(error), sort_keys=True))
        raise SystemExit(1)
