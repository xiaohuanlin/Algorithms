'''
Given two positive integers n and x.

Return the number of ways n can be expressed as the sum of the xth power of unique positive integers, in other words, the number of sets of unique integers [n1, n2, ..., nk] where n = n1x + n2x + ... + nkx.

Since the result can be very large, return it modulo 109 + 7.

For example, if n = 160 and x = 3, one way to express n is n = 23 + 33 + 53.

 

Example 1:

Input: n = 10, x = 2
Output: 1
Explanation: We can express n as the following: n = 32 + 12 = 10.
It can be shown that it is the only way to express 10 as the sum of the 2nd power of unique integers.
Example 2:

Input: n = 4, x = 1
Output: 2
Explanation: We can express n in the following ways:
- n = 41 = 4.
- n = 31 + 11 = 4.
 

Constraints:

1 <= n <= 300
1 <= x <= 5
'''
from typing import *

import unittest

from functools import lru_cache

class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        mod = int(1e9 + 7)
        @lru_cache
        def dfs(num, remain):
            if remain < 0:
                return 0
            if remain == 0:
                return 1
            if num ** x > remain:
                return 0
            pick = dfs(num + 1, remain - num ** x)
            skip = dfs(num + 1, remain)
            return (pick + skip) % mod
        
        return dfs(1, n)
        

class TestSolution(unittest.TestCase):
    def test_case(self):
        examples = (
            ((10, 2), 1),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().numberOfWays(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()