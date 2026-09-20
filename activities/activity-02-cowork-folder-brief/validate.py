"""Deterministic local calculation baseline using only synthetic CSV inputs.
Writes verification.json under outputs;never changes raw data or uses network.
"""
import csv,json,math
from collections import Counter,defaultdict
from pathlib import Path
root=Path(__file__).resolve().parent
with (root/'mock-data'/'campaign-files.csv').open() as f:rows=list(csv.DictReader(f))
assert len(rows)==4
assert set(['file_id', 'filename', 'owner', 'period', 'row_count', 'status'])<=set(rows[0])
approved=[r['file_id'] for r in rows if r['status']=='approved']
quarantined=[r['file_id'] for r in rows if r['status']=='untrusted']
coverage=len(approved)/len(rows)
assert approved==['F01','F02','F03'] and quarantined==['F04']
assert math.isclose(coverage,0.75)
result={'approved_ids':approved,'quarantined_ids':quarantined,'coverage':coverage}
output=root/'outputs';output.mkdir(exist_ok=True)
temporary=output/'verification.build-tmp.json'
temporary.write_text(json.dumps(result,indent=2))
temporary.replace(output/'verification.json')
print(json.dumps(result,indent=2))
