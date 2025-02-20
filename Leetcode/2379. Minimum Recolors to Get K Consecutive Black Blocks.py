'''
You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.

You are also given an integer k, which is the desired number of consecutive black blocks.

In one operation, you can recolor a white block such that it becomes a black block.

Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.

 

Example 1:

Input: blocks = "WBBWWBBWBW", k = 7
Output: 3
Explanation:
One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks
so that blocks = "BBBBBBBWBW". 
It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3 operations.
Therefore, we return 3.
Example 2:

Input: blocks = "WBWBBBW", k = 2
Output: 0
Explanation:
No changes need to be made, since 2 consecutive black blocks already exist.
Therefore, we return 0.
 

Constraints:

n == blocks.length
1 <= n <= 100
blocks[i] is either 'W' or 'B'.
1 <= k <= n
'''
import unittest

from typing import *


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        cnt = 0
        res = 0
        for right in range(len(blocks)):
            cnt += blocks[right] == 'B'
            if right - left == k - 1:
                res = max(res, cnt)
                cnt -= blocks[left] == 'B'
                left += 1
        return k - res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("WBBWWBBWBW", 7), 3),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().minimumRecolors(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
