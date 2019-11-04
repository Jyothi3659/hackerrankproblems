import unittest
from max_stack import stackfunc

class MaxStackTests(unittest.TestCase):
    def test_case1(self):
        """
            case for same values any number of times
        :return:
        """
        # slot = ["01:00:00 02:00:00", "03:00:00 04:00:00", "04:00:00 12:00:00", "15:00:00 24:00:00"]
        slot = [[1,97],[2],[1,20],[2],[1,26],[1,20],[2],[3],[1,91],[3]]
        self.assertEqual(stackfunc(slot),[26,91])
if __name__ == '__main__':
    unittest.main()