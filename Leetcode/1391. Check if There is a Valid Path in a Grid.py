'''
You are given an m x n grid. Each cell of grid represents a street. The street of grid[i][j] can be:

1 which means a street connecting the left cell and the right cell.
2 which means a street connecting the upper cell and the lower cell.
3 which means a street connecting the left cell and the lower cell.
4 which means a street connecting the right cell and the lower cell.
5 which means a street connecting the left cell and the upper cell.
6 which means a street connecting the right cell and the upper cell.

You will initially start at the street of the upper-left cell (0, 0). A valid path in the grid is a path that starts from the upper left cell (0, 0) and ends at the bottom-right cell (m - 1, n - 1). The path should only follow the streets.

Notice that you are not allowed to change any street.

Return true if there is a valid path in the grid or false otherwise.

 

Example 1:


Input: grid = [[2,4,3],[6,5,2]]
Output: true
Explanation: As shown you can start at cell (0, 0) and visit all the cells of the grid to reach (m - 1, n - 1).
Example 2:


Input: grid = [[1,2,1],[1,2,1]]
Output: false
Explanation: As shown you the street at cell (0, 0) is not connected with any street of any other cell and you will get stuck at cell (0, 0)
Example 3:

Input: grid = [[1,1,2]]
Output: false
Explanation: You will get stuck at cell (0, 1) and you cannot reach cell (0, 2).
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
1 <= grid[i][j] <= 6
'''
import unittest

from typing import *

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        row = len(grid)
        col = len(grid[0])
        left = (0, -1)
        right = (0, 1)
        up = (-1, 0)
        down = (1, 0)
        directs = {
            1: (left, right),
            2: (up, down),
            3: (left, down),
            4: (right, down),
            5: (up, left),
            6: (up, right),
        }
        
        
        def dfs(x, y, prev, visit):
            if x < 0 or x >= row or y < 0 or y >= col:
                return False
            if (x, y) in visit:
                return False
            
            d = directs[grid[x][y]]
            if d[0] == prev:
                other_d = d[1]
            elif d[1] == prev:
                other_d = d[0]
            else:
                return False
            
            if x == row - 1 and y == col - 1:
                return True
            
            visit.add((x, y))
            return dfs(x + other_d[0], y + other_d[1], (other_d[0] * -1, other_d[1] * -1), visit)
                
        
        return dfs(0, 0, directs[grid[0][0]][0], set()) or dfs(0, 0, directs[grid[0][0]][1], set())


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([[2,4,3],[6,5,2]],), True),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().hasValidPath(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()