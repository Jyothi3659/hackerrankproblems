import unittest
from kangaroo import kangaroo


class Kangroo(unittest.TestCase):
    def test_eqjumps(self):
        self.assertEqual(kangaroo(10,19,20,29),('no'))

    def test_high(self):
        self.assertEqual(kangaroo(253,350,850,200),('no'))

    def test_positive(self):
        self.assertEqual(kangaroo(230,100,200,130),('yes'))

    def test_negitive(self):
        self.assertEqual(kangaroo(-512,200,220,92),('no'))

    def test_zeros(self):
        self.assertEqual(kangaroo(00,00,00,10),('no'))


if __name__ == '__main__':
    unittest.main()
