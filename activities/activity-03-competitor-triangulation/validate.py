"""Deterministic local calculation baseline using only synthetic CSV inputs.
Writes verification.json under outputs;never changes raw data or uses network.
"""
import csv,json,math
from collections import Counter,defaultdict
from pathlib import Path
root=Path(__file__).resolve().parent
with (root/'mock-data'/'competitors.csv').open() as f:rows=list(csv.DictReader(f))
assert len(rows)==3
assert set(['competitor', 'price_sgd', 'hours', 'review_n', 'rating', 'claim_id'])<=set(rows[0])
values={r['competitor']:float(r['price_sgd'])/float(r['hours']) for r in rows}
assert list(values.values())==[60,45,50]
result={'sgd_per_hour':values,'claim_ids':[r['claim_id'] for r in rows],'limitation':'Fictional competitor offers;not willingness to pay'}
output=root/'outputs';output.mkdir(exist_ok=True)
temporary=output/'verification.build-tmp.json'
temporary.write_text(json.dumps(result,indent=2))
temporary.replace(output/'verification.json')
print(json.dumps(result,indent=2))
