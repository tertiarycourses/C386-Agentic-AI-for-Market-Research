"""Deterministic local calculation baseline using only synthetic CSV inputs.
Writes verification.json under outputs;never changes raw data or uses network.
"""
import csv,json,math
from collections import Counter,defaultdict
from pathlib import Path
root=Path(__file__).resolve().parent
with (root/'mock-data'/'lifecycle.csv').open() as f:rows=list(csv.DictReader(f))
assert len(rows)==3
assert set(['segment', 'eligible', 'sent', 'clicked', 'enrolled'])<=set(rows[0])
values={r['segment']:{'click_rate':int(r['clicked'])/int(r['sent']),'enrolment_per_sent':int(r['enrolled'])/int(r['sent'])} for r in rows}
assert [v['click_rate'] for v in values.values()]==[0.2,0.3,0.2]
assert [v['enrolment_per_sent'] for v in values.values()]==[0.05,0.15,0.1]
result={'segment_rates':values,'send_authorised':False,'incremental_effect_estimated':False}
output=root/'outputs';output.mkdir(exist_ok=True)
temporary=output/'verification.build-tmp.json'
temporary.write_text(json.dumps(result,indent=2))
temporary.replace(output/'verification.json')
print(json.dumps(result,indent=2))
