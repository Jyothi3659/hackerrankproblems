import unittest
from fractions import fraction


class DecimalBinaryTests(unittest.TestCase):
    def test_case1(self):
        """
            case for same values any number of times
        :return:
        """
        # slot = ["01:00:00 02:00:00", "03:00:00 04:00:00", "04:00:00 12:00:00", "15:00:00 24:00:00"]
        slot = [1,2,3,-8,0,0]
        self.assertEqual(fraction(slot), (0.5,0.1666,0.333))

if __name__ == '__main__':
    unittest.main()
