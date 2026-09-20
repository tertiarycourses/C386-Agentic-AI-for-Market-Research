"""Deterministic local calculation baseline using only synthetic CSV inputs.
Writes verification.json under outputs;never changes raw data or uses network.
"""
import csv,json,math
from collections import Counter,defaultdict
from pathlib import Path
root=Path(__file__).resolve().parent
with (root/'mock-data'/'campaigns.csv').open() as f:rows=list(csv.DictReader(f))
assert len(rows)==4
assert set(['channel', 'spend_sgd', 'leads', 'revenue_sgd', 'gross_margin_rate'])<=set(rows[0])
values={}
for r in rows:
    spend=float(r['spend_sgd']);revenue=float(r['revenue_sgd']);leads=int(r['leads']);margin=float(r['gross_margin_rate'])
    values[r['channel']]={'cpl':spend/leads,'revenue_roas':revenue/spend if spend else None,'contribution_after_spend':revenue*margin-spend}
total_leads=sum(int(r['leads']) for r in rows);spend=sum(float(r['spend_sgd']) for r in rows);revenue=sum(float(r['revenue_sgd']) for r in rows)
contribution=sum(v['contribution_after_spend'] for v in values.values())
assert (total_leads,spend,revenue,contribution)==(96,2100,6000,900)
assert values['Paid search']=={'cpl':40,'revenue_roas':2,'contribution_after_spend':0}
result={'channel_metrics':values,'totals':{'leads':total_leads,'spend':spend,'revenue':revenue,'contribution':contribution},'approval':'pending','causal_roi_estimated':False}
output=root/'outputs';output.mkdir(exist_ok=True)
temporary=output/'verification.build-tmp.json'
temporary.write_text(json.dumps(result,indent=2))
temporary.replace(output/'verification.json')
print(json.dumps(result,indent=2))
