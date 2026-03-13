import unittest
from main import *

class TestMethods(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(Add("2, 4"), 6)
        self.assertEqual(Add("10"), 10)
        self.assertEqual(Add("1, 2"), 3)
        self.assertEqual(Add("1,2"), 3)


    def test_sum_multiple_numbers(self):
        self.assertEqual(Add("2, 4, 13"), 19)
        self.assertEqual(Add("1 2 3 4 5 6 7 8 9"), ValueError)
        self.assertEqual(Add("2 \n 4 \n 13"), 19)
        self.assertEqual(Add("10, 9, p"), ValueError)
        self.assertEqual(Add("1,\n"), ValueError)
        self.assertEqual(Add("1\n2, 3"), 6)