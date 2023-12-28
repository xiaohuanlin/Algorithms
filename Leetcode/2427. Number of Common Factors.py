'''
Given two positive integers a and b, return the number of common factors of a and b.

An integer x is a common factor of a and b if x divides both a and b.



Example 1:

Input: a = 12, b = 6
Output: 4
Explanation: The common factors of 12 and 6 are 1, 2, 3, 6.
Example 2:

Input: a = 25, b = 30
Output: 2
Explanation: The common factors of 25 and 30 are 1, 5.


Constraints:

1 <= a, b <= 1000
'''

from typing import *
import unittest

from math import gcd

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        res = 0
        g = gcd(a, b)
        for i in range(1, g + 1):
            if i ** 2 > g:
                break
            if g % i == 0:
                res += (2 if g // i != i else 1)
        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((12, 6), 4),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().commonFactors(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
