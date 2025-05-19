'''
You are given a 0-indexed m x n binary matrix grid. You can move from a cell (row, col) to any of the cells (row + 1, col) or (row, col + 1) that has the value 1. The matrix is disconnected if there is no path from (0, 0) to (m - 1, n - 1).

You can flip the value of at most one (possibly none) cell. You cannot flip the cells (0, 0) and (m - 1, n - 1).

Return true if it is possible to make the matrix disconnect or false otherwise.

Note that flipping a cell changes its value from 0 to 1 or from 1 to 0.

 

Example 1:


Input: grid = [[1,1,1],[1,0,0],[1,1,1]]
Output: true
Explanation: We can change the cell shown in the diagram above. There is no path from (0, 0) to (2, 2) in the resulting grid.
Example 2:


Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
Output: false
Explanation: It is not possible to change at most one cell such that there is not path from (0, 0) to (2, 2).
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 1000
1 <= m * n <= 105
grid[i][j] is either 0 or 1.
grid[0][0] == grid[m - 1][n - 1] == 1
'''
import unittest

from typing import *


class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        row = len(grid)
        col = len(grid[0])
        def dfs(point):
            x, y = point
            if x >= row or y >= col:
                return False
            if grid[x][y] == 0:
                return False
            if point == (row - 1, col - 1):
                return True
            grid[x][y] = 0
            for x_del, y_del in ((1, 0), (0, 1)):
                if dfs((x + x_del, y + y_del)):
                    return True
            return False
        
        res = dfs((0, 0))
        if not res:
            return True
        grid[0][0] = 1
        return not dfs((0, 0))

        

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([[1,1,1],[1,0,0],[1,1,1]],), True),
            (([[1,1,1],[1,0,1],[1,1,1]],), False),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().isPossibleToCutPath(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

