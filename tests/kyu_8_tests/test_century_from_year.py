import unittest

from katas.kyu_8.century_from_year import century

class TestComputationCentury(unittest.TestCase):
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
    
    def test_equals_7(self):
        self.assertEqual(century(22399), 224, 'Testing for year 22399')
    
    def test_equals_8(self):
        self.assertEqual(century(1), 1, 'Testing for year 1')
    
    def test_equals_9(self):
        self.assertEqual(century(555), 6, 'Testing for year 555')
    
    def test_equals_10(self):
        self.assertEqual(century(1111), 12, 'Testing for year 1111')
    
    def test_equals_11(self):
        self.assertEqual(century(-1), 0, 'Testing for year -1')
    
    def test_equals_12(self):
        self.assertEqual(century(0), 0, 'Testing for year 0')
