'''
Given a 2D character matrix grid, where grid[i][j] is either 'X', 'Y', or '.', return the number of 
submatrices
 that contains:

grid[0][0]
an equal frequency of 'X' and 'Y'.
at least one 'X'.
 

Example 1:

Input: grid = [["X","Y","."],["Y",".","."]]

Output: 3

Explanation:



Example 2:

Input: grid = [["X","X"],["X","Y"]]

Output: 0

Explanation:

No submatrix has an equal frequency of 'X' and 'Y'.

Example 3:

Input: grid = [[".","."],[".","."]]

Output: 0

Explanation:

No submatrix has at least one 'X'.

 

Constraints:

1 <= grid.length, grid[i].length <= 1000
grid[i][j] is either 'X', 'Y', or '.'.
'''
from typing import *
import unittest


class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        dp = [[[0, 0] for _ in range(col+1)] for _ in range(row+1)]
        res = 0

        for i in range(1, row + 1):
            for j in range(1, col + 1):
                dp[i][j][0] = dp[i-1][j][0] + dp[i][j-1][0] - dp[i-1][j-1][0] + (grid[i-1][j-1] == 'X')
                dp[i][j][1] = dp[i-1][j][1] + dp[i][j-1][1] - dp[i-1][j-1][1] + (grid[i-1][j-1] == 'Y')
                if dp[i][j][0] == dp[i][j][1] and dp[i][j][0] > 0:
                    res += 1
        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([["X","X"],["X","Y"]],),0),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().numberOfSubmatrices(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()