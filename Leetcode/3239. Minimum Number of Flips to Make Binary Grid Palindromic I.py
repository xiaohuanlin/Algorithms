'''
You are given an m x n binary matrix grid.

A row or column is considered palindromic if its values read the same forward and backward.

You can flip any number of cells in grid from 0 to 1, or from 1 to 0.

Return the minimum number of cells that need to be flipped to make either all rows palindromic or all columns palindromic.



Example 1:

Input: grid = [[1,0,0],[0,0,0],[0,0,1]]

Output: 2

Explanation:



Flipping the highlighted cells makes all the rows palindromic.

Example 2:

Input: grid = [[0,1],[0,1],[0,0]]

Output: 1

Explanation:



Flipping the highlighted cell makes all the columns palindromic.

Example 3:

Input: grid = [[1],[0]]

Output: 0

Explanation:

All rows are already palindromic.



Constraints:

m == grid.length
n == grid[i].length
1 <= m * n <= 2 * 105
0 <= grid[i][j] <= 1
'''
from typing import *
import unittest


class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        ans = float('inf')

        res = 0
        for i in range(row):
            cnt = 0
            for j in range(col):
                cnt += grid[i][j] ^ grid[i][-j-1]
            res += cnt // 2
        ans = min(ans, res)

        res = 0
        for j in range(col):
            cnt = 0
            for i in range(row):
                cnt += grid[i][j] ^ grid[-i-1][j]
            res += cnt // 2
        ans = min(ans, res)
        return ans


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([[1,0,0],[0,0,0],[0,0,1]],),2),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().minFlips(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
