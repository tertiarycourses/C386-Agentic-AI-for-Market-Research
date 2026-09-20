"""Deterministic local calculation baseline using only synthetic CSV inputs.
Writes verification.json under outputs;never changes raw data or uses network.
"""
import csv,json,math
from collections import Counter,defaultdict
from pathlib import Path
root=Path(__file__).resolve().parent
with (root/'mock-data'/'measurement-plan.csv').open() as f:rows=list(csv.DictReader(f))
assert len(rows)==4
assert set(['event_name', 'trigger', 'required_parameter', 'purpose', 'key_event'])<=set(rows[0])
names={r['event_name'] for r in rows}
assert names=={'page_view','generate_lead','purchase','view_item'}
assert all(r['trigger'] for r in rows)
contract=json.loads((root/'assets'/'purchase-contract.json').read_text())
required={'transaction_id','currency','value','items'}
assert required<=set(contract['params'])
for field in contract['params']:
    assert field not in {'email','phone','name','address'}
result={'event_names':sorted(names),'purchase_required_fields':sorted(required),'live_collection_executed':False}
output=root/'outputs';output.mkdir(exist_ok=True)
temporary=output/'verification.build-tmp.json'
temporary.write_text(json.dumps(result,indent=2))
temporary.replace(output/'verification.json')
print(json.dumps(result,indent=2))
