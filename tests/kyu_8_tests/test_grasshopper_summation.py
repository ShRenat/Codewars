import unittest

from katas.kyu_8.grasshopper_summation import summation


class TestSummation(unittest.TestCase):
    def test_summation_1(self):
        self.assertEqual(summation(1), 1)

    def test_summation_8(self):
        self.assertEqual(summation(8), 36)
    
    def test_summation_22(self):
        self.assertEqual(summation(22), 253)
    
    def test_summation_100(self):
        self.assertEqual(summation(100), 5050)

    def test_summation_213(self):
        self.assertEqual(summation(213), 22791)
