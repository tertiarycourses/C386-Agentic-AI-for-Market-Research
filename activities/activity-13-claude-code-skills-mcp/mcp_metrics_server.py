"""Read-only MCP stdio server;synthetic CSV only,no network or secrets.
Protocol version2024-11-05;newline-delimited JSON-RPC messages.
Only read_synthetic_metrics is exposed. No writes,deletion or external calls.
"""
import sys,json,csv
from pathlib import Path
root=Path(__file__).resolve().parent
for line in sys.stdin:
 try:
  request=json.loads(line);method=request.get('method');rid=request.get('id')
  if rid is None:continue
  if method=='initialize':
   result={'protocolVersion':'2024-11-05','capabilities':{'tools':{}},'serverInfo':{'name':'synthetic-market-metrics','version':'1.0.0'}}
  elif method=='ping':result={}
  elif method=='tools/list':
   result={'tools':[{'name':'read_synthetic_metrics','description':'Read four fictional channel metric rows;read-only,no network.','inputSchema':{'type':'object','properties':{},'additionalProperties':False}}]}
  elif method=='tools/call' and request.get('params',{}).get('name')=='read_synthetic_metrics':
   with (root/'mock-data/tool-results.csv').open() as f:rows=list(csv.DictReader(f))
   result={'content':[{'type':'text','text':json.dumps({'synthetic':True,'source':'mock-data/tool-results.csv','rows':rows})}],'isError':False}
  else:
   print(json.dumps({'jsonrpc':'2.0','id':rid,'error':{'code':-32601,'message':'Method or tool not allowed'}}),flush=True);continue
  print(json.dumps({'jsonrpc':'2.0','id':rid,'result':result}),flush=True)
 except Exception as e:
  print(json.dumps({'jsonrpc':'2.0','id':None,'error':{'code':-32603,'message':type(e).__name__}}),flush=True)
