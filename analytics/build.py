from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from mismatch import ROOT, VOCAB, tokens, load_catalog, score_row, write_json

def build():
    rows = load_catalog()
    flags = sum(score_row(r)['flag'] for r in rows)
    write_json(ROOT / 'analytics/rates.json', {'overall_flag_rate':flags/len(rows) if rows else None,'n':len(rows),'denominator':len(rows),'flagged_count':flags,'population':'all synthetic catalog fixtures'})
    terms = [t for r in rows for t in tokens(r['title']+' '+r['description'])]
    covered = sum(t in VOCAB for t in terms)
    missing = sorted(set(terms)-set(VOCAB))
    write_json(ROOT / 'analytics/vocab_gaps.json', {'token_count':len(terms),'covered_token_count':covered,'token_coverage':covered/len(terms) if terms else None,'missing_vocabulary':missing,'fields':['title','description'],'limitations':'English ASCII tokenization; no semantic or multilingual coverage; transcript excluded'})
if __name__ == '__main__':
    build()
