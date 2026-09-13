"""Prepare a fresh native least-privilege qualification key for the R4 candidate."""
import argparse
import ast
import base64
import hashlib
import importlib.util
import inspect
import json
import os
import pathlib
import re


ROOT = pathlib.Path(__file__).resolve().parents[1]
COORDINATOR_ROOT = pathlib.Path(r"C:\ChatGPT Projects\SW-Selfhosted-Network\.worktrees\omniroute-auto-switch-20260912")
CANDIDATE_ROOT = pathlib.Path(r"C:\ChatGPT Projects\SW-Selfhosted-Network\.worktrees\omniroute-candidate-r4-20260913")
RECONCILE_ROOT = pathlib.Path(r"C:\ChatGPT Projects\SW-Selfhosted-Network\.worktrees\omniroute-candidate-reconcile-20260913")
CONTRACT = ROOT / "docs/auto-switch-candidate-key-r4-contract-20260913.md"
RESULT = ROOT / "docs/auto-switch-candidate-key-r4-result-20260913.md"
BINDINGS = COORDINATOR_ROOT / "docs/auto-switch-bindings-candidate-20260912.json"
TRANSPORT = COORDINATOR_ROOT / "scripts/auto-switch-image-transfer-r3-20260913.py"
SPENT_START_RESULT = CANDIDATE_ROOT / "docs/auto-switch-candidate-start-r4-result-20260913.md"
SPENT_RECONCILE_RESULT = RECONCILE_ROOT / "docs/auto-switch-candidate-reconcile-r1-result-20260913.md"
RECONCILIATION_RESULT = RECONCILE_ROOT / "docs/auto-switch-candidate-reconcile-r2-result-20260913.md"

BINDINGS_SHA256 = "c30aa56eba04d15a50c766a20ba44e88792c60bcddbdf25670fafd5955286e58"
TRANSPORT_SHA256 = "78bb97e57d6229aae84c2f0d0caaf68eeb71ba6b92e69415d83af2a869b8224a"
SPENT_START_RESULT_SHA256 = "cbbd08cfd678021d67bc6f8a799743cfd00d72cff1ce0bbc73960d945e1348bf"
SPENT_RECONCILE_RESULT_SHA256 = "6d7a9c135dfd16375de82a2497444fde72cd869795cf3ee092d6c4d4075aac50"
RECONCILIATION_RESULT_SHA256 = "7efe1cb83cc1c5c6cf85199b919338bb2a6143054d9a6cd315e0c3270fc213cf"

SOURCE = "e53d895e9a5e38a7f06ce59de254835f10e829c1"
IMAGE = "sha256:8211e1071a3b68eac01673d76129150eb0c0fea329dd222bc8bf0394b13fc844"
TAG = "omniroute-auto-switch-r3:" + SOURCE
LIVE_ID = "7b20ca195e3c9e875d0a1ce98832ca469c2a114886335b8466b1467b3ed139bc"
LIVE_IMAGE = "sha256:60ab56311d1c9873416dc53683148d314465370312547b8ce87c442ce084c6a5"
LIVE_VOLUME = "omniroute-data-mcp-audit-20260910-r3"
CANDIDATE_NAME = "omniroute-auto-switch-candidate-r4-20260913"
CANDIDATE_VOLUME = "omniroute-auto-switch-candidate-data-r4-20260913"
CANDIDATE_ID = "9468859edcdb483c53900edde14d301a162cccc791079154677e913f39bf26a3"
KEY_NAME = "auto-switch-candidate-qualification-r4-20260913"
OPERATOR_STORE = "/root/.omniroute-qualification/auto-switch-candidate-qualification-r4-20260913.key"
EXECUTION_READY = True
FIXTURE_CANDIDATE_ID = "f" * 64
RESULT_SCHEMA = "auto-switch-candidate-key-r4-result/v1"
RESULT_LIMIT = 16384

CODEX_CONNECTION = "8f92f200-d280-47b3-b380-2d94be0a4b75"
MODELS = [
    "agent/normal", "agent/high", "llama-cpp/qwen3.8-27b",
    "lm-studio/qwen3.8-27b-unsloth-ud-q4ks",
    "openrouter/cohere/north-mini-code:free", "openrouter/nex-agi/nex-n2.5-pro:free",
    "openrouter/nvidia/nemotron-3-super-120b-a12b:free", "codex/gpt-5.6-terra",
    "codex/gpt-5.6-sol", "openrouter/deepseek/deepseek-v4-flash-0731",
    "openrouter/z-ai/glm-5.3-flash", "openrouter/moonshotai/kimi-k3",
    "openrouter/z-ai/glm-5.3", "openrouter/qwen/qwen3.8-2.4t-a95b",
]
CONNECTIONS = [
    "eb57393b-f559-4acf-aac6-3eb4612e6d1f", "da74225c-0fc0-45ce-ad22-ded85edb34b8",
    "441b80a8-0dd8-4d6b-af31-f0e829f500d8", CODEX_CONNECTION,
    "c9cf9beb-d5bf-4d47-b65e-e219ea4206b9",
]
COMBO_SENTINEL = "__omniroute_agent_route_no_combos__"


class Stop(Exception):
    pass


def digest(path):
    with pathlib.Path(path).open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def regular(path):
    return isinstance(path, pathlib.Path) and path.is_file() and not path.is_symlink()


def require_bound():
    missing = []
    if not re.fullmatch(r"[0-9a-f]{64}", CANDIDATE_ID):
        missing.append("candidate_id")
    if not isinstance(RECONCILIATION_RESULT, pathlib.Path) or not re.fullmatch(r"[0-9a-f]{64}", RECONCILIATION_RESULT_SHA256):
        missing.append("reconciliation_result_sha256")
    return missing


def patch_body():
    return {
        "name": KEY_NAME, "modelAccessMode": "restricted", "allowedModels": MODELS,
        "allowedCombos": [COMBO_SENTINEL], "allowedConnections": CONNECTIONS,
        "noLog": True, "autoResolve": False, "isActive": True, "throttleDelayMs": 0,
        "isBanned": False, "expiresAt": None, "maxSessions": 0, "accessSchedule": None,
        "rateLimits": None, "scopes": ["agent:route"], "allowedEndpoints": ["chat", "models"],
        "streamDefaultMode": "legacy", "compressionEnabled": True,
        "cacheDefaultMode": "legacy", "disableNonPublicModels": False,
        "allowUsageCommand": False, "usageLimitEnabled": False,
        "dailyUsageLimitUsd": None, "weeklyUsageLimitUsd": None, "chaosModeEnabled": False,
    }


