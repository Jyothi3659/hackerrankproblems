import unittest
from array_queries import resultingarray

class ArrayManipulationTests(unittest.TestCase):
    def test_case1(self):
        """
            case for same values any number of times
        :return:
        """
        # slot = ["01:00:00 02:00:00", "03:00:00 04:00:00", "04:00:00 12:00:00", "15:00:00 24:00:00"]
        N = 8
        M = 4
        A = [1,2,3,4,5,6,7,8]
        slot = [[1,2,4],[2,3,5],[1,4,7],[2,1,4]]
        self.assertEqual(resultingarray(N,slot,A),1)
if __name__ == '__main__':
    unittest.main()

