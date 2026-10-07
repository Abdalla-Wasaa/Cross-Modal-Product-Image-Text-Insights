import argparse
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from mismatch import bow, tokens, cosine, load_catalog

def search(query, catalog, k=3):
    if isinstance(k, bool) or not isinstance(k, int) or k < 1:
        raise ValueError('k must be a positive integer')
    vector = bow(tokens(query))
    results = [{'sku':r['sku'], 'score':round(cosine(vector,bow(tokens(' '.join(r['image_tags'])))),6)} for r in catalog]
    return sorted((r for r in results if r['score'] > 0), key=lambda r:(-r['score'],r['sku']))[:k]
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('query')
    parser.add_argument('-k', type=int, default=3)
    args = parser.parse_args()
    print(search(args.query, load_catalog(), args.k))
