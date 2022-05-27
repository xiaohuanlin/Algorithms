'''
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

 

Example 1:


Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
'''
import unittest

from typing import *

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        
        def dfs(x, y):
            if x >= row or x < 0 or y >= col or y < 0:
                return 0
            if grid[x][y] == 0:
                return 0
            
            grid[x][y] = 0
            count = 1
            for x_d, y_d in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                count += dfs(x + x_d, y + y_d)
            return count
        
        res = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))
        return res

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([[0,0,0,0,0,0,0,0]],),0),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maxAreaOfIsland(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()