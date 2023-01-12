'''
You are given a positive integer n.

Continuously replace n with the sum of its prime factors.

Note that if a prime factor divides n multiple times, it should be included in the sum as many times as it divides n.
Return the smallest value n will take on.



Example 1:

Input: n = 15
Output: 5
Explanation: Initially, n = 15.
15 = 3 * 5, so replace n with 3 + 5 = 8.
8 = 2 * 2 * 2, so replace n with 2 + 2 + 2 = 6.
6 = 2 * 3, so replace n with 2 + 3 = 5.
5 is the smallest value n will take on.
Example 2:

Input: n = 3
Output: 3
Explanation: Initially, n = 3.
3 is the smallest value n will take on.


Constraints:

2 <= n <= 105
'''
import unittest

from typing import *

class Solution:
    def smallestValue(self, n: int) -> int:
        def factor(num):
            i = 2
            while i * i <= num:
                if num % i == 0:
                    return factor(num // i) + [i]
                i += 1
            return [num]


        while True:
            factor_sum = sum(factor(n))
            if factor_sum >= n:
                return n
            n = factor_sum

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((15,),5),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().smallestValue(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
