'''
A digit string is good if the digits (0-indexed) at even indices are even and the digits at odd indices are prime (2, 3, 5, or 7).

For example, "2582" is good because the digits (2 and 8) at even positions are even and the digits (5 and 2) at odd positions are prime. However, "3245" is not good because 3 is at an even index but is not even.
Given an integer n, return the total number of good digit strings of length n. Since the answer may be large, return it modulo 109 + 7.

A digit string is a string consisting of digits 0 through 9 that may contain leading zeros.

 

Example 1:

Input: n = 1
Output: 5
Explanation: The good numbers of length 1 are "0", "2", "4", "6", "8".
Example 2:

Input: n = 4
Output: 400
Example 3:

Input: n = 50
Output: 564908303
 

Constraints:

1 <= n <= 1015
'''
from typing import *

import unittest

from math import ceil
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = int(1e9 + 7)
        def pow(x, y):
            if y == 0:
                return 1
            return (pow(x, y//2) % mod) ** 2 * (x if y % 2 == 1 else 1)
        
        return (pow(5, ceil(n / 2)) * pow(4, n // 2)) % mod
    
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((50,),564908303),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().countGoodNumbers(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
