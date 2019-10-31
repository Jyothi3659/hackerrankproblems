import unittest
from sumarray import bigSumArray


class SumarrayTests(unittest.TestCase):

    def test_case(self):
        self.assertEqual(bigSumArray([1000015,10012,1003,100056,1000086]),(2111172))

    def test_zeros(self):
        self.assertEqual(bigSumArray([00000,00000,00000,00000,00000]),(00000))

    def test_largeint(self):
        self.assertEqual(bigSumArray([25632,25362,86596,65486,52462]),(255538))

    def test_onetohigh(self):
        self.assertEqual(bigSumArray([1,10,100,1000,1000086]),(1001197))

    def test_negative(self):
        self.assertEqual(bigSumArray([1, -10, 100, 1000, 1000086]), (1001177))

    def test_multiple(self):
        self.assertEqual(bigSumArray([1, 10*10, 100, 1000, 1000086]), (1001287))

    def test_divide(self):
        self.assertEqual(bigSumArray([1, 10*10, 100/5, 1000, 1000086]), (1001207))


if __name__ == '__main__':
    unittest.main()
