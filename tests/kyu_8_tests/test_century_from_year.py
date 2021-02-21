import unittest

from katas.kyu_8.century_from_year import century

class ComputationTestCase(unittest.TestCase):
    def test_equals_1(self):
        self.assertEqual(century(1705), 18, 'Testing for year 1705')
    
    def test_equals_2(self):
        self.assertEqual(century(1900), 19, 'Testing for year 1900')
    
    def test_equals_3(self):
        self.assertEqual(century(1601), 17, 'Testing for year 1601')
