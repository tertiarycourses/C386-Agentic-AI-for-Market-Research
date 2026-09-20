"""Exercise actual local MCP initialize,list and read-only tools-call messages."""
import subprocess,json,sys
from pathlib import Path
root=Path(__file__).resolve().parent
requests=[{'jsonrpc':'2.0','id':1,'method':'initialize','params':{'protocolVersion':'2024-11-05','capabilities':{},'clientInfo':{'name':'training-verifier','version':'1.0'}}},{'jsonrpc':'2.0','method':'notifications/initialized'},{'jsonrpc':'2.0','id':2,'method':'tools/list'},{'jsonrpc':'2.0','id':3,'method':'tools/call','params':{'name':'read_synthetic_metrics','arguments':{}}}]
result=subprocess.run([sys.executable,str(root/'mcp_metrics_server.py')],input=''.join(json.dumps(r)+'\n' for r in requests),text=True,capture_output=True,check=True)
responses=[json.loads(line) for line in result.stdout.splitlines()]
assert len(responses)==3
assert responses[0]['result']['serverInfo']['name']=='synthetic-market-metrics'
assert responses[1]['result']['tools'][0]['name']=='read_synthetic_metrics'
metrics=json.loads(responses[2]['result']['content'][0]['text'])
assert metrics['synthetic'] is True and len(metrics['rows'])==4
assert [r['source_id'] for r in metrics['rows']]==['M01','M02','M03','M04']
(root/'outputs').mkdir(exist_ok=True)
(root/'outputs/mcp-verification.json').write_text(json.dumps({'transport':'actual_local_stdio_jsonrpc','responses':responses,'live_account_connected':False},indent=2))
print('PASS:actual local initialize,tools/list,tools/call;4synthetic rows;no live account.')
