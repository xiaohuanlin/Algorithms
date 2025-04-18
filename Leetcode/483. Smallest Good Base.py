'''
Given an integer n represented as a string, return the smallest good base of n.

We call k >= 2 a good base of n, if all digits of n base k are 1's.



Example 1:

Input: n = "13"
Output: "3"
Explanation: 13 base 3 is 111.
Example 2:

Input: n = "4681"
Output: "8"
Explanation: 4681 base 8 is 11111.
Example 3:

Input: n = "1000000000000000000"
Output: "999999999999999999"
Explanation: 1000000000000000000 base 999999999999999999 is 11.


Constraints:

n is an integer in the range [3, 1018].
n does not contain any leading zeros.
'''
import unittest

from typing import *
from collections import Counter
from math import log2


class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        m = int(log2(n))
        while m > 0:
            start = 2
            end = n
            while start <= end:
                middle = (start + end) // 2
                z = (middle ** (m + 1) - 1)
                if z == n * (middle-1):
                    return str(middle)
                elif z < n * (middle-1):
                    start = middle + 1
                else:
                    end = middle - 1

            m -= 1
        return str(n-1)


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("13",),"3"),
            (("1000000000000000000",),"999999999999999999"),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().smallestGoodBase(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

