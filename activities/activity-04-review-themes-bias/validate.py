"""Deterministic local calculation baseline using only synthetic CSV inputs.
Writes verification.json under outputs;never changes raw data or uses network.
"""
import csv,json,math
from collections import Counter,defaultdict
from pathlib import Path
root=Path(__file__).resolve().parent
with (root/'mock-data'/'reviews.csv').open() as f:rows=list(csv.DictReader(f))
assert len(rows)==8
assert set(['review_id', 'segment', 'text', 'theme_reference'])<=set(rows[0])
coded=[]
for r in rows:
    text=r['text'].lower()
    theme='timing' if 'timing' in text else ('relevance' if 'relevant' in text else 'support')
    mixed=('but' in text)
    coded.append({'review_id':r['review_id'],'theme':theme,'mixed':mixed})
counts=dict(Counter(r['theme'] for r in coded))
assert counts=={'timing':3,'relevance':3,'support':2}
assert coded[-1]['mixed'] is True
result={'coded_rows':coded,'theme_counts':counts,'limitation':'Rule baseline;human review and volunteer selection bias remain'}
output=root/'outputs';output.mkdir(exist_ok=True)
temporary=output/'verification.build-tmp.json'
temporary.write_text(json.dumps(result,indent=2))
temporary.replace(output/'verification.json')
print(json.dumps(result,indent=2))
