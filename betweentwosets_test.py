import unittest
from betweentwosets import getTotalX


class Betweentwosets(unittest.TestCase):
    def test_high(self):
        self.assertEqual(getTotalX([2,4],[16,32,96]),(3))

    def test_highrange(self):
        self.assertEqual(getTotalX([2,6],[45,70]),(0))

    def test_negative(self):
        self.assertEqual(getTotalX([-5,6],[50,-30,-50,10]),(0))