def native_roundtrip_probe():
    """Return a disposable e53 native route/DB regression with no live inputs."""
    fields = [
        "id", "name", "key", "machineId", "createdAt", "modelAccessMode", "allowedModels",
        "blockedModels", "allowedCombos", "allowedConnections", "allowedQuotas", "noLog",
        "autoResolve", "isActive", "accessSchedule", "maxRequestsPerDay", "maxRequestsPerMinute",
        "throttleDelayMs", "rateLimits", "maxSessions", "revokedAt", "expiresAt", "lastUsedAt",
        "ipAllowlist", "scopes", "isBanned", "keyPrefix", "keyHash", "proxyId",
        "allowedEndpoints", "streamDefaultMode", "cacheDefaultMode", "disableNonPublicModels",
        "allowUsageCommand", "usageLimitEnabled", "dailyUsageLimitUsd", "weeklyUsageLimitUsd",
        "chaosModeEnabled", "compressionEnabled",
    ]
    expected = dict(patch_body(), blockedModels=[], allowedQuotas=[], accessSchedule=None,
                    maxRequestsPerDay=None, maxRequestsPerMinute=None, revokedAt=None,
                    lastUsedAt=None, ipAllowlist=None, proxyId=None)
    template = r'''(async()=>{
const fs=require('node:fs'),os=require('node:os'),path=require('node:path'),crypto=require('node:crypto');
const {pathToFileURL}=require('node:url');const emit=console.log;console.log=()=>{};console.error=()=>{};
const data=fs.mkdtempSync(path.join(os.tmpdir(),'omniroute-key-r4-roundtrip-'));
process.env.DATA_DIR=data;process.env.API_KEY_SECRET='test-api-key-secret';process.env.INITIAL_PASSWORD='bootstrap-password';delete process.env.CLOUD_URL;
const imp=p=>import(pathToFileURL(path.join(process.cwd(),p)).href);
const core=await imp('src/lib/db/core.ts'),keys=await imp('src/lib/db/apiKeys.ts');
try{
 const settings=await imp('src/lib/db/settings.ts'),helper=await imp('tests/helpers/managementSession.ts');
 const list=await imp('src/app/api/keys/route.ts'),detail=await imp('src/app/api/keys/[id]/route.ts');
 await settings.updateSettings({requireLogin:true,password:'',cloudEnabled:false});await keys.createApiKey('management','1234567890abcdef');
 const createReq=await helper.makeManagementSessionRequest('http://localhost/api/keys',{method:'POST',body:{name:__NAME__,noLog:true,scopes:['agent:route'],allowedConnections:__CONNECTIONS__}});
 const createRes=await list.POST(createReq),created=await createRes.json(),patch=__PATCH__;
 const patchReq=await helper.makeManagementSessionRequest('http://localhost/api/keys/'+created.id,{method:'PATCH',body:patch});
 const patchRes=await detail.PATCH(patchReq,{params:Promise.resolve({id:created.id})});
 const getReq=await helper.makeManagementSessionRequest('http://localhost/api/keys/'+created.id);
 const getRes=await detail.GET(getReq,{params:Promise.resolve({id:created.id})}),row=await getRes.json();
 const expectedFields=__FIELDS__.sort(),expected=__EXPECTED__,missing_fields=expectedFields.filter(k=>!(k in row));
 const extra_fields=Object.keys(row).filter(k=>!expectedFields.includes(k)).sort(),mismatch_fields=Object.keys(expected).filter(k=>JSON.stringify(row[k])!==JSON.stringify(expected[k])).sort();
 const createFields=['key','name','id','machineId','allowedConnections','noLog','allowUsageCommand','usageLimitEnabled','dailyUsageLimitUsd','weeklyUsageLimitUsd','chaosModeEnabled','streamDefaultMode','compressionEnabled','cacheDefaultMode'].sort();
 if(JSON.stringify(Object.keys(created).sort())!==JSON.stringify(createFields))mismatch_fields.push('create.fields');
 if(created.name!==__NAME__||JSON.stringify(created.allowedConnections)!==JSON.stringify(__CONNECTIONS__))mismatch_fields.push('create.policy');
 if(typeof created.id!=='string'||typeof created.machineId!=='string'||typeof created.key!=='string')mismatch_fields.push('create.identity');
 const patchBody=await patchRes.json(),patchFields=['message',...Object.keys(patch)].sort();
 if(JSON.stringify(Object.keys(patchBody).sort())!==JSON.stringify(patchFields)||patchBody.message!=='API key settings updated successfully')mismatch_fields.push('patch.fields');
 const echo={...patchBody};delete echo.message;if(JSON.stringify(echo)!==JSON.stringify(patch))mismatch_fields.push('patch.echo');
 if(row.id!==created.id||row.name!==__NAME__||row.machineId!==created.machineId)mismatch_fields.push('get.identity');
 if(row.key!==created.key.slice(0,8)+'****'+created.key.slice(-4))mismatch_fields.push('get.mask');
 if(row.keyPrefix!==created.key.slice(0,12)||row.keyHash!==crypto.createHash('sha256').update(created.key).digest('hex'))mismatch_fields.push('get.key_metadata');
 const dbrow=core.getDbInstance().prepare('SELECT id,ip_allowlist FROM api_keys WHERE id=?').get(created.id);mismatch_fields.sort();
 emit(JSON.stringify({create_status:createRes.status,patch_status:patchRes.status,get_status:getRes.status,missing_fields,extra_fields,mismatch_fields,db_ip_allowlist_is_null:!!dbrow&&dbrow.id===created.id&&dbrow.ip_allowlist===null}));
 if(createRes.status!==201||patchRes.status!==200||getRes.status!==200||missing_fields.length||extra_fields.length||mismatch_fields.length||!dbrow||dbrow.ip_allowlist!==null)process.exitCode=1;
}finally{core.resetDbInstance();keys.resetApiKeyState();fs.rmSync(data,{recursive:true,force:true});}
})().catch(()=>{process.stdout.write(JSON.stringify({status:'ROUNDTRIP_FAILED'}));process.exitCode=1;});'''
    values = {"__CONNECTIONS__": json.dumps(CONNECTIONS, separators=(",", ":")),
              "__NAME__": json.dumps(KEY_NAME), "__PATCH__": json.dumps(patch_body(), separators=(",", ":")),
              "__FIELDS__": json.dumps(fields, separators=(",", ":")),
              "__EXPECTED__": json.dumps(expected, separators=(",", ":"))}
    for marker, replacement in values.items():
        template = template.replace(marker, replacement)
    return template


