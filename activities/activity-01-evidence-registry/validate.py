"""Deterministic local calculation baseline using only synthetic CSV inputs.
Writes verification.json under outputs;never changes raw data or uses network.
"""
import csv,json,math
from collections import Counter,defaultdict
from pathlib import Path
root=Path(__file__).resolve().parent
with (root/'mock-data'/'sources.csv').open() as f:rows=list(csv.DictReader(f))
assert len(rows)==4
assert set(['source_id', 'source_type', 'published_date', 'population', 'sample_n', 'claim', 'confidence'])<=set(rows[0])
counts={r['source_id']:int(r['sample_n']) for r in rows}
evening=int(rows[0]['claim'].split()[0])/counts['S01']
enquiry=int(rows[1]['claim'].split()[0])/counts['S02']
assert math.isclose(evening,0.6) and math.isclose(enquiry,0.45)
result={'source_count':len(rows),'evening_survey_rate':evening,'evening_enquiry_rate':enquiry,'limitation':'Different synthetic populations;not market size'}
output=root/'outputs';output.mkdir(exist_ok=True)
temporary=output/'verification.build-tmp.json'
temporary.write_text(json.dumps(result,indent=2))
temporary.replace(output/'verification.json')
print(json.dumps(result,indent=2))
