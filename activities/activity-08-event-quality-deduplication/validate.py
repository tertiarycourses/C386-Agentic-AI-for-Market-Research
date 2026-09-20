"""Deterministic local calculation baseline using only synthetic CSV inputs.
Writes verification.json under outputs;never changes raw data or uses network.
"""
import csv,json,math
from collections import Counter,defaultdict
from pathlib import Path
root=Path(__file__).resolve().parent
with (root/'mock-data'/'events.csv').open() as f:rows=list(csv.DictReader(f))
assert len(rows)==5
assert set(['event_id', 'event_name', 'transaction_id', 'value', 'currency'])<=set(rows[0])
raw=sum(float(r['value']) for r in rows if r['event_name']=='purchase')
seen=set();valid=[];quarantine=[]
for r in rows:
    if r['event_name']!='purchase':continue
    tid=r['transaction_id']
    reason='missing_id' if not tid else ('duplicate' if tid in seen else None)
    if reason:quarantine.append({'event_id':r['event_id'],'reason':reason,'value':float(r['value'])})
    else:valid.append(r);seen.add(tid)
accepted=sum(float(r['value']) for r in valid)
assert raw==2100 and accepted==1100
assert raw==accepted+sum(r['value'] for r in quarantine)
assert [r['event_id'] for r in quarantine]==['E02','E04']
result={'raw_purchase_value':raw,'accepted_value':accepted,'quarantine':quarantine,'live_ga4_test_executed':False}
output=root/'outputs';output.mkdir(exist_ok=True)
temporary=output/'verification.build-tmp.json'
temporary.write_text(json.dumps(result,indent=2))
temporary.replace(output/'verification.json')
print(json.dumps(result,indent=2))