NODE_TEMPLATE = r'''
const http=require('node:http'),crypto=require('node:crypto');
const ADMIN=Buffer.from('__ADMIN_B64__','base64').toString('utf8');
const NAME=__NAME__;const CODEX=__CODEX__;const MODELS=__MODELS__;const CONNECTIONS=__CONNECTIONS__;
const SENTINEL=__SENTINEL__;const PATCH=__PATCH__;
const FIELDS=['id','name','key','machineId','createdAt','modelAccessMode','allowedModels','blockedModels',
'allowedCombos','allowedConnections','allowedQuotas','noLog','autoResolve','isActive','accessSchedule',
'maxRequestsPerDay','maxRequestsPerMinute','throttleDelayMs','rateLimits','maxSessions','revokedAt',
'expiresAt','lastUsedAt','ipAllowlist','scopes','isBanned','keyPrefix','keyHash','proxyId',
'allowedEndpoints','streamDefaultMode','cacheDefaultMode','disableNonPublicModels','allowUsageCommand',
'usageLimitEnabled','dailyUsageLimitUsd','weeklyUsageLimitUsd','chaosModeEnabled','compressionEnabled'];
let stage='native_preflight',keyId=null,secret=null,httpStatus=null,failure='validation';
let rollbackAttempted=false,keyInactiveReadback=null;
function fail(category='validation'){failure=category;const e=new Error('stop');e.category=category;throw e}
function category(s){return s>=400&&s<500?'http_4xx':s>=500&&s<600?'http_5xx':'http_other'}
function keys(v,w){if(!v||typeof v!=='object'||Array.isArray(v)||JSON.stringify(Object.keys(v).sort())!==JSON.stringify([...w].sort()))fail()}
function canonical(v){if(Array.isArray(v))return v.map(canonical);if(v&&typeof v==='object')return Object.fromEntries(Object.keys(v).sort().map(k=>[k,canonical(v[k])]));return v}
function equal(a,b){if(JSON.stringify(canonical(a))!==JSON.stringify(canonical(b)))fail()}
function request(method,path,body){return new Promise((resolve,reject)=>{const payload=body===undefined?null:Buffer.from(JSON.stringify(body));const headers={Authorization:'Bearer '+ADMIN,Accept:'application/json'};if(payload){headers['Content-Type']='application/json';headers['Content-Length']=String(payload.length)}const req=http.request({host:'127.0.0.1',port:20128,method,path,headers},res=>{let size=0,chunks=[];res.on('data',c=>{size+=c.length;if(size>1048576)req.destroy(Object.assign(new Error('bounded'),{category:'output_limit'}));else chunks.push(c)});res.on('end',()=>{try{if(res.statusCode>=300&&res.statusCode<400)fail('http_other');resolve({status:res.statusCode,value:JSON.parse(Buffer.concat(chunks).toString('utf8'))})}catch(e){reject(e)}})});req.setTimeout(8000,()=>req.destroy(Object.assign(new Error('timeout'),{category:'timeout'})));req.on('error',e=>{if(!e.category)e.category='connection';reject(e)});if(payload)req.write(payload);req.end()})}
function expect(r,s){if(r.status!==s){httpStatus=r.status;fail(category(r.status))}}
async function rollback(){if(!keyId)return;rollbackAttempted=true;try{let r=await request('PATCH','/api/keys/'+keyId,{isActive:false});expect(r,200);r=await request('GET','/api/keys/'+keyId);expect(r,200);keys(r.value,FIELDS);keyInactiveReadback=r.value.id===keyId&&r.value.name===NAME&&r.value.isActive===false}catch{keyInactiveReadback=false}}
async function main(){
 let r=await request('GET','/api/keys');expect(r,200);keys(r.value,['keys','total','allowKeyReveal']);if(!Array.isArray(r.value.keys)||r.value.keys.some(x=>x&&x.name===NAME))fail();
 r=await request('GET','/api/combos');expect(r,200);keys(r.value,['combos','total']);if(!Array.isArray(r.value.combos)||r.value.combos.some(x=>x&&(x.name===SENTINEL||x.name==='combo/'+SENTINEL)))fail();
 stage='provider_preflight';r=await request('GET','/api/providers/'+CODEX);expect(r,200);keys(r.value,['connection']);if(!r.value.connection||r.value.connection.id!==CODEX||r.value.connection.provider!=='codex'||r.value.connection.isActive!==false||'accessToken'in r.value.connection||'refreshToken'in r.value.connection||'idToken'in r.value.connection)fail();
 stage='create';r=await request('POST','/api/keys',{name:NAME,noLog:true,scopes:['agent:route'],allowedConnections:CONNECTIONS});expect(r,201);keys(r.value,['key','name','id','machineId','allowedConnections','noLog','allowUsageCommand','usageLimitEnabled','dailyUsageLimitUsd','weeklyUsageLimitUsd','chaosModeEnabled','streamDefaultMode','compressionEnabled','cacheDefaultMode']);
 keyId=r.value.id;secret=r.value.key;if(r.value.name!==NAME||!/^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/.test(keyId)||!/^sk-[0-9a-f]{16}-[0-9a-f]{6}-[0-9a-f]{8}$/.test(secret))fail();equal(r.value.allowedConnections,CONNECTIONS);
 stage='patch';r=await request('PATCH','/api/keys/'+keyId,PATCH);expect(r,200);keys(r.value,['message',...Object.keys(PATCH)]);if(r.value.message!=='API key settings updated successfully')fail();const echo={...r.value};delete echo.message;equal(echo,PATCH);
 stage='readback';r=await request('GET','/api/keys/'+keyId);expect(r,200);keys(r.value,FIELDS);const row=r.value;if(row.id!==keyId||row.name!==NAME||row.key!==secret.slice(0,8)+'****'+secret.slice(-4)||row.keyPrefix!==secret.slice(0,12)||row.keyHash!==crypto.createHash('sha256').update(secret).digest('hex'))fail();
 equal({modelAccessMode:row.modelAccessMode,allowedModels:row.allowedModels,blockedModels:row.blockedModels,allowedCombos:row.allowedCombos,allowedConnections:row.allowedConnections,allowedQuotas:row.allowedQuotas,noLog:row.noLog,autoResolve:row.autoResolve,isActive:row.isActive,accessSchedule:row.accessSchedule,maxRequestsPerDay:row.maxRequestsPerDay,maxRequestsPerMinute:row.maxRequestsPerMinute,throttleDelayMs:row.throttleDelayMs,rateLimits:row.rateLimits,maxSessions:row.maxSessions,revokedAt:row.revokedAt,expiresAt:row.expiresAt,lastUsedAt:row.lastUsedAt,ipAllowlist:row.ipAllowlist,scopes:row.scopes,isBanned:row.isBanned,proxyId:row.proxyId,allowedEndpoints:row.allowedEndpoints,streamDefaultMode:row.streamDefaultMode,cacheDefaultMode:row.cacheDefaultMode,disableNonPublicModels:row.disableNonPublicModels,allowUsageCommand:row.allowUsageCommand,usageLimitEnabled:row.usageLimitEnabled,dailyUsageLimitUsd:row.dailyUsageLimitUsd,weeklyUsageLimitUsd:row.weeklyUsageLimitUsd,chaosModeEnabled:row.chaosModeEnabled,compressionEnabled:row.compressionEnabled},{modelAccessMode:'restricted',allowedModels:MODELS,blockedModels:[],allowedCombos:[SENTINEL],allowedConnections:CONNECTIONS,allowedQuotas:[],noLog:true,autoResolve:false,isActive:true,accessSchedule:null,maxRequestsPerDay:null,maxRequestsPerMinute:null,throttleDelayMs:0,rateLimits:null,maxSessions:0,revokedAt:null,expiresAt:null,lastUsedAt:null,ipAllowlist:null,scopes:['agent:route'],isBanned:false,proxyId:null,allowedEndpoints:['chat','models'],streamDefaultMode:'legacy',cacheDefaultMode:'legacy',disableNonPublicModels:false,allowUsageCommand:false,usageLimitEnabled:false,dailyUsageLimitUsd:null,weeklyUsageLimitUsd:null,chaosModeEnabled:false,compressionEnabled:true});
 process.stdout.write(JSON.stringify({status:'KEY_NATIVE_R4_PASS',key_id:keyId,secret,codex_inactive_readback:true}));
}
main().catch(async e=>{if(e&&['validation','http_4xx','http_5xx','http_other','timeout','connection','output_limit'].includes(e.category))failure=e.category;await rollback();process.stdout.write(JSON.stringify({status:'KEY_NATIVE_R4_STOP',stage,key_id:keyId,failure_category:failure,http_status:httpStatus,rollback_attempted:rollbackAttempted,key_inactive_readback:keyInactiveReadback}));process.exitCode=1});
'''


