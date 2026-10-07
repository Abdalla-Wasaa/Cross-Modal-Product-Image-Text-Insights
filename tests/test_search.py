import unittest
from analytics.search import search
from mismatch import load_catalog
class SearchTests(unittest.TestCase):
    def test_relevant_result(self):
        self.assertEqual(search('navy sisal kiondo',load_catalog(),1)[0]['sku'],'KND-01')
    def test_unknown(self):
        self.assertEqual(search('unrecognized',load_catalog()),[])
    def test_k(self):
        with self.assertRaises(ValueError): search('bag',load_catalog(),0)
