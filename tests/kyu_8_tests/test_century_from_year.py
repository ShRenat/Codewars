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
    
    def test_century_1200(self):
        self.assertEqual(century(1200), 12, 'Testing for year 1200')
    
    def test_century_250(self):
        self.assertEqual(century(250), 3, 'Testing for year 250')
    
    def test_century_389(self):
        self.assertEqual(century(389), 4, 'Testing for year 389')
    
    def test_century_521(self):
        self.assertEqual(century(521), 6, 'Testing for year 521')
    
    def test_century_842(self):
        self.assertEqual(century(842), 9, 'Testing for year 842')
    
    def test_century_1349(self):
        self.assertEqual(century(1349), 14, 'Testing for year 1349')
    
    def test_century_9999(self):
        self.assertEqual(century(9999), 100, 'Testing for year 9999')
    
    def test_century_6531(self):
        self.assertEqual(century(6531), 66, 'Testing for year 6531')
    
    def test_century_2021(self):
        self.assertEqual(century(2021), 21, 'Testing for year 2021')
    
    def test_century_3030(self):
        self.assertEqual(century(3030), 31, 'Testing for year 3030')
