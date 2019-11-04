import unittest
from appleandorange import countapplesandoranges


class Appleorange(unittest.TestCase):
    def test_highcount(self):
        self.assertEqual(countapplesandoranges(22, 33, 456, 24, 100, 200))