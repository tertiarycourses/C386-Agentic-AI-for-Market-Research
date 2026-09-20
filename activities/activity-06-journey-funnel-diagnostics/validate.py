"""Deterministic local calculation baseline using only synthetic CSV inputs.
Writes verification.json under outputs;never changes raw data or uses network.
"""
import csv,json,math
from collections import Counter,defaultdict
from pathlib import Path
root=Path(__file__).resolve().parent
with (root/'mock-data'/'funnel.csv').open() as f:rows=list(csv.DictReader(f))
assert len(rows)==4
assert set(['stage', 'count', 'cohort', 'window'])<=set(rows[0])
with (root/'mock-data/journey-events.csv').open() as f:events=list(csv.DictReader(f))
stages=['landing_session','enquiry','qualified_lead','enrolment']
sets={stage:{r['session_id'] for r in events if r['event_name']==stage} for stage in stages}
assert all(sets[b]<=sets[a] for a,b in zip(stages,stages[1:]))
by_session=defaultdict(dict)
for r in events:by_session[r['session_id']][r['event_name']]=r['timestamp']
for sid,times in by_session.items():
    sequence=[times[stage] for stage in stages if stage in times]
    assert sequence==sorted(sequence)
counts=[len(sets[stage]) for stage in stages]
assert counts==[2400,96,48,12]
rates=[b/a for a,b in zip(counts,counts[1:])]
overall=counts[-1]/counts[0]
assert rates==[0.04,0.5,0.25] and overall==0.005
result={'validated_session_counts':counts,'stage_rates':rates,'overall_rate':overall,'row_level_order_verified':True,'limitation':'Synthetic session cohort;does not establish customer motivation or causality'}
output=root/'outputs';output.mkdir(exist_ok=True)
temporary=output/'verification.build-tmp.json'
temporary.write_text(json.dumps(result,indent=2))
temporary.replace(output/'verification.json')
print(json.dumps(result,indent=2))
