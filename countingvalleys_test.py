import unittest
from countingvalleys import countingValleys

class Countingvalleys(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(countingValleys((8),('UDDDUDUU')),(1))

    def test_allu(self):
        self.assertEqual(countingValleys((10),('UUUUUUUUUU')),(0))

    def test_alld(self):
        self.assertEqual(countingValleys((8),('DDDDDDDD')),(0))

    def test_du(self):
        self.assertEqual(countingValleys((10),('UDUDUDUDUD')),(0))

    def test_loeca(self):
        self.assertEqual(countingValleys((10),('ududududud')),(0))