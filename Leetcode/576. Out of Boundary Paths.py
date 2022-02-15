'''
There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.

 

Example 1:


Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
Output: 6
Example 2:


Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
Output: 12
 

Constraints:

1 <= m, n <= 50
0 <= maxMove <= 50
0 <= startRow < m
0 <= startColumn < n
'''

from typing import *

import unittest



class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        return self.helper(m, n, maxMove, startRow, startColumn, {})

    def helper(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int, mem: Dict) -> int:
        is_out = startRow < 0 or startRow >= m or startColumn < 0 or startColumn >= n
        if maxMove == 0 or is_out:
            return int(is_out)
        
        key = (maxMove, startRow, startColumn)
        if key in mem:
            return mem[key]

        res = 0
        for x_delta, y_delta in ((0, -1), (-1, 0), (0, 1), (1, 0)):
            res += self.helper(m, n, maxMove - 1, startRow + x_delta, startColumn + y_delta, mem)
        mem[key] = res % (1e9 + 7)
        return mem[key]
        

    
class TestSolution(unittest.TestCase):
    def test_case(self):
        examples = (
            ((2, 2, 2, 0, 0), 6),
            ((1, 3, 3, 0, 1), 12),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().findPaths(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

