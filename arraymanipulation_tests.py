import unittest
from arraymanipulation import arrayManipulation

class ArrayManipulationTests(unittest.TestCase):
    def test_case1(self):
        """
            case for same values any number of times
        :return:
        """
        # slot = ["01:00:00 02:00:00", "03:00:00 04:00:00", "04:00:00 12:00:00", "15:00:00 24:00:00"]
        n = 10
        slot = [[1,5,3],[4,8,7],[6,9,1]]
        self.assertEqual(arrayManipulation(n,slot),10)
if __name__ == '__main__':
    unittest.main()
