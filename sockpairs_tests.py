import unittest
from sockpairs import sockMerchant


class CloudsTests(unittest.TestCase):
    def test_case1(self):
        """
            case for same values any number of times
        :return:
        """
        # slot = ["01:00:00 02:00:00", "03:00:00 04:00:00", "04:00:00 12:00:00", "15:00:00 24:00:00"]

        slot = [10,20,20,10,10,30,50,10,20]
        self.assertEqual(sockMerchant(9,slot), 3)

    def test_case2(self):
        """
            case for same values any number of times
        :return:
        """
        # slot = ["01:00:00 02:00:00", "03:00:00 04:00:00", "04:00:00 12:00:00", "15:00:00 24:00:00"]

        slot = [100]
        self.assertEqual(sockMerchant(1,slot), 0)


if __name__ == '__main__':
    unittest.main()
