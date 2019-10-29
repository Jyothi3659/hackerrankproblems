import unittest
from birthdaycakecandles import birthdayCakeCandles


class Birthdaycake(unittest.TestCase):
    def test_case(self):
        self.assertEqual(birthdayCakeCandles([1,2,3,5,5,4]),(2))

    def test_allhigh(self):
        self.assertEqual(birthdayCakeCandles([5,5,5,5,5,5,5,5]),(8))

    def test_zeros(self):
        self.assertEqual(birthdayCakeCandles([0,0,0,0,0]),(5))

    def test_negative(self):
        self.assertEqual(birthdayCakeCandles([1,2,3,3,-5,-5,-4]),(2))