ROLLBACK_TEMPLATE = r'''
const http=require('node:http');const ADMIN=Buffer.from('__ADMIN_B64__','base64').toString('utf8');const ID=__KEY_ID__;const NAME=__NAME__;
function request(method,path,body){return new Promise((resolve,reject)=>{const b=body?Buffer.from(JSON.stringify(body)):null;const h={Authorization:'Bearer '+ADMIN,Accept:'application/json'};if(b){h['Content-Type']='application/json';h['Content-Length']=String(b.length)}const q=http.request({host:'127.0.0.1',port:20128,method,path,headers:h},r=>{let n=0,a=[];r.on('data',c=>{n+=c.length;if(n>1048576)q.destroy();else a.push(c)});r.on('end',()=>{try{resolve({status:r.statusCode,value:JSON.parse(Buffer.concat(a).toString())})}catch(e){reject(e)}})});q.setTimeout(8000,()=>q.destroy());q.on('error',reject);if(b)q.write(b);q.end()})}
(async()=>{let r=await request('PATCH','/api/keys/'+ID,{isActive:false});if(r.status!==200)throw 0;r=await request('GET','/api/keys/'+ID);if(r.status!==200||!r.value||r.value.id!==ID||r.value.name!==NAME||r.value.isActive!==false)throw 0;process.stdout.write(JSON.stringify({status:'ROLLBACK_PASS',key_inactive_readback:true}))})().catch(()=>{process.stdout.write(JSON.stringify({status:'ROLLBACK_STOP',key_inactive_readback:false}));process.exitCode=1});
'''


