'''
You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.


Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it modulo 109 + 7.

In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.



Example 1:


Input: n = 3
Output: 5
Explanation: The five different ways are show above.
Example 2:

Input: n = 1
Output: 1


Constraints:

1 <= n <= 1000
'''
from typing import *

import unittest

class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        dp = [1 for _ in range(n+1)]
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] = dp[i-3] + 2 * dp[i-1]
            dp[i] %= int(1e9+7)
        return dp[-1]


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((3,),5),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().numTilings(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
