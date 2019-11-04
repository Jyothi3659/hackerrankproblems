import unittest
from catsandamouse import catMouse


class Catmouse(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(catMouse(5,4,2),('Cat B'))

    def test_negt(self):
        self.assertEqual(catMouse(1,3,2),('Mouse C'))

    def test_high(self):
        self.assertEqual(catMouse(50,55,53),('Cat B'))

    def test_zero(self):
        self.assertEqual(catMouse(0,0,0),('Mouse C'))
