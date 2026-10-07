import unittest,json,hashlib
from mismatch import ROOT,VOCAB,THRESHOLD
class PinTests(unittest.TestCase):
    def test_encoder(self):
        pin=json.loads((ROOT/'encoder_pin.json').read_text())
        self.assertEqual(pin['encoder'],'lab-bow-v1')
        self.assertEqual(pin['threshold'],THRESHOLD)
        self.assertEqual(pin['vocabulary'],list(VOCAB))
        self.assertFalse(pin['transformers_used'])
        self.assertFalse(pin['pixels_encoded'])
    def test_prompt_hash(self):
        pin=json.loads((ROOT/'generation/prompt_pin.json').read_text())
        self.assertEqual(pin['sha256'],hashlib.sha256((ROOT/'generation/generation_prompt.txt').read_bytes()).hexdigest())
    def test_rates(self):
        rates=json.loads((ROOT/'analytics/rates.json').read_text())
        self.assertEqual(rates['n'],3)
        self.assertEqual(rates['denominator'],3)
        self.assertEqual(rates['overall_flag_rate'],1/3)
