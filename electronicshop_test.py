import unittest
from electronicshop import get


class Electronic(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(get([3,1],[5,2,8],10),(9))

    def test_high(self):
        self.assertEqual(get([30,50,20],[15,20,40],22),(-1))

    def test_lowp(self):
        self.assertEqual(get([2,5,4],[10,3,5],8),(8))

    def test_negt(self):
        self.assertEqual(get([-10,-30,10],[-20,40,-10],15),(10))

    def test_highl(self):
        self.assertEqual(get([50,40,10],[50,40,10],5),(-1))
