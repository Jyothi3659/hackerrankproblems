import unittest
from formingamagicsquare import formingamagicsquare


class Formamagicsquare(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(formingamagicsquare([[5,3,4],[1,5,8],[6,4,2]]),(7))

    def test_normalcheck(self):
        self.assertEqual(formingamagicsquare([[4,9,2],[3,5,7],[8,1,5]]),(1))

    def test_highnum(self):
        self.assertEqual(formingamagicsquare([[50,80,20],[33,70,200],[500,320,100]]),(1328))

    def test_negt(self):
        self.assertEqual(formingamagicsquare([[-200,150,-500],[-10000,40000,-50000],[100000,-150000,-2000000]]),(2350851))

    def test_withzero(self):
        self.assertEqual(formingamagicsquare([[2002,500002,1000050],[000,000,500000],[200000,500050,2020202]]),(4722273))


if __name__ == '__main__':
    unittest.main()

