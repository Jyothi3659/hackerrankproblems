import unittest
from bubblesorting import bubble_sorting

class DecimalBinaryTests(unittest.TestCase):
    def test_case1(self):
        """
            case for same values any number of times
        :return:
        """
        # slot = ["01:00:00 02:00:00", "03:00:00 04:00:00", "04:00:00 12:00:00", "15:00:00 24:00:00"]
        slot = [1,2,3]
        self.assertEqual(bubble_sorting(slot), 0)

    def test_case2(self):
        """
            case for same values any number of times
        :return:
        """
        # slot = ["01:00:00 02:00:00", "03:00:00 04:00:00", "04:00:00 12:00:00", "15:00:00 24:00:00"]
        slot = [3,2,1]
        self.assertEqual(bubble_sorting(slot), 3)

if __name__ == '__main__':
    unittest.main()
