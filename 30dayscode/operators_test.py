import unittest
from operators import solve

class Operators(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(solve(12.00,20,8),(15.36))

    def test_high(self):
        self.assertEqual(solve(58,72,520),(401.36))

    def test_negt(self):
        self.assertEqual(solve(-800,-280,530),(-2800))

    def test_long(self):
        self.assertEqual(solve(10000,158932,298576),(45760800))

    def test_zero(self):
        self.assertEqual(solve(00000,00000,1919),(0.0))