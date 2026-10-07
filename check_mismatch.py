from mismatch import ROOT, load_catalog, score_row
import json

def check():
    report = json.loads((ROOT / 'mismatch_report.json').read_text())
    expected = [score_row(r) for r in load_catalog()]
    if report != expected:
        raise ValueError('Stale mismatch report: rerun mismatch.py')
    rows = {r['sku']:r for r in report}
    if rows['KND-01']['flag'] or not rows['NK-99']['flag']:
        raise ValueError('Gold checks failed')
    print('KND-01 clear\nNK-99 flagged')
if __name__ == '__main__':
    check()
