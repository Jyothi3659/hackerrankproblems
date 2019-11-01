import unittest
from breakingtherecords import breakingtherecords


class Breakingthecandles(unittest.TestCase):
    def test_normalscore(self):
        self.assertEqual(breakingtherecords([20,10,5,8,50,80,90,70,2]),([3,3]))

    def test_highscremaxi(self):
        self.assertEqual(breakingtherecords([100,90,80,70,60,50,2,10]),([0,6]))

    def test_scoresmax(self):
        self.assertEqual(breakingtherecords([2000,5000,10000,450,4500,15000,200,8000,110,80,50,55]),([3,5]))

    def test_scoresneg(self):
        self.assertEqual(breakingtherecords([-10000,500,-20000,800,10000,1000,-100000,289855,10,15,40]),([4,2]))