import unittest

from katas.kyu_8.century_from_year import century

class TestComputationCentury(unittest.TestCase):
    def test_century_1705(self):
        self.assertEqual(century(1705), 18, 'Testing for year 1705')
    
    def test_century_1900(self):
        self.assertEqual(century(1900), 19, 'Testing for year 1900')
    
    def test_century_1601(self):
        self.assertEqual(century(1601), 17, 'Testing for year 1601')
    
    def test_century_2000(self):
        self.assertEqual(century(2000), 20, 'Testing for year 2000')
    
    def test_century_356(self):
        self.assertEqual(century(356), 4, 'Testing for year 356')
    
    def test_century_89(self):
        self.assertEqual(century(89), 1, 'Testing for year 89')
    
    def test_century_22399(self):
        self.assertEqual(century(22399), 224, 'Testing for year 22399')
    
    def test_century_1(self):
        self.assertEqual(century(1), 1, 'Testing for year 1')
    
    def test_century_555(self):
        self.assertEqual(century(555), 6, 'Testing for year 555')
    
    def test_century_1111(self):
        self.assertEqual(century(1111), 12, 'Testing for year 1111')
    
    def test_century_minus_1(self):
        self.assertEqual(century(-1), 0, 'Testing for year -1')
    
    def test_century_0(self):
        self.assertEqual(century(0), 0, 'Testing for year 0')
