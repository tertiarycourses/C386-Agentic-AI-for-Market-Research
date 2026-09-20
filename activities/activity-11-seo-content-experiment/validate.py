"""Deterministic local calculation baseline using only synthetic CSV inputs.
Writes verification.json under outputs;never changes raw data or uses network.
"""
import csv,json,math
from collections import Counter,defaultdict
from pathlib import Path
root=Path(__file__).resolve().parent
with (root/'mock-data'/'search-content.csv').open() as f:rows=list(csv.DictReader(f))
assert len(rows)==4
assert set(['query', 'impressions', 'clicks', 'enquiries', 'intent'])<=set(rows[0])
values={r['query']:{'ctr':int(r['clicks'])/int(r['impressions']),'enquiry_per_click':int(r['enquiries'])/int(r['clicks'])} for r in rows}
assert [v['ctr'] for v in values.values()]==[0.04,0.03,0.06,0.03]
assert values['market research training']['enquiry_per_click']==0.125
result={'query_rates':values,'ranking_or_lift_guaranteed':False}
output=root/'outputs';output.mkdir(exist_ok=True)
temporary=output/'verification.build-tmp.json'
temporary.write_text(json.dumps(result,indent=2))
temporary.replace(output/'verification.json')
print(json.dumps(result,indent=2))