REMOTE_TEMPLATE = r'''
import json,os,pathlib,re,sqlite3,stat,subprocess,threading,time,urllib.parse
__BOUNDED_CAPTURE__
LIVE_ID=__LIVE_ID__;LIVE_IMAGE=__LIVE_IMAGE__;LIVE_VOLUME=__LIVE_VOLUME__;CANDIDATE=__CANDIDATE__;CANDIDATE_ID=__CANDIDATE_ID__;VOLUME=__VOLUME__;IMAGE=__IMAGE__;TAG=__TAG__;SOURCE=__SOURCE__;KEY_NAME=__KEY_NAME__;STORE=pathlib.Path(__STORE__);NODE=__NODE__;ROLLBACK=__ROLLBACK__
stage='identity';key_id=None;created=False;stored=False;store_identity=None;store_parent_fd=None;rollback_attempted=False;key_inactive_readback=None;failure_category='validation';http_status=None
class Stop(Exception):pass
class MutationUnknown(Exception):pass
def run(a,p=None,t=60):
 try:rc,out,err=bounded_capture(a,p,t)
 except RuntimeError as e:raise Stop('child_timeout' if str(e)=='COMMAND_TIMEOUT' else 'child_output')
 return rc,out,err
def docker(a,p=None,t=60):return run(['docker',*a],p,t)
def formatted(kind,fmt,identity):
 rc,out,err=docker([kind,'inspect','--format',fmt,identity])
 if rc or err:raise Stop()
 v=json.loads(out)
 if not isinstance(v,dict):raise Stop()
 return v
def safe_dir(path,mode):
 item=os.lstat(path)
 if not stat.S_ISDIR(item.st_mode) or stat.S_ISLNK(item.st_mode) or item.st_uid!=0 or item.st_gid!=0 or stat.S_IMODE(item.st_mode)!=mode or pathlib.Path(os.path.realpath(path))!=path:raise Stop()
 return item
def read_regular(path,limit,uid,gid,mode):
 item=os.lstat(path)
 if not stat.S_ISREG(item.st_mode) or stat.S_ISLNK(item.st_mode) or item.st_uid!=uid or item.st_gid!=gid or stat.S_IMODE(item.st_mode)!=mode or item.st_size>limit:raise Stop()
 fd=os.open(path,os.O_RDONLY|os.O_NOFOLLOW)
 try:
  held=os.fstat(fd);raw=b''
  while len(raw)<=limit:
   block=os.read(fd,min(65536,limit+1-len(raw)))
   if not block:break
   raw+=block
  after=os.fstat(fd)
  if len(raw)>limit or len(raw)!=held.st_size or (held.st_dev,held.st_ino,held.st_size,held.st_mtime_ns)!=(after.st_dev,after.st_ino,after.st_size,after.st_mtime_ns):raise Stop()
  return raw
 finally:os.close(fd)
def parse_env(raw):
 result={}
 for line in raw.decode('utf8').splitlines():
  value=line.strip()
  if not value or value.startswith('#') or '=' not in value:continue
  key,item=value.split('=',1);key=key.strip();item=item.strip()
  if key in result:raise Stop()
  if len(item)>=2 and item[0] in ('\"',"'") and item[-1]==item[0]:item=item[1:-1]
  result[key]=item
 return result
def cloud_false(path):
 db=sqlite3.connect('file:'+urllib.parse.quote(str(path),safe='/')+'?mode=ro',uri=True,timeout=10)
 try:
  db.execute('PRAGMA query_only=ON');db.execute('BEGIN');rows=db.execute("SELECT value FROM key_value WHERE namespace='settings' AND key='cloudEnabled'").fetchall()
  if len(rows)!=1 or not isinstance(rows[0][0],str) or json.loads(rows[0][0]) is not False:raise Stop()
  db.execute('ROLLBACK')
 finally:db.close()
def schema_ready(path):
 db=sqlite3.connect('file:'+urllib.parse.quote(str(path),safe='/')+'?mode=ro',uri=True,timeout=10)
 try:
  db.execute('PRAGMA query_only=ON');db.execute('BEGIN')
  if db.execute('PRAGMA quick_check').fetchall()!=[('ok',)]:raise Stop()
  migrations=set(db.execute("SELECT version,name FROM _omniroute_migrations WHERE version IN ('170','171')"))
  expected={'agent_route_runs':{'run_id','api_key_id','task_id','effective_review_class','created_at','updated_at'},'agent_route_turns':{'run_id','turn_id','idempotency_key','virtual_route','state','output_started','tool_started','dispatch_claimed','created_at','updated_at'},'agent_route_events':{'event_id','run_id','turn_id','idempotency_key','kind','provider','model','connection_id','candidate_attempt','repair_attempt','reviewer_attempt','admission_state','fallback_reason','latency_ms','busy_slots','processing_requests','prompt_tokens','completion_tokens','objective_outcome','reviewer_class','reviewer_model','reviewer_verdict','subscription_percent','subscription_evidence_id','subscription_evidence_at','subscription_decision','occurred_at','deferred_requests'}}
  if ('170','170_agent_route_runs') not in migrations or ('171','171_agent_route_deferred_metrics') not in migrations:raise Stop()
  for table,columns in expected.items():
   actual={row[1] for row in db.execute('PRAGMA table_info('+table+')')}
   if actual!=columns:raise Stop()
  db.execute('ROLLBACK')
 finally:db.close()
def credential_shape(path):
 db=sqlite3.connect('file:'+urllib.parse.quote(str(path),safe='/')+'?mode=ro',uri=True,timeout=10)
 try:
  db.execute('PRAGMA query_only=ON');db.execute('BEGIN')
  columns={row[1] for row in db.execute('PRAGMA table_info(provider_connections)')};fields=['api_key','access_token','refresh_token','id_token']
  if not set(fields).issubset(columns):raise Stop()
  encrypted=plain=empty=0
  for row in db.execute('SELECT '+','.join(fields)+' FROM provider_connections'):
   for value in row:
    if value is None or value=='':empty+=1
    elif isinstance(value,str) and value.startswith('enc:v1:'):encrypted+=1
    else:plain+=1
  if (encrypted,plain,empty)!=(18,0,34):raise Stop()
  db.execute('ROLLBACK')
 finally:db.close()
def rollback_key():
 global rollback_attempted,key_inactive_readback
 if not key_id or rollback_attempted:return
 rollback_attempted=True
 try:
  source=ROLLBACK.replace('__KEY_ID__',json.dumps(key_id));rc,out,err=docker(['container','exec','-i','--user','node','--workdir','/app',CANDIDATE,'node','-'],source.encode(),60)
  value=json.loads(out) if not err else None
  key_inactive_readback=rc==0 and value=={'status':'ROLLBACK_PASS','key_inactive_readback':True}
 except:key_inactive_readback=False
def remove_store():
 if not stored or store_identity is None or store_parent_fd is None:return None
 try:
  item=os.stat(STORE.name,dir_fd=store_parent_fd,follow_symlinks=False)
  if (item.st_dev,item.st_ino)!=store_identity or not stat.S_ISREG(item.st_mode) or stat.S_ISLNK(item.st_mode):return False
  os.unlink(STORE.name,dir_fd=store_parent_fd);os.fsync(store_parent_fd)
  try:os.stat(STORE.name,dir_fd=store_parent_fd,follow_symlinks=False);return False
  except FileNotFoundError:return True
 except:return False
try:
 candidate_format='{"id":{{json .Id}},"name":{{json .Name}},"image":{{json .Image}},"config_image":{{json .Config.Image}},"source":{{json (index .Config.Labels "org.opencontainers.image.revision")}},"user":{{json .Config.User}},"running":{{json .State.Running}},"status":{{json .State.Status}},"health":{{if .State.Health}}{{json .State.Health.Status}}{{else}}"none"{{end}},"network":{{json .HostConfig.NetworkMode}},"readonly":{{json .HostConfig.ReadonlyRootfs}},"restart":{{json .HostConfig.RestartPolicy.Name}},"caps":{{json .HostConfig.CapDrop}},"security":{{json .HostConfig.SecurityOpt}},"ports":{{json .HostConfig.PortBindings}},"network_ports":{{json .NetworkSettings.Ports}},"tmpfs":{{json .HostConfig.Tmpfs}},"mounts":{{json .Mounts}}}'
 row=formatted('container',candidate_format,CANDIDATE)
 if row!=formatted('container',candidate_format,CANDIDATE_ID):raise Stop()
 expected_tmpfs={'rw','noexec','nosuid','nodev','size=67108864','mode=1777'};tmpfs=row.get('tmpfs');tokens=(tmpfs.get('/tmp') if isinstance(tmpfs,dict) else '').split(',')
 ports=row.get('network_ports')
 if row.get('id')!=CANDIDATE_ID or row.get('name')!='/'+CANDIDATE or row.get('image')!=IMAGE or row.get('config_image')!=TAG or row.get('source')!=SOURCE or row.get('user')!='node' or row.get('running') is not True or row.get('status')!='running' or row.get('health')!='healthy':raise Stop()
 if row.get('network')!='none' or row.get('readonly') is not True or row.get('restart')!='no' or row.get('caps')!=['ALL'] or row.get('security')!=['no-new-privileges'] or row.get('ports') not in (None,{}) or not isinstance(tmpfs,dict) or set(tmpfs)!={'/tmp'} or len(tokens)!=6 or set(tokens)!=expected_tmpfs or not (ports in (None,{}) or isinstance(ports,dict) and all(x is None for x in ports.values())):raise Stop()
 mounts=row.get('mounts');
 if not isinstance(mounts,list) or len(mounts)!=1 or mounts[0].get('Type')!='volume' or mounts[0].get('Name')!=VOLUME or mounts[0].get('Destination')!='/app/data' or mounts[0].get('RW') is not True:raise Stop()
 live_format='{"id":{{json .Id}},"image":{{json .Image}},"running":{{json .State.Running}},"mounts":{{json .Mounts}}}'
 live=formatted('container',live_format,LIVE_ID);lm=live.get('mounts')
 if live.get('id')!=LIVE_ID or live.get('image')!=LIVE_IMAGE or live.get('running') is not True or not isinstance(lm,list) or len(lm)!=1 or lm[0].get('Type')!='volume' or lm[0].get('Name')!=LIVE_VOLUME or lm[0].get('Destination')!='/app/data':raise Stop()
 image=formatted('image','{"id":{{json .Id}},"tags":{{json .RepoTags}}}',TAG)
 if image!={'id':IMAGE,'tags':[TAG]}:raise Stop()
 volume=formatted('volume','{"name":{{json .Name}},"driver":{{json .Driver}},"scope":{{json .Scope}},"root":{{json .Mountpoint}}}',VOLUME);root=pathlib.Path(volume.get('root',''))
 if volume.get('name')!=VOLUME or volume.get('driver')!='local' or volume.get('scope')!='local' or not root.is_dir() or root.is_symlink() or pathlib.Path(os.path.realpath(root))!=root:raise Stop()
 db_path=root/'storage.sqlite';item=os.lstat(db_path)
 if not stat.S_ISREG(item.st_mode) or stat.S_ISLNK(item.st_mode) or pathlib.Path(os.path.realpath(db_path))!=db_path:raise Stop()
 cloud_false(db_path);schema_ready(db_path);credential_shape(db_path)
 env=parse_env(read_regular(root/'server.env',65536,1000,1000,0o600));required={'STORAGE_ENCRYPTION_KEY','JWT_SECRET','API_KEY_SECRET'}
 if set(env) not in (required,required|{'STORAGE_ENCRYPTION_KEY_VERSION'}) or any(not env[name] or len(env[name])>4096 for name in env):raise Stop()
 del env
 stage='store_preflight';parent=STORE.parent
 if STORE.name!='auto-switch-candidate-qualification-r4-20260913.key' or parent!=pathlib.Path('/root/.omniroute-qualification') or os.path.lexists(STORE):raise Stop()
 parent_before=safe_dir(parent,0o700)
 store_parent_fd=os.open(parent,os.O_RDONLY|os.O_DIRECTORY|os.O_NOFOLLOW);parent_info=os.fstat(store_parent_fd)
 if not stat.S_ISDIR(parent_info.st_mode) or parent_info.st_uid!=0 or parent_info.st_gid!=0 or stat.S_IMODE(parent_info.st_mode)!=0o700 or (parent_info.st_dev,parent_info.st_ino)!=(parent_before.st_dev,parent_before.st_ino):raise Stop()
 stage='native_dispatch'
 try:rc,out,err=bounded_capture(['docker','container','exec','-i','--user','node','--workdir','/app',CANDIDATE,'node','-'],NODE.encode(),180)
 except RuntimeError as error:raise MutationUnknown('child_timeout' if str(error)=='COMMAND_TIMEOUT' else 'child_output')
 if err:raise MutationUnknown('child_output')
 try:native=json.loads(out)
 except Exception:raise MutationUnknown('remote_envelope')
 if rc:
  fields={'status','stage','key_id','failure_category','http_status','rollback_attempted','key_inactive_readback'}
  if not isinstance(native,dict) or set(native)!=fields or native.get('status')!='KEY_NATIVE_R4_STOP':raise MutationUnknown('remote_envelope')
  key_id=native['key_id'];failure_category=native['failure_category'];http_status=native['http_status'];rollback_attempted=native['rollback_attempted'];key_inactive_readback=native['key_inactive_readback']
  if native['stage'] not in {'native_preflight','provider_preflight','create','patch','readback'}:raise MutationUnknown('remote_envelope')
  stage=native['stage']
  raise Stop(failure_category)
 if not isinstance(native,dict) or set(native)!={'status','key_id','secret','codex_inactive_readback'} or native.get('status')!='KEY_NATIVE_R4_PASS' or native.get('codex_inactive_readback') is not True:raise MutationUnknown('remote_envelope')
 key_id=native['key_id'];secret=native['secret'];created=True
 if not re.fullmatch(r'[0-9a-f-]{36}',key_id) or not re.fullmatch(r'sk-[0-9a-f]{16}-[0-9a-f]{6}-[0-9a-f]{8}',secret):raise Stop()
 stage='db_readback';db=sqlite3.connect('file:'+urllib.parse.quote(str(db_path),safe='/')+'?mode=ro',uri=True,timeout=10)
 try:
  db.execute('PRAGMA query_only=ON');db.execute('BEGIN');rows=db.execute('SELECT id,ip_allowlist FROM api_keys WHERE id=?',(key_id,)).fetchall()
  if rows!=[(key_id,None)]:raise Stop()
  db.execute('ROLLBACK')
 finally:db.close()
 stage='store';old=os.umask(0o077)
 try:
  fd=os.open(STORE.name,os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW,0o600,dir_fd=store_parent_fd);stored=True;opened=os.fstat(fd);store_identity=(opened.st_dev,opened.st_ino)
  try:
   raw=secret.encode('ascii');offset=0
   while offset<len(raw):
    wrote=os.write(fd,raw[offset:])
    if wrote<=0:raise Stop()
    offset+=wrote
   os.fchmod(fd,0o600);os.fchown(fd,0,0);os.fsync(fd);item=os.fstat(fd)
   if not stat.S_ISREG(item.st_mode) or item.st_uid!=0 or item.st_gid!=0 or stat.S_IMODE(item.st_mode)!=0o600 or item.st_size!=len(raw):raise Stop()
  finally:os.close(fd)
 finally:os.umask(old)
 os.fsync(store_parent_fd);item=os.stat(STORE.name,dir_fd=store_parent_fd,follow_symlinks=False)
 if not stat.S_ISREG(item.st_mode) or stat.S_ISLNK(item.st_mode) or (item.st_dev,item.st_ino)!=store_identity:raise Stop()
 stage='result';row=formatted('container',candidate_format,CANDIDATE_ID)
 if row.get('id')!=CANDIDATE_ID or row.get('running') is not True or row.get('health')!='healthy' or row.get('network')!='none':raise Stop()
 print(json.dumps({'status':'CANDIDATE_KEY_R4_PASS','candidate_id':CANDIDATE_ID,'candidate_running':True,'key_id':key_id,'key_name':KEY_NAME,'created':True,'patched':True,'readback':True,'stored':True,'allowed_models':14,'allowed_connections':5,'allowed_quotas':0,'scopes':1,'endpoints':2,'no_log':True,'auto_resolve':False,'codex_inactive_readback':True,'db_ip_allowlist_is_null':True,'migration_170':True,'migration_171':True,'rollback_attempted':False,'key_inactive_readback':False},sort_keys=True,separators=(',',':')))
except MutationUnknown as error:
 print(json.dumps({'status':'CANDIDATE_KEY_R4_UNKNOWN','stage':'native_dispatch','candidate_id':None,'candidate_running':None,'key_id':None,'created':None,'stored':None,'store_removed':None,'failure_category':str(error) if str(error) in {'child_timeout','child_output','remote_envelope'} else 'remote_envelope','http_status':None,'rollback_attempted':None,'key_inactive_readback':None},sort_keys=True,separators=(',',':')));raise SystemExit(2)
except Exception as error:
 if str(error) in {'validation','http_4xx','http_5xx','http_other','timeout','connection','output_limit','child_timeout','child_output'}:failure_category=str(error)
 rollback_key();removed=remove_store()
 print(json.dumps({'status':'CANDIDATE_KEY_R4_STOP','stage':stage if stage in {'identity','store_preflight','native','native_preflight','provider_preflight','create','patch','readback','db_readback','store','result'} else 'identity','candidate_id':CANDIDATE_ID,'candidate_running':True if stage!='identity' else None,'key_id':key_id,'created':created,'stored':stored,'store_removed':removed,'failure_category':failure_category,'http_status':http_status,'rollback_attempted':rollback_attempted,'key_inactive_readback':key_inactive_readback},sort_keys=True,separators=(',',':')));raise SystemExit(1)
finally:
 if store_parent_fd is not None:os.close(store_parent_fd)
'''


