import unittest
from repeated_string import repeatedString

class RepeatedStringTests(unittest.TestCase):
    def test_case1(self):
        """
            case for same values any number of times
        :return:
        """
        # slot = ["01:00:00 02:00:00", "03:00:00 04:00:00", "04:00:00 12:00:00", "15:00:00 24:00:00"]
        s = 'aba'
        self.assertEqual(repeatedString(s,10), 7)

    def test_case2(self):
        """
            case for same values any number of times
        :return:
        """
        # slot = ["01:00:00 02:00:00", "03:00:00 04:00:00", "04:00:00 12:00:00", "15:00:00 24:00:00"]

        s =  'a'
        self.assertEqual(repeatedString(s,1000000000000), 1000000000000)

    def test_case3(self):
        """
            case for same values any number of times
        :return:
        """
        # slot = ["01:00:00 02:00:00", "03:00:00 04:00:00", "04:00:00 12:00:00", "15:00:00 24:00:00"]

        s = 'ceebbcb'
        self.assertEqual(repeatedString(s, 817723), 0)


if __name__ == '__main__':
    unittest.main()
