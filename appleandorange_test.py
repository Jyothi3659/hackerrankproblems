import unittest
from appleandorange import countapplesandoranges


class Appleorange(unittest.TestCase):
    def test_highcount(self):
        self.assertEqual(countapplesandoranges(7,11,5,15,(-2,2,1),(5,-6)),(1,1))


if __name__ == '__main__':
    unittest.main()