PASS_FIELDS = {"status", "candidate_id", "candidate_running", "key_id", "key_name", "created",
               "patched", "readback", "stored", "allowed_models", "allowed_connections",
               "allowed_quotas", "scopes", "endpoints", "no_log", "auto_resolve",
               "codex_inactive_readback", "db_ip_allowlist_is_null", "migration_170", "migration_171", "rollback_attempted",
               "key_inactive_readback"}


def fixture_result():
    return {"status": "CANDIDATE_KEY_R4_PASS", "candidate_id": FIXTURE_CANDIDATE_ID,
            "candidate_running": True, "key_id": "11111111-1111-4111-8111-111111111111",
            "key_name": KEY_NAME, "created": True, "patched": True, "readback": True,
            "stored": True, "allowed_models": 14, "allowed_connections": 5,
            "allowed_quotas": 0, "scopes": 1, "endpoints": 2, "no_log": True,
            "auto_resolve": False, "codex_inactive_readback": True,
            "db_ip_allowlist_is_null": True, "migration_170": True, "migration_171": True, "rollback_attempted": False,
            "key_inactive_readback": False}


def validate_result(value, returncode, expected_candidate_id=None):
    candidate_id = expected_candidate_id or CANDIDATE_ID
    if returncode == 0:
        if not isinstance(value, dict) or set(value) != PASS_FIELDS or value["status"] != "CANDIDATE_KEY_R4_PASS":
            raise Stop("remote_validation")
        expected = {"candidate_id": candidate_id, "candidate_running": True, "key_name": KEY_NAME,
                    "created": True, "patched": True, "readback": True, "stored": True,
                    "allowed_models": 14, "allowed_connections": 5, "allowed_quotas": 0,
                    "scopes": 1, "endpoints": 2, "no_log": True, "auto_resolve": False,
                    "codex_inactive_readback": True, "db_ip_allowlist_is_null": True,
                    "migration_170": True, "migration_171": True,
                    "rollback_attempted": False, "key_inactive_readback": False}
        if any(value[key] != wanted or type(value[key]) is not type(wanted) for key, wanted in expected.items()):
            raise Stop("remote_validation")
        if not re.fullmatch(r"[0-9a-f-]{36}", value["key_id"]):
            raise Stop("remote_validation")
        return value
    stop_fields = {"status", "stage", "candidate_id", "candidate_running", "key_id", "created",
                   "stored", "store_removed", "failure_category", "http_status",
                   "rollback_attempted", "key_inactive_readback"}
    if isinstance(value, dict) and value.get("status") == "CANDIDATE_KEY_R4_UNKNOWN":
        if (returncode == 0 or set(value) != stop_fields or value["stage"] != "native_dispatch"
                or value["failure_category"] not in {"child_timeout", "child_output", "remote_envelope"}
                or any(value[name] is not None for name in stop_fields - {"status", "stage", "failure_category"})):
            raise Stop("remote_validation")
        return value
    if not isinstance(value, dict) or set(value) != stop_fields or value["status"] != "CANDIDATE_KEY_R4_STOP":
        raise Stop("remote_validation")
    if value["stage"] not in {"identity", "store_preflight", "native", "native_preflight", "provider_preflight", "create", "patch", "readback", "db_readback", "store", "result"}:
        raise Stop("remote_validation")
    if value["candidate_id"] != candidate_id or value["candidate_running"] is not (None if value["stage"] == "identity" else True):
        raise Stop("remote_validation")
    if value["failure_category"] not in {"validation", "http_4xx", "http_5xx", "http_other", "timeout", "connection", "output_limit", "child_timeout", "child_output"}:
        raise Stop("remote_validation")
    if value["key_id"] is not None and not re.fullmatch(r"[0-9a-f-]{36}", value["key_id"]):
        raise Stop("remote_validation")
    if any(type(value[key]) is not bool for key in ("created", "stored", "rollback_attempted")):
        raise Stop("remote_validation")
    if value["store_removed"] not in (None, True, False) or value["key_inactive_readback"] not in (None, True, False):
        raise Stop("remote_validation")
    if value["http_status"] is not None and (type(value["http_status"]) is not int or not 100 <= value["http_status"] <= 599):
        raise Stop("remote_validation")
    if value["stored"] and not value["created"] or value["store_removed"] is not None and not value["stored"]:
        raise Stop("remote_validation")
    if value["key_inactive_readback"] is True and not value["rollback_attempted"]:
        raise Stop("remote_validation")
    return value


