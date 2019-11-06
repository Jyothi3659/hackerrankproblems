import unittest
from operator import restaurent


class Operators(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(restaurent(12.00,20,8),(15))

    def test_high(self):
        self.assertEqual(restaurent(58,72,520),(401))

    def test_negt(self):
        self.assertEqual(restaurent(-800,-280,530),(-2800))

    def test_long(self):
        self.assertEqual(restaurent(10000,158932,298576),(45760800))

    def test_zero(self):
        self.assertEqual(restaurent(00000,00000,1919),(0))

if __name__ == '__main__':
    unittest.main()
