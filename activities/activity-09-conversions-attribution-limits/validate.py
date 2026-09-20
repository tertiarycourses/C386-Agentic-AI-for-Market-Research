"""Deterministic local calculation baseline using only synthetic CSV inputs.
Writes verification.json under outputs;never changes raw data or uses network.
"""
import csv,json,math
from collections import Counter,defaultdict
from pathlib import Path
root=Path(__file__).resolve().parent
with (root/'mock-data'/'touchpoints.csv').open() as f:rows=list(csv.DictReader(f))
assert len(rows)==4
assert set(['journey_id', 'first_channel', 'last_channel', 'revenue_sgd'])<=set(rows[0])
first=defaultdict(float);last=defaultdict(float)
for r in rows:
    value=float(r['revenue_sgd'])
    first[r['first_channel']]+=value;last[r['last_channel']]+=value
total=sum(float(r['revenue_sgd']) for r in rows)
assert sum(first.values())==sum(last.values())==total==2400
assert first['Paid search']==1200 and last['Email']==1300
result={'first_touch':dict(first),'last_touch':dict(last),'total':total,'causal_lift_estimated':False}
output=root/'outputs';output.mkdir(exist_ok=True)
temporary=output/'verification.build-tmp.json'
temporary.write_text(json.dumps(result,indent=2))
temporary.replace(output/'verification.json')
print(json.dumps(result,indent=2))
