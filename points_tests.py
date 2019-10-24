import unittest
from points import compareTriplets


class PointsTests(unittest.TestCase):
    def test_case1(self):
        """if both has  one equal qualities"""
        self.assertEqual(compareTriplets([5,6,7],[3,6,10]), (1,1))

    def test_empty_list(self):
        """"if both has"""
        self.assertEqual(compareTriplets([], []), (0, 0))

    def test_zeros(self):
        self.assertEqual(compareTriplets([0,0], [0, 0]), (0, 0))

    def test_high(self):
        self.assertEqual(compareTriplets([22,10,5],[20,9,10]), (2,1))

    def test_low(self):
        self.assertEqual(compareTriplets([10,10,4],[11,11,6]), (0,3))


if __name__ == "__main__":
    unittest.main()
