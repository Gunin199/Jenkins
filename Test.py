#!/usr/bin/python3
# Test case for average of 2 numbers
import unittest

from AverageCalc import my_avg

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to find average of two numbers
        """
        n1 = 20
        n2 = 30
        result = my_avg(n1,n2)
        self.assertEqual(result, 45)

if __name__ == '__main__':
    unittest.main()