def render_node(admin):
    value = NODE_TEMPLATE
    replacements = {"__ADMIN_B64__": base64.b64encode(admin.encode()).decode(), "__NAME__": json.dumps(KEY_NAME),
                    "__CODEX__": json.dumps(CODEX_CONNECTION), "__MODELS__": json.dumps(MODELS, separators=(",", ":")),
                    "__CONNECTIONS__": json.dumps(CONNECTIONS, separators=(",", ":")),
                    "__SENTINEL__": json.dumps(COMBO_SENTINEL), "__PATCH__": json.dumps(patch_body(), separators=(",", ":"))}
    for marker, replacement in replacements.items():
        if value.count(marker) != 1: raise Stop("local_validation")
        value = value.replace(marker, replacement)
    return value


def render_remote(admin, candidate_id=None):
    candidate_id = candidate_id or CANDIDATE_ID
    if not re.fullmatch(r"[0-9a-f]{64}", candidate_id): raise Stop("pending_candidate_id")
    transport = load_transport()
    node = render_node(admin)
    rollback = ROLLBACK_TEMPLATE.replace("__ADMIN_B64__", base64.b64encode(admin.encode()).decode()).replace("__NAME__", json.dumps(KEY_NAME))
    values = {"__BOUNDED_CAPTURE__": inspect.getsource(transport.bounded_capture), "__LIVE_ID__": repr(LIVE_ID),
              "__LIVE_IMAGE__": repr(LIVE_IMAGE), "__LIVE_VOLUME__": repr(LIVE_VOLUME),
              "__CANDIDATE__": repr(CANDIDATE_NAME), "__CANDIDATE_ID__": repr(candidate_id),
              "__VOLUME__": repr(CANDIDATE_VOLUME), "__IMAGE__": repr(IMAGE), "__TAG__": repr(TAG),
              "__SOURCE__": repr(SOURCE), "__KEY_NAME__": repr(KEY_NAME), "__STORE__": repr(OPERATOR_STORE),
              "__NODE__": repr(node), "__ROLLBACK__": repr(rollback)}
    value = REMOTE_TEMPLATE
    for marker, replacement in values.items():
        if value.count(marker) != 1: raise Stop("local_validation")
        value = value.replace(marker, replacement)
    ast.parse(value)
    return value.encode()


def load_transport():
    if not regular(TRANSPORT) or digest(TRANSPORT) != TRANSPORT_SHA256: raise Stop("local_validation")
    spec = importlib.util.spec_from_file_location("candidate_key_r4_transport", TRANSPORT)
    module = importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module


def parse_receipt(path):
    value = json.loads(pathlib.Path(path).read_text("utf-8"))
    if not isinstance(value, dict): raise Stop("local_validation")
    return value


def validate_reconciliation(value, candidate_id):
    if not isinstance(value, dict) or set(value) != {"schema", "status", "stage", "remote"} or value["status"] != "PASS" or value["stage"] != "complete":
        raise Stop("local_validation")
    remote = value["remote"]
    if not isinstance(remote, dict) or remote.get("status") != "CANDIDATE_RECONCILE_R2_PASS" or remote.get("candidate_id") != candidate_id or remote.get("candidate_image") != IMAGE or remote.get("candidate_volume") != CANDIDATE_VOLUME or remote.get("source_revision") != SOURCE:
        raise Stop("local_validation")
    required = ("candidate_present", "volume_present", "candidate_running", "can_enter_hardware_preflight_without_restart", "identity_verified", "image_verified", "volume_verified", "network_none", "published_ports_zero", "user_node", "mount_exact", "readonly_root", "cap_drop_all", "no_new_privileges", "restart_no", "tmpfs_hardened", "live_unchanged", "retained_candidates_unchanged")
    if remote.get("state_status") != "running" or remote.get("docker_health_status") != "healthy" or any(remote.get(key) is not True for key in required):
        raise Stop("local_validation")
    if any(remote.get(key) is not False for key in ("environment_checked", "historical_startup_reconstructed", "database_checked", "native_health_checked")):
        raise Stop("local_validation")
    return value


