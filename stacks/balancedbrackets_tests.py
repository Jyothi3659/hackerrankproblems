import unittest
from balancedbrackets import isBalanced
class BalancedBracketsTests(unittest.TestCase):
    def test_case1(self):
        """
            case for same values any number of times
        :return:
        """
        # slot = ["01:00:00 02:00:00", "03:00:00 04:00:00", "04:00:00 12:00:00", "15:00:00 24:00:00"]
        slot = '{{[[(())]]}}'
        self.assertEqual(isBalanced(slot),'YES')

    def test_case2(self):
        """
            case for same values any number of times
        :return:
        """
        # slot = ["01:00:00 02:00:00", "03:00:00 04:00:00", "04:00:00 12:00:00", "15:00:00 24:00:00"]
        slot = '{[(])}'
        self.assertEqual(isBalanced(slot),'NO')

    def test_case3(self):
        """
            case for same values any number of times
        :return:
        """
        # slot = ["01:00:00 02:00:00", "03:00:00 04:00:00", "04:00:00 12:00:00", "15:00:00 24:00:00"]
        slot = '{[()]}'
        self.assertEqual(isBalanced(slot),'YES')
if __name__ == '__main__':
    unittest.main()