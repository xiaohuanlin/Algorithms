'''
Given an m x n binary matrix mat, return the number of submatrices that have all ones.

 

Example 1:


Input: mat = [[1,0,1],[1,1,0],[1,1,0]]
Output: 13
Explanation: 
There are 6 rectangles of side 1x1.
There are 2 rectangles of side 1x2.
There are 3 rectangles of side 2x1.
There is 1 rectangle of side 2x2. 
There is 1 rectangle of side 3x1.
Total number of rectangles = 6 + 2 + 3 + 1 + 1 = 13.
Example 2:


Input: mat = [[0,1,1,0],[0,1,1,1],[1,1,1,0]]
Output: 24
Explanation: 
There are 8 rectangles of side 1x1.
There are 5 rectangles of side 1x2.
There are 2 rectangles of side 1x3. 
There are 4 rectangles of side 2x1.
There are 2 rectangles of side 2x2. 
There are 2 rectangles of side 3x1. 
There is 1 rectangle of side 3x2. 
Total number of rectangles = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24.
 

Constraints:

1 <= m, n <= 150
mat[i][j] is either 0 or 1.
'''
import unittest

from typing import *

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        row = len(mat)
        col = len(mat[0])
        right_dp = [[0 for _ in range(col)] for _ in range(row)]
        for i in range(row):
            for j in range(col)[::-1]:
                right_dp[i][j] = (right_dp[i][j+1] if j+1 < col else 0) + 1 if mat[i][j] == 1 else 0

        down_dp = [[0 for _ in range(col)] for _ in range(row)]
        for j in range(col):
            for i in range(row)[::-1]:
                down_dp[i][j] = (down_dp[i+1][j] if i+1 < row else 0) + 1 if mat[i][j] == 1 else 0

        count = 0
        for i in range(row):
            for j in range(col):
                h = row
                for k in range(j, j + right_dp[i][j]):
                    h = min(h, down_dp[i][k])
                    count += h
        return count
        
        
        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([[1,1,1,1,0],[1,0,0,1,0],[0,0,1,0,1],[0,1,0,0,0]],), 17),
            # (([[1,0,1],[1,1,0],[1,1,0]],), 13),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().numSubmat(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