def fixed_dependencies():
    return ((BINDINGS, BINDINGS_SHA256), (TRANSPORT, TRANSPORT_SHA256),
            (SPENT_START_RESULT, SPENT_START_RESULT_SHA256), (SPENT_RECONCILE_RESULT, SPENT_RECONCILE_RESULT_SHA256),
            (RECONCILIATION_RESULT, RECONCILIATION_RESULT_SHA256))


def offline_check():
    if not EXECUTION_READY or require_bound(): raise Stop("local_validation")
    if not all(regular(path) and digest(path) == expected for path, expected in fixed_dependencies()): raise Stop("local_validation")
    if RESULT.exists() or RESULT.is_symlink(): raise Stop("stale_result")
    if len(MODELS) != 14 or len(set(MODELS)) != 14 or len(CONNECTIONS) != 5 or len(set(CONNECTIONS)) != 5: raise Stop("local_validation")
    bindings=json.loads(BINDINGS.read_text("utf-8"));flat=[]
    for rows in bindings.values():flat.extend(rows if isinstance(rows,list) else [rows])
    if set(CONNECTIONS)!={row["connectionId"] for row in flat} or set(MODELS[2:])!={row["provider"]+"/"+row["model"] for row in flat}:raise Stop("local_validation")
    node=render_node("oma_fixture_secret");payload=render_remote("oma_fixture_secret",FIXTURE_CANDIDATE_ID)
    if b"oma_fixture_secret" in payload or b"bounded_capture" not in payload:raise Stop("local_validation")
    for forbidden in (b"container','start",b"container','stop",b"container','restart",b"container','rm",b"volume','rm",b"/v1/chat",b"/v1/models"):
        if forbidden in payload:raise Stop("local_validation")
    if node.count("stage='create';r=await request('POST','/api/keys'")!=1 or node.count("stage='patch';r=await request('PATCH','/api/keys/'+keyId,PATCH)")!=1 or OPERATOR_STORE.encode() not in payload:raise Stop("local_validation")
    validate_reconciliation(parse_receipt(RECONCILIATION_RESULT),CANDIDATE_ID)
    validate_result(fixture_result(),0,FIXTURE_CANDIDATE_ID)
    print("CANDIDATE_KEY_R4_PREPARATION_PASS")


def review_payload():
    if not EXECUTION_READY or require_bound(): raise Stop("pending_bindings")
    paths = [path for path, _ in fixed_dependencies()] + [CONTRACT, RECONCILIATION_RESULT]
    if not all(regular(path) for path in paths): raise Stop("local_validation")
    return {"schema":"auto-switch-candidate-key-r4-review/v1","launcher_sha256":digest(pathlib.Path(__file__)),
            "contract_sha256":digest(CONTRACT),"bindings_sha256":digest(BINDINGS),"transport_sha256":digest(TRANSPORT),
            "spent_start_result_sha256":digest(SPENT_START_RESULT),"spent_reconcile_result_sha256":digest(SPENT_RECONCILE_RESULT),
            "reconciliation_result_sha256":digest(RECONCILIATION_RESULT),"candidate_id":CANDIDATE_ID,
            "candidate_image":IMAGE,"candidate_name":CANDIDATE_NAME,"candidate_volume":CANDIDATE_VOLUME,
            "key_name":KEY_NAME,"operator_store":OPERATOR_STORE,"models":MODELS,"connections":CONNECTIONS}


def reserve_result():
    if RESULT.exists() or RESULT.is_symlink():raise Stop("stale_result")
    return os.open(RESULT,os.O_WRONLY|os.O_CREAT|os.O_EXCL|getattr(os,"O_BINARY",0),0o600)


def finish_result(fd,value):
    raw=(json.dumps(value,sort_keys=True,separators=(",",":"))+"\n").encode()
    if len(raw)>RESULT_LIMIT:raise Stop("local_validation")
    try:
        offset=0
        while offset<len(raw):
            written=os.write(fd,raw[offset:])
            if written<=0:raise OSError("result_write")
            offset+=written
        os.fsync(fd)
    finally:os.close(fd)


def execute(reviewed):
    if not EXECUTION_READY or require_bound():raise Stop("pending_bindings")
    if not all(regular(path) and digest(path)==expected for path,expected in fixed_dependencies()):raise Stop("local_validation")
    if not regular(RECONCILIATION_RESULT) or digest(RECONCILIATION_RESULT)!=RECONCILIATION_RESULT_SHA256:raise Stop("local_validation")
    validate_reconciliation(parse_receipt(RECONCILIATION_RESULT),CANDIDATE_ID)
    if not regular(reviewed) or json.loads(reviewed.read_text("utf-8"))!=review_payload():raise Stop("review_pin_mismatch")
    if "PROGRAMDATA" not in {key.upper() for key in os.environ}:raise Stop("local_validation")
    fd=reserve_result();receipt={"schema":RESULT_SCHEMA,"status":"UNKNOWN","stage":"transport","remote":None}
    try:
        admin=os.environ.get("OMNIROUTE_ADMIN_TOKEN","")
        if not re.fullmatch(r"oma_[A-Za-z0-9._~-]{16,512}",admin):raise Stop("local_validation")
        payload=render_remote(admin);transport=load_transport();command=[transport.SSH,"-T",*transport.options("192.168.1.68"),"belladmin@192.168.1.68","sudo -n python3 -"]
        saved=os.environ.pop("OMNIROUTE_ADMIN_TOKEN",None)
        try:rc,out,err=transport.bounded_capture(command,payload,300)
        except RuntimeError as error:raise Stop("transport") from error
        finally:
            if saved is not None:os.environ["OMNIROUTE_ADMIN_TOKEN"]=saved
        if err:raise Stop("remote_validation")
        try:value=validate_result(json.loads(out),rc)
        except Exception as error:raise Stop("remote_validation") from error
        status="PASS" if rc==0 else ("UNKNOWN" if value["status"]=="CANDIDATE_KEY_R4_UNKNOWN" else "STOP")
        receipt={"schema":RESULT_SCHEMA,"status":status,"stage":"complete" if rc==0 else value["stage"],"remote":value}
        print(json.dumps(value,sort_keys=True));return 0 if rc==0 else 1
    except Stop as error:
        if str(error) not in {"transport","remote_validation"}:
            receipt={"schema":RESULT_SCHEMA,"status":"STOP","stage":"local_validation","remote":None}
        raise
    finally:finish_result(fd,receipt)


def main():
    parser=argparse.ArgumentParser();parser.add_argument("--self-check",action="store_true");parser.add_argument("--render-review-payload",action="store_true");parser.add_argument("--execute-reviewed",type=pathlib.Path);args=parser.parse_args()
    if sum((args.self_check,args.render_review_payload,bool(args.execute_reviewed)))!=1:raise Stop("local_validation")
    if args.self_check:offline_check();return 0
    if args.render_review_payload:print(json.dumps(review_payload(),indent=2,sort_keys=True));return 0
    return execute(args.execute_reviewed)


if __name__=="__main__":
    try:raise SystemExit(main())
    except Exception as error:
        stage=str(error) if str(error) in {"pending_bindings","stale_result","transport","remote_validation"} else "local_validation"
        print(json.dumps({"status":"CANDIDATE_KEY_R4_NOT_EXECUTABLE","stage":stage,"execution_ready":False},sort_keys=True));raise SystemExit(1)
