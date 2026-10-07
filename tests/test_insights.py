import unittest,json,copy
from mismatch import ROOT,load_catalog
from insights import insight
class InsightsTests(unittest.TestCase):
    def test_artifact_and_title_preserved(self):
        rows=load_catalog(); before=copy.deepcopy(rows)
        expected=[insight(r) for r in rows]
        self.assertEqual(rows,before)
        self.assertEqual(json.loads((ROOT/'insights.json').read_text()),expected)
        self.assertIn('transcript',expected[0])
        self.assertTrue(all(r['seller_message'] for r in expected))
    def test_transcript_escape_rejected(self):
        row=load_catalog()[0]; row['transcript_path']='../README.md'
        with self.assertRaises(ValueError): insight(row)
