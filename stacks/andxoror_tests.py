import unittest
from stack_andxoror import  andXorOr
class AndXorOrTests(unittest.TestCase):
    def test_case1(self):
        """
            case for same values any number of times
        :return:
        """
        # slot = ["01:00:00 02:00:00", "03:00:00 04:00:00", "04:00:00 12:00:00", "15:00:00 24:00:00"]
        slot = [9,8,3,5,7]
        self.assertEqual(andXorOr(slot),11)
if __name__ == '__main__':
    unittest.main()
