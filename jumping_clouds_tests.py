import unittest
from jumping_clouds import jumpingOnClouds


class CloudsTests(unittest.TestCase):
    def test_case1(self):
        """
            case for same values any number of times
        :return:
        """
        # slot = ["01:00:00 02:00:00", "03:00:00 04:00:00", "04:00:00 12:00:00", "15:00:00 24:00:00"]

        slot = [0,0,1,0,0,1,0]
        self.assertEqual(jumpingOnClouds(slot), 4)

    def test_case2(self):
        """
            case for same values any number of times
        :return:
        """
        # slot = ["01:00:00 02:00:00", "03:00:00 04:00:00", "04:00:00 12:00:00", "15:00:00 24:00:00"]

        slot = [0, 0, 0, 1, 0, 0]
        self.assertEqual(jumpingOnClouds(slot), 3)


if __name__ == '__main__':
    unittest.main()
