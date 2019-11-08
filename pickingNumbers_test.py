import unittest
from pickingnumbers import pickingNumbers


class Pickingnumbers(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(pickingNumbers([3,3,4,1]),(3))

    def test_high(self):
        self.assertEqual(pickingNumbers([200,200,500,100,300]),(2))

    def test_neg(self):
        self.assertEqual(pickingNumbers([-5000,-400,950,150,600,-5000,-6000,-1000]),(2))

    def test_zero(self):
        self.assertEqual(pickingNumbers([0000,0000,2000,1500,0000,0000,1500]),(4))

    def test_nomatch(self):
        self.assertEqual(pickingNumbers([145214,253352,523625,524625,524953,852425]),(1))


if __name__ == '__main__':
    unittest.main()
