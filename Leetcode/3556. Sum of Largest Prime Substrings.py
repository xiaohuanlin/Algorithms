'''
Given a string s, find the sum of the 3 largest unique prime numbers that can be formed using any of its substrings.

Return the sum of the three largest unique prime numbers that can be formed. If fewer than three exist, return the sum of all available primes. If no prime numbers can be formed, return 0.

Note: Each prime number should be counted only once, even if it appears in multiple substrings. Additionally, when converting a substring to an integer, any leading zeros are ignored.

 

Example 1:

Input: s = "12234"

Output: 1469

Explanation:

The unique prime numbers formed from the substrings of "12234" are 2, 3, 23, 223, and 1223.
The 3 largest primes are 1223, 223, and 23. Their sum is 1469.
Example 2:

Input: s = "111"

Output: 11

Explanation:

The unique prime number formed from the substrings of "111" is 11.
Since there is only one prime number, the sum is 11.
 

Constraints:

1 <= s.length <= 10
s consists of only digits.
'''
import unittest
from typing import *
from math import sqrt
from heapq import heappush, heappop
from functools import cache


class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:
        @cache
        def is_prime(x):
            if x <= 1:
                return False
            if x == 2 or x == 3:
                return True
            for y in range(2, int(sqrt(x)) + 1):
                if x % y == 0:
                    return False
            return True

        res = []
        for i in range(len(s)):
            for j in range(i, len(s)):
                w = int(s[i:j+1])
                if is_prime(w) and w not in res:
                    heappush(res, w)
                    if len(res) > 3:
                        heappop(res)
        return sum(res)


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ("12234", 1469),
            ("111", 11),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().sumOfLargestPrimes(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

