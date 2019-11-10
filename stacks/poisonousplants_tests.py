import unittest
from poisonousplants import poisonousPlants
class PoisonousPlantsTests(unittest.TestCase):
    def test_case1(self):
        """
            case for same values any number of times
        :return:
        """
        # slot = ["01:00:00 02:00:00", "03:00:00 04:00:00", "04:00:00 12:00:00", "15:00:00 24:00:00"]
        slot = [6,5,8,4,7,10,9]
        self.assertEqual(poisonousPlants(slot),2)

    def test_case2(self):
        """
            case for same values any number of times
        :return:
        """
        # slot = ["01:00:00 02:00:00", "03:00:00 04:00:00", "04:00:00 12:00:00", "15:00:00 24:00:00"]
        slot = [4,3,7,5,6,4,2]
        self.assertEqual(poisonousPlants(slot),3)
if __name__ == '__main__':
    unittest.main()