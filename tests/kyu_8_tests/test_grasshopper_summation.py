import unittest

from katas.kyu_8.grasshopper_summation.py import summation

class SummationTestCase(unittest.TestCase):
    def test_equals_1(self):
        self.assertEqual(summation(1), 1)
    
    def test_equals_2(self):
        self.assertEqual(summation(8), 36)
    
    def test_equals_3(self):
        self.assertEqual(summation(22), 253)
    
    def test_equals_4(self):
        self.assertEqual(summation(100), 5050)
    
    def test_equals_5(self):
        self.assertEqual(summation(213), 22791)
