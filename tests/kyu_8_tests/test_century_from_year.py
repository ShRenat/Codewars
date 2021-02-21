import unittest

from katas.kyu_8.century_from_year.py import century


class CalculationCenturyTestCase(unittest.TestCase):
    def test_equals_1(self):
        self.assertEqual(century(1705), 18, 'Testing for year 1705')
    
    def test_equals_2(self):
        self.assertEqual(century(1900), 19, 'Testing for year 1900')
    
    def test_equals_3(self):
        self.assertEqual(century(1601), 17, 'Testing for year 1601')
    
    def test_equals_4(self):
        self.assertEqual(century(2000), 20, 'Testing for year 2000')
    
    def test_equals_5(self):
        self.assertEqual(century(356), 4, 'Testing for year 356')
    
    def test_equals_6(self):
        self.assertEqual(century(89), 1, 'Testing for year 89')
