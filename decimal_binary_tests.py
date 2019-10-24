import unittest
from decimal_binary import binary_func


class DecimalBinaryTests(unittest.TestCase):
    def test_case1(self):
        """
            case for same values any number of times
        :return:
        """
        # slot = ["01:00:00 02:00:00", "03:00:00 04:00:00", "04:00:00 12:00:00", "15:00:00 24:00:00"]
        slot = 5
        self.assertEqual(binary_func(slot), 2)
    def test_case2(self):
        """
            case for same values any number of times
        :return:
        """
        # slot = ["01:00:00 02:00:00", "03:00:00 04:00:00", "04:00:00 12:00:00", "15:00:00 24:00:00"]
        slot = 8
        self.assertEqual(binary_func(slot), 3)

    def test_case3(self):
        """

        :return:
        """
        # slot = ["01:00:00 02:00:00", "03:00:00 04:00:00", "04:00:00 12:00:00", "15:00:00 24:00:00"]
        slot = 439
        self.assertEqual(binary_func(slot), 3)

    def test_case4(self):
        """
            case for same values any number of times
        :return:
        """
        # slot = ["01:00:00 02:00:00", "03:00:00 04:00:00", "04:00:00 12:00:00", "15:00:00 24:00:00"]
        slot = 951
        self.assertEqual(binary_func(slot), 3)

    def test_binary(self):
        """
            case for same values any number of times
        :return:
        """
        # slot = ["01:00:00 02:00:00", "03:00:00 04:00:00", "04:00:00 12:00:00", "15:00:00 24:00:00"]
        slot = 262141
        self.assertEqual(binary_func(slot), 16)


if __name__ == '__main__':
    unittest.main()