"""Deterministic local calculation baseline using only synthetic CSV inputs.
Writes verification.json under outputs;never changes raw data or uses network.
"""
import csv,json,math
from collections import Counter,defaultdict
from pathlib import Path
root=Path(__file__).resolve().parent
with (root/'mock-data'/'segments.csv').open() as f:rows=list(csv.DictReader(f))
assert len(rows)==3
assert set(['segment', 'customers', 'revenue_sgd', 'cost_sgd', 'retention'])<=set(rows[0])
values={r['segment']:(float(r['revenue_sgd'])-float(r['cost_sgd']))/int(r['customers']) for r in rows}
total=sum(int(r['customers']) for r in rows)
assert list(values.values())==[300,200,500] and total==80
result={'margin_per_customer':values,'total_customers':total,'retained_margin_assumption':values[rows[0]['segment']]*float(rows[0]['retention'])}
output=root/'outputs';output.mkdir(exist_ok=True)
temporary=output/'verification.build-tmp.json'
temporary.write_text(json.dumps(result,indent=2))
temporary.replace(output/'verification.json')
print(json.dumps(result,indent=2))
