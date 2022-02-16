'''
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
'''

from typing import *

import unittest
from  collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        row = len(grid)
        col = len(grid[0])
        all_zero = True
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] != 0:
                    all_zero = False
        if all_zero:
            return 0 

        dis = -1
        while q:
            size = len(q)
            for _ in range(size):
                x, y = q.popleft()

                for x_delta, y_delta in ((0, -1), (-1, 0), (0, 1), (1, 0)):
                    next_x = x + x_delta
                    next_y = y + y_delta
                    if next_x < 0 or next_x >= row or next_y < 0 or next_y >= col:
                        continue
                    if grid[next_x][next_y] == 0 or grid[next_x][next_y] == 2:
                        continue
                    grid[next_x][next_y] = 2
                    q.append((next_x, next_y))
            dis += 1

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return -1
        return dis
        

        
class TestSolution(unittest.TestCase):
    def test_case(self):
        examples = (
            (([[2,2],[1,1],[0,0],[2,0]], ), 1),
            (([[2,1,1],[1,1,0],[0,1,1]], ), 4),
            (([[2,1,1],[0,1,1],[1,0,1]], ), -1),
            (([[0,2]], ), 0),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().orangesRotting(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

