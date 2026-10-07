"""Manual image-tag/text cosine fallback; no pixels are encoded."""
import json
import math
import re
from pathlib import Path
ROOT = Path(__file__).resolve().parent
VOCAB = ('kiondo','bag','sisal','navy','woven','nike','white','sports','training','red','leso','cloth')
THRESHOLD = 0.50

def tokens(text):
    return re.findall(r"[a-z0-9]+", text.lower())

def bow(words):
    return [words.count(term) for term in VOCAB]

def cosine(a, b):
    norm = math.sqrt(sum(x*x for x in a)*sum(y*y for y in b))
    return sum(x*y for x,y in zip(a,b))/norm if norm else 0.0

def load_catalog(path=ROOT / 'catalog.json'):
    rows = json.loads(Path(path).read_text())
    seen = set()
    for row in rows:
        if not row.get('sku') or row['sku'] in seen:
            raise ValueError('Missing or duplicate SKU')
        seen.add(row['sku'])
        if not isinstance(row.get('image_tags'), list) or not row['image_tags']:
            raise ValueError('Manual image annotations required')
        for field in ('title', 'description', 'image'):
            if not isinstance(row.get(field), str) or not row[field].strip():
                raise ValueError(f'Missing {field}')
        image = (ROOT / row['image']).resolve()
        if ROOT / 'images' not in image.parents or not image.is_file():
            raise ValueError('Image must exist inside images/')
    return rows

def score_row(row):
    text = tokens(row['title'] + ' ' + row['description'])
    score = cosine(bow(tokens(' '.join(row['image_tags']))), bow(text))
    return {'sku':row['sku'], 'score':round(score,6), 'flag':score < THRESHOLD}

def write_json(path, value):
    Path(path).write_text(json.dumps(value, indent=2) + '\n')

if __name__ == '__main__':
    report = [score_row(r) for r in load_catalog()]
    write_json(ROOT / 'mismatch_report.json', report)
    print(json.dumps(report, indent=2))
