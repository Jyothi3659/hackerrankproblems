import unittest
from drawingbook import solve


class Drawingbook(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(solve(6,2),(1))

    def test_highnum(self):
        self.assertEqual(solve(100,50),(25))

    def test_neg(self):
        self.assertEqual(solve(-15,5),(-10))

    def test_zero(self):
        self.assertEqual(solve(0,0),(0))

    def test_longnum(self):
        self.assertEqual(solve(10,13),(-1))

if __name__ == '__main__':
    unittest.main()
