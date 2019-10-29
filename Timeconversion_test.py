import unittest
from Timeconversion import timeConversion


class Timeconversiontest(unittest.TestCase):
    def test_pm(self):
        self.assertEqual(timeConversion("07:05:45PM"),("19:05:45"))

    def test_am(self):
        self.assertEqual(timeConversion("12:40:22AM"),("00:40:22"))

    def test_night(self):
        self.assertEqual(timeConversion("10:40:05"),("10:40:05"))

    
