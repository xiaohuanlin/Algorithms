'''
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

 

Example 1:


Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Example 2:

Input: heights = [[2,1],[1,2]]
Output: [[0,0],[0,1],[1,0],[1,1]]
 

Constraints:

m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 105
'''
from typing import *

import unittest


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row = len(heights)
        col = len(heights[0])
        pacific = [[False for _ in range(col)] for _ in range(row)]
        atlantic = [[False for _ in range(col)] for _ in range(row)]

        for i in range(row):
            # start from left point of every row
            self.dfs(heights, i, 0, row, col, pacific)
            # start from right point of every row
            self.dfs(heights, i, col - 1, row, col, atlantic)

        for j in range(col):
            # start from top point of every col
            self.dfs(heights, 0, j, row, col, pacific)
            # start from bottom point of every col
            self.dfs(heights, row - 1, j, row, col, atlantic)
            
        res = []
        for i in range(row):
            for j in range(col):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i, j])

        return res
        
    def dfs(self, heights, x, y, row, col, visit):
        visit[x][y] = True
        for x_del, y_del in ((0, 1), (0, -1), (-1, 0), (1, 0)):
            next_x = x + x_del
            next_y = y + y_del
            if not self.valid(next_x, next_y, row, col) or visit[next_x][next_y] or heights[next_x][next_y] < heights[x][y]:
                continue
            self.dfs(heights, next_x, next_y, row, col, visit)

    def valid(self, x, y, row, col):
        return x >= 0 and x < row and y >= 0 and y < col


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]],), [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]),
            # (([[2,1],[1,2]],), [[0,0],[0,1],[1,0],[1,1]]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().pacificAtlantic(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
