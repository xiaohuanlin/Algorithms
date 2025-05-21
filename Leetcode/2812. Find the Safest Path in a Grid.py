'''
You are given a 0-indexed 2D matrix grid of size n x n, where (r, c) represents:

A cell containing a thief if grid[r][c] = 1
An empty cell if grid[r][c] = 0
You are initially positioned at cell (0, 0). In one move, you can move to any adjacent cell in the grid, including cells containing thieves.

The safeness factor of a path on the grid is defined as the minimum manhattan distance from any cell in the path to any thief in the grid.

Return the maximum safeness factor of all paths leading to cell (n - 1, n - 1).

An adjacent cell of cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) and (r - 1, c) if it exists.

The Manhattan distance between two cells (a, b) and (x, y) is equal to |a - x| + |b - y|, where |val| denotes the absolute value of val.

 

Example 1:


Input: grid = [[1,0,0],[0,0,0],[0,0,1]]
Output: 0
Explanation: All paths from (0, 0) to (n - 1, n - 1) go through the thieves in cells (0, 0) and (n - 1, n - 1).
Example 2:


Input: grid = [[0,0,1],[0,0,0],[0,0,0]]
Output: 2
Explanation: The path depicted in the picture above has a safeness factor of 2 since:
- The closest cell of the path to the thief at cell (0, 2) is cell (0, 0). The distance between them is | 0 - 0 | + | 0 - 2 | = 2.
It can be shown that there are no other paths with a higher safeness factor.
Example 3:


Input: grid = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]
Output: 2
Explanation: The path depicted in the picture above has a safeness factor of 2 since:
- The closest cell of the path to the thief at cell (0, 3) is cell (1, 2). The distance between them is | 0 - 1 | + | 3 - 2 | = 2.
- The closest cell of the path to the thief at cell (3, 0) is cell (3, 2). The distance between them is | 3 - 3 | + | 0 - 2 | = 2.
It can be shown that there are no other paths with a higher safeness factor.
 

Constraints:

1 <= grid.length == n <= 400
grid[i].length == n
grid[i][j] is either 0 or 1.
There is at least one thief in the grid.
'''
import unittest
from typing import *

from collections import deque


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        def bfs(x, y, maxd):
            if maxd > grid[x][y] - 1:
                return False
            
            visited = [[False for _ in range(col)] for _ in range(row)]
            q = deque([(x, y)])
            while q:
                x, y = q.popleft()
                if visited[x][y]:
                    continue
                visited[x][y] = True
                for (x_d, y_d) in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                    if x+x_d < 0 or x+x_d >= row or y+y_d < 0 or y+y_d >= col or maxd > grid[x+x_d][y+y_d] - 1:
                        continue
                    if x+x_d == row - 1 and y+y_d == col - 1:
                        return True
                    q.append((x+x_d, y+y_d))
            return False

        q = deque([])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    q.append((i, j))
        while q:
            x, y = q.popleft()
            for (x_d, y_d) in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                if x+x_d < 0 or x+x_d >= row or y+y_d < 0 or y+y_d >= col or grid[x+x_d][y+y_d] > 0:
                    continue
                grid[x+x_d][y+y_d] = grid[x][y] + 1
                q.append((x+x_d, y+y_d))
        
        start = 0
        end = 2 * row
        while start < end:
            middle = (start + end + 1) // 2
            if bfs(0, 0, middle):
                start = middle
            else:
                end = middle - 1
        return start


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([[1,0,0],[0,0,0],[0,0,1]],), 0),
            (([[0,0,1],[0,0,0],[0,0,0]],), 2),
            (([[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]],), 2),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maximumSafenessFactor(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

