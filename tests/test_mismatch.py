import unittest
from mismatch import load_catalog, score_row, cosine, ROOT
from check_mismatch import check
class MismatchTests(unittest.TestCase):
    def test_gold_and_fresh_report(self):
        check()
    def test_zero_vector(self):
        self.assertEqual(cosine([0],[1]),0)
    def test_missing_image(self):
        import tempfile,json
        rows=load_catalog(); rows[0]['image']='images/absent.svg'
        with tempfile.NamedTemporaryFile(mode='w+',suffix='.json') as f:
            json.dump(rows,f); f.flush()
            with self.assertRaises(ValueError): load_catalog(f.name)
