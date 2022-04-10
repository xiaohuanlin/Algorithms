'''
You are given an m x n binary matrix grid.

A move consists of choosing any row or column and toggling each value in that row or column (i.e., changing all 0's to 1's, and all 1's to 0's).

Every row of the matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

Return the highest possible score after making any number of moves (including zero moves).

 

Example 1:


Input: grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39
Explanation: 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
Example 2:

Input: grid = [[0]]
Output: 1
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 20
grid[i][j] is either 0 or 1.
'''
from typing import *

import unittest
    
class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        sum_v = row
        for j in range(1, col):
            sum_v <<= 1
            count = 0
            for i in range(row):
                count += (grid[i][j] == grid[i][0])
            count = max(count, row - count)
            sum_v += count
        return sum_v
        
        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([[0,0,1,1],[1,0,1,0],[1,1,0,0]], ), 39),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().matrixScore(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
