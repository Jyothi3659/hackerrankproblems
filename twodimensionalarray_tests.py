import unittest
from twodimensionalarray import array_func


class TwoDimensionArrayTests(unittest.TestCase):
    # def test_allpostive(self):
    #     """
    #         case for same values any number of times
    #     :return:
    #     """
    #     # slot = ["01:00:00 02:00:00", "03:00:00 04:00:00", "04:00:00 12:00:00", "15:00:00 24:00:00"]
    #     slot = 5
    #     self.assertEqual(2D_6array.array_func(slot), 2)
    def test_negative(self):
        """
            case for same values any number of times
        :return:
        """

        slot = [[1,1,1,0,0,0],[0,1,0,0,0,0],[1,1,1,0,0,0],[0,9,2,-4,-4,0],[0,0,0,-2,0,0],[0,0,-1,-2,-4,0]]
        self.assertEqual(array_func(slot), 13)

    def test_allnegative(self):
        """
            case for same values any number of times
        :return:
        """

        slot = [[-1,-1,-1,0,0,0], [0,-1,0,0,0,0], [-1,-1,-1,0,0,0], [0,-9,2,-4,-4,0], [-7,0,0,-2,0,0],[0,0,-1,-2,-4,0]]
        self.assertEqual(array_func(slot), 0)

    def test_allnegative2(self):
        """
            case for same values any number of times
        :return:
        """

        slot = [[-1,-1,0,-9,-2,-2],[-2,-1,-6,-8,-2,-5],[-1,-1,-1,-2,-3,-4],[-1,-9,-2,-4,-4,-5],[-7,-3,-3,-2,-9,-9],[-1,-3,-1,-2,-4,-5]]
        self.assertEqual(array_func(slot),-6)
if __name__ == '__main__':
    unittest.main()