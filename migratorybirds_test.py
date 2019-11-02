import unittest
from migratorybirds import migratorybirds

class Migratorybirds(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(migratorybirds([1,4,4,4,5,1,3,6]),(4))

    def test_positive(self):
        self.assertEqual(migratorybirds([1,2,3,4,4,4,5,5,1,1,2]),(1))

    def test_highrange(self):
        self.assertEqual(migratorybirds([0,0,0,1,2]),(0))

    def test_negtive(self):
        self.assertEqual(migratorybirds([1,-1,1,1,-2,2,2,2]),(1))

