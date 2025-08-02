'''
You are given an m x n matrix grid and a positive integer k. An island is a group of positive integers (representing land) that are 4-directionally connected (horizontally or vertically).

The total value of an island is the sum of the values of all cells in the island.

Return the number of islands with a total value divisible by k.

 

Example 1:


Input: grid = [[0,2,1,0,0],[0,5,0,0,5],[0,0,1,0,0],[0,1,4,7,0],[0,2,0,0,8]], k = 5

Output: 2

Explanation:

The grid contains four islands. The islands highlighted in blue have a total value that is divisible by 5, while the islands highlighted in red do not.

Example 2:


Input: grid = [[3,0,3,0], [0,3,0,3], [3,0,3,0]], k = 3

Output: 6

Explanation:

The grid contains six islands, each with a total value that is divisible by 3.

 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 1000
1 <= m * n <= 105
0 <= grid[i][j] <= 106
1 <= k <= 106
'''
import unittest
from typing import *


class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        row = len(grid)
        col = len(grid[0])
        def dfs(x, y):
            res = grid[x][y]
            grid[x][y] = 0
            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                nx = x + dx
                ny = y + dy
                if nx < 0 or nx >= row or ny < 0 or ny >= col or grid[nx][ny] == 0:
                    continue
                res += dfs(nx, ny)
            return res
        
        ans = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    continue
                res = dfs(i, j)
                if res > 0 and res % k == 0:
                    ans += 1
        return ans
    
        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([[0,2,1,0,0],[0,5,0,0,5],[0,0,1,0,0],[0,1,4,7,0],[0,2,0,0,8]], 5), 2),
            (([[3,0,3,0], [0,3,0,3], [3,0,3,0]], 3), 6),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().countIslands(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
