'''
You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You can move up, down, left, or right from and to an empty cell in one step.

Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.

 

Example 1:


Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
Output: 6
Explanation: 
The shortest path without eliminating any obstacle is 10.
The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
Example 2:


Input: grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
Output: -1
Explanation: We need to eliminate at least two obstacles to find such a walk.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 40
1 <= k <= m * n
grid[i][j] is either 0 or 1.
grid[0][0] == grid[m - 1][n - 1] == 0
'''
from typing import *

import unittest
from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        row = len(grid)
        col = len(grid[0])
        mem = set()
        q = deque()
        q.append(((0,0), k))
        dis = 0
        while q:
            size = len(q)
            for _ in range(size):
                item = q.popleft()
                (x, y), eli = item
                if x >= row or x < 0 or y >= col or y < 0:
                    continue
                if item in mem:
                    continue
                if grid[x][y] == 1:
                    eli -= 1
                if eli < 0:
                    continue
                mem.add(item)
                if x == row - 1 and y == col - 1:
                    return dis
                for x_delta, y_delta in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    q.append(((x + x_delta, y + y_delta), eli))
                
            dis += 1
        return -1
            


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], 1), 6),
            (([[0,1,1],[1,1,1],[1,0,0]], 1), -1),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().shortestPath(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
