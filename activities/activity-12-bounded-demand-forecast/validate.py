"""Deterministic local calculation baseline using only synthetic CSV inputs.
Writes verification.json under outputs;never changes raw data or uses network.
"""
import csv,json,math
from collections import Counter,defaultdict
from pathlib import Path
root=Path(__file__).resolve().parent
with (root/'mock-data'/'demand.csv').open() as f:rows=list(csv.DictReader(f))
assert len(rows)==6
assert set(['month', 'enquiries', 'campaign_change'])<=set(rows[0])
values=[int(r['enquiries']) for r in rows]
aug_naive=values[4];aug_ma=sum(values[2:5])/3
naive_error=abs(values[5]-aug_naive);ma_error=abs(values[5]-aug_ma)
sep_naive=values[-1];sep_ma=sum(values[-3:])/3
assert sep_naive==104 and sep_ma==100
assert naive_error==4 and math.isclose(ma_error,10.66666666666667)
result={'september_naive':sep_naive,'september_ma':sep_ma,'august_naive_error':naive_error,'august_ma_error':ma_error,'annual_seasonality_established':False}
output=root/'outputs';output.mkdir(exist_ok=True)
temporary=output/'verification.build-tmp.json'
temporary.write_text(json.dumps(result,indent=2))
temporary.replace(output/'verification.json')
print(json.dumps(result,indent=2))
