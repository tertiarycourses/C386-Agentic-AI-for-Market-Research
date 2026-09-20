"""Deterministic local calculation baseline using only synthetic CSV inputs.
Writes verification.json under outputs;never changes raw data or uses network.
"""
import csv,json,math
from collections import Counter,defaultdict
from pathlib import Path
root=Path(__file__).resolve().parent
with (root/'mock-data'/'tool-results.csv').open() as f:rows=list(csv.DictReader(f))
assert len(rows)==4
assert set(['channel', 'sessions', 'leads', 'source_id'])<=set(rows[0])
rates={r['channel']:int(r['leads'])/int(r['sessions']) for r in rows}
overall=sum(int(r['leads']) for r in rows)/sum(int(r['sessions']) for r in rows)
assert list(rates.values())==[0.05,0.04,0.08,0.01] and overall==0.04
result={'channel_lead_rates':rates,'overall':overall,'source_ids':[r['source_id'] for r in rows],'transport':'local_csv_baseline'}
output=root/'outputs';output.mkdir(exist_ok=True)
temporary=output/'verification.build-tmp.json'
temporary.write_text(json.dumps(result,indent=2))
temporary.replace(output/'verification.json')
print(json.dumps(result,indent=2))
