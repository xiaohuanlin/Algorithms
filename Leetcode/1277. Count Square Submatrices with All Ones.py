'''
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

 

Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
Example 2:

Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.
 

Constraints:

1 <= arr.length <= 300
1 <= arr[0].length <= 300
0 <= arr[i][j] <= 1
'''
from typing import *

import unittest


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        # the length of this position max square matrix
        dp = [[0 for _ in range(col)] for _ in range(row)]
        res = 0 if matrix[0][0] == 0 else -1

        # first row
        for j in range(col):
            dp[0][j] = 1 if matrix[0][j] == 1 else 0
            res += dp[0][j]

        # first col
        for i in range(row):
            dp[i][0] = 1 if matrix[i][0] == 1 else 0
            res += dp[i][0]
        
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == 1:
                    dp[i][j] = min(dp[i][j - 1] + 1, dp[i - 1][j] + 1, dp[i - 1][j - 1] + 1)
                    res += dp[i][j]
        return res
        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (
                [
                    [0,1,1,1],
                    [1,1,1,1],
                    [0,1,1,1]
                ], 15
            ),
            (
                [
                    [1,0,1],
                    [1,1,0],
                    [1,1,0]
                ], 7
            ),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().countSquares(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
