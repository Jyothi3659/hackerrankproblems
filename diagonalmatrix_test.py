import unittest
from diag_matrix import diagonalDifference


class Decimalbinarytest(unittest.TestCase):
    def test_posnum(self):
        self.assertEqual(diagonalDifference([[3],[11,2,6],[10,4,6],[20,5,10]]),(50))

    def test_zero(self):
        self.assertEqual(diagonalDifference([[0,0,0,0],[0,0],[0,0,0,0],[0,0,0,0]]),(0))

    def test_neg(self):
        self.assertEqual(diagonalDifference([[-3],[11,2,-6],[10,4,6],[20,5,-10]]),(27))

    def test_long(self):
        self.assertEqual(diagonalDifference([[6,6,7,-10,9,-3,8,9,-1],[9,7,-10,6,4,1,6,1,1],[-1,-2,4,-6,1,-4,-6,3,9],[-8,7,6,-1,-6,-6,6,-7,2],[-10,-4,9,1,-7,8,-5,3,-5],[-8,-3,-4,2,-3,7,-5,1,-5],
       [-2,-7,-4,8,3,-1,8,2,3],[-3,4,6,-7,-7,-8,-3,9,-6],[-2,0,5,4,4,4,-3,3,0]]),(52))

if __name__ == '__main__':
    unittest.main()

