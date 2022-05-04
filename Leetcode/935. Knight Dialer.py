'''
The chess knight has a unique movement, it may move two squares vertically and one square horizontally, or two squares horizontally and one square vertically (with both forming the shape of an L). The possible movements of chess knight are shown in this diagaram:

A chess knight can move as indicated in the chess diagram below:


We have a chess knight and a phone pad as shown below, the knight can only stand on a numeric cell (i.e. blue cell).


Given an integer n, return how many distinct phone numbers of length n we can dial.

You are allowed to place the knight on any numeric cell initially and then you should perform n - 1 jumps to dial a number of length n. All jumps should be valid knight jumps.

As the answer may be very large, return the answer modulo 109 + 7.

 

Example 1:

Input: n = 1
Output: 10
Explanation: We need to dial a number of length 1, so placing the knight over any numeric cell of the 10 cells is sufficient.
Example 2:

Input: n = 2
Output: 20
Explanation: All the valid number we can dial are [04, 06, 16, 18, 27, 29, 34, 38, 40, 43, 49, 60, 61, 67, 72, 76, 81, 83, 92, 94]
Example 3:

Input: n = 3131
Output: 136006598
Explanation: Please take care of the mod.
 

Constraints:

1 <= n <= 5000
'''
import unittest

from typing import *

class Solution:
    def knightDialer(self, n: int) -> int:
        prev = [1 for _ in range(10)]
        cur = [1 for _ in range(10)]
        v = int(1e9 + 7)
        for _ in range(n-1):
            cur[0] = (prev[4] + prev[6]) % v
            cur[1] = (prev[8] + prev[6]) % v
            cur[2] = (prev[7] + prev[9]) % v
            cur[3] = (prev[8] + prev[4]) % v
            cur[4] = (prev[0] + prev[3] + prev[9]) % v
            cur[5] = 0
            cur[6] = (prev[0] + prev[1] + prev[7]) % v
            cur[7] = (prev[2] + prev[6]) % v
            cur[8] = (prev[1] + prev[3]) % v
            cur[9] = (prev[4] + prev[2]) % v
            prev = list(cur)
        return sum(cur) % v
        
        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((2,),20),
            ((3131,),136006598)
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().knightDialer(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
