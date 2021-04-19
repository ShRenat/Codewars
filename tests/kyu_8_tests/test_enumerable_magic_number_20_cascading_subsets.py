import unittest

from katas.8_kuy.enumerable_magic_number_20_cascading_subsets.py import each_cons

class TestCascadingSubsets(unittest.TestCase):
  def test_case1():
    test.assert_equals(each_cons(lst, 2), [[3,5], [5,8], [8,13]])
