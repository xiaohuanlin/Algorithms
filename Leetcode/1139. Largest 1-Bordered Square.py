'''
Given a 2D grid of 0s and 1s, return the number of elements in the largest square subgrid that has all 1s on its border, or 0 if such a subgrid doesn't exist in the grid.

 

Example 1:

Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
Output: 9
Example 2:

Input: grid = [[1,1,0,0]]
Output: 1
 

Constraints:

1 <= grid.length <= 100
1 <= grid[0].length <= 100
grid[i][j] is 0 or 1
'''
import unittest

from typing import *
class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        pre_sum = [[(0, 0) for _ in range(col + 1)] for _ in range(row + 1)]
        
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                pre_sum[i][j] = (pre_sum[i][j-1][0] + grid[i-1][j-1], pre_sum[i-1][j][1] + grid[i-1][j-1])

        res = 0
        for i in range(row):
            for j in range(col):
                for r in range(min(i, j) + 1):
                    if (r + 1) ** 2 > res and \
                        pre_sum[i+1][j+1][1] - pre_sum[i-r][j+1][1] == r + 1 and \
                        pre_sum[i+1][j+1][0] - pre_sum[i+1][j-r][0] == r + 1 and \
                        pre_sum[i-r+1][j+1][0] - pre_sum[i-r+1][j-r][0] == r + 1 and \
                        pre_sum[i+1][j-r+1][1] - pre_sum[i-r][j-r+1][1] == r + 1:
                        res = (r + 1) ** 2
        return res
        
        
        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([[1,1,1],[1,0,1],[1,1,1]],),9),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().largest1BorderedSquare(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
