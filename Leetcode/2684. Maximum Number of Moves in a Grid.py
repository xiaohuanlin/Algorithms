'''
You are given a 0-indexed m x n matrix grid consisting of positive integers.

You can start at any cell in the first column of the matrix, and traverse the grid in the following way:

From a cell (row, col), you can move to any of the cells: (row - 1, col + 1), (row, col + 1) and (row + 1, col + 1) such that the value of the cell you move to, should be strictly bigger than the value of the current cell.
Return the maximum number of moves that you can perform.



Example 1:


Input: grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
Output: 3
Explanation: We can start at the cell (0, 0) and make the following moves:
- (0, 0) -> (0, 1).
- (0, 1) -> (1, 2).
- (1, 2) -> (2, 3).
It can be shown that it is the maximum number of moves that can be made.
Example 2:


Input: grid = [[3,2,4],[2,1,9],[1,1,7]]
Output: 0
Explanation: Starting from any cell in the first column we cannot perform any moves.


Constraints:

m == grid.length
n == grid[i].length
2 <= m, n <= 1000
4 <= m * n <= 105
1 <= grid[i][j] <= 106
'''
import unittest

from typing import *

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        depth = 0
        queue = []
        row = len(grid)
        col = len(grid[0])

        for i in range(row):
            queue.append((i, 0))

        while queue:
            next_queue = set()
            for i in range(len(queue)):
                x, y = queue.pop()
                if x + 1 < row and y + 1 < col and grid[x+1][y+1] > grid[x][y]:
                    next_queue.add((x + 1, y + 1))
                if x - 1 >= 0 and y + 1 < col and grid[x-1][y+1] > grid[x][y]:
                    next_queue.add((x - 1, y + 1))
                if y + 1 < col and grid[x][y+1] > grid[x][y]:
                    next_queue.add((x, y + 1))
                depth = max(depth, y)
            queue = sorted(list(next_queue))
        return depth


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]],),3),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maxMoves(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
