import unittest
from fraction import add


class FractionTests(unittest.TestCase):
    def test_case(self):
        self.assertEqual(add([-4,-10,10,3,5,0]),(0.333333333,0.5,0))


