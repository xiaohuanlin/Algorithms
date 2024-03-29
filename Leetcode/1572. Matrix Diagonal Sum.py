'''
Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

 

Example 1:


Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.
Example 2:

Input: mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
Output: 8
Example 3:

Input: mat = [[5]]
Output: 5
 

Constraints:

n == mat.length == mat[i].length
1 <= n <= 100
1 <= mat[i][j] <= 100
'''
import unittest

from typing import *

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        l = len(mat)
        res = 0
        for i in range(l):
            res += (mat[i][i] + mat[l-1-i][i])
        if l % 2 == 1:
            res -= mat[l // 2][l // 2]
        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([[1,2,3],
              [4,5,6],
              [7,8,9]],), 25),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().diagonalSum(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
