import unittest
from Divisiblesumpairs import divisibleSumPairs


class Divisiblesumpairs(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(divisibleSumPairs(3,[1,3,2,6,1,2]),(5))

    def test_highlen(self):
        self.assertEqual(divisibleSumPairs(5,[110,140,156,189,200,78,99,20,96,46]),(12))

    def test_neg(self):
        self.assertEqual(divisibleSumPairs(8,[-58,33,-45,-8,20,-64,1000,-10000,2000]),(10))

    def test_zero(self):
        self.assertEqual(divisibleSumPairs(18,[10000,29890,43590,3281,90422,34090,45678,24678,14905,12267,10003,20345,100034,200345,590567,36259,569,42136,78956,22569,5246,90,80,780,56023,25698,89562,23104]),(26))