'''
You are given an m x n integer matrix grid.

We define an hourglass as a part of the matrix with the following form:


Return the maximum sum of the elements of an hourglass.

Note that an hourglass cannot be rotated and must be entirely contained within the matrix.

 

Example 1:


Input: grid = [[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,1,2,9]]
Output: 30
Explanation: The cells shown above represent the hourglass with the maximum sum: 6 + 2 + 1 + 2 + 9 + 2 + 8 = 30.
Example 2:


Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
Output: 35
Explanation: There is only one hourglass in the matrix, with the sum: 1 + 2 + 3 + 5 + 7 + 8 + 9 = 35.
 

Constraints:

m == grid.length
n == grid[i].length
3 <= m, n <= 150
0 <= grid[i][j] <= 106
'''
from typing import *
import unittest

class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        dp = [[0 for _ in range(col + 1)] for _ in range(row + 1)]
        
        res = 0
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + grid[i-1][j-1]
                if i - 3 >= 0 and j - 3 >= 0:
                    res = max(res, 
                        dp[i][j] - dp[i-3][j] - dp[i][j-3] + dp[i-3][j-3] - grid[i-2][j-3] - grid[i-2][j-1]
                    )
        return res



class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([[1,2,3],[4,5,6],[7,8,9]],),35),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maxSum(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
