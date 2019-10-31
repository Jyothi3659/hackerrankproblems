import unittest
from Gradingstudents import gradingstudents


class GradingStudents(unittest.TestCase):
    #test case for grades > 60 and grades < 40
    def test_normalgrade(self):
        self.assertEqual(gradingstudents([73,67,38,33]),([75,67,40,33]))

    #test case for all students having grades less than 40
    def test_lessgrade(self):
        self.assertEqual(gradingstudents([38,32,35,30]),([40,32,35,30]))

    #test case for negative grades
    def negative(self):
        self.assertEqual(gradingstudents([-50,-68,-73,-96]),([-50,-68,-73,-96]))

    #test case for grades greater than 100 and above
    def highgrades(self):
        self.assertEqual(gradingstudents([150,289,569,820]),([150, 290, 570, 820]))


if __name__ == '__main__':
    unittest.main()