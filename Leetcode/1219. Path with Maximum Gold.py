'''
In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

Every time you are located in a cell you will collect all the gold in that cell.
From your position, you can walk one step to the left, right, up, or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.
 

Example 1:

Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
Explanation:
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7.
Example 2:

Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
Output: 28
Explanation:
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 15
0 <= grid[i][j] <= 100
There are at most 25 cells containing gold.
'''
from collections import defaultdict
from typing import *

import unittest


class Solution:
    max_v = 0
    
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        for i in range(row):
            for j in range(col):
                if grid[i][j] != 0:
                    tmp = grid[i][j]
                    grid[i][j] = 0
                    self.backtrace(i, j, tmp, grid)
                    grid[i][j] = tmp
        return self.max_v
    
    def backtrace(self, x: int, y: int, sum: int, grid: List[List]):
        self.max_v = max(self.max_v, sum)

        for i, j in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] != 0:
                tmp = grid[i][j]
                grid[i][j] = 0
                self.backtrace(i, j, sum + tmp, grid)
                grid[i][j] = tmp
        

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ([[0,6,0],[5,8,7],[0,9,0]], 24),
            ([[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]], 28)
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().getMaximumGold(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
