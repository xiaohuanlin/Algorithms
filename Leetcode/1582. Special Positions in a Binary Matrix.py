'''
Given an m x n binary matrix mat, return the number of special positions in mat.

A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).



Example 1:


Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
Output: 1
Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.
Example 2:


Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
Explanation: (0, 0), (1, 1) and (2, 2) are special positions.


Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 100
mat[i][j] is either 0 or 1.
'''
from typing import *

import unittest
from collections import defaultdict

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row = len(mat)
        col = len(mat[0])
        rows = defaultdict(list)
        cols = defaultdict(list)
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 1:
                    rows[i].append(j)
                    cols[j].append(i)

        res = 0
        for _, v in rows.items():
            if len(v) == 0 or len(v) > 1:
                continue

            if len(cols[v[0]]) == 0 or len(cols[v[0]]) > 1:
                continue

            res += 1
        return res



class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([[0,0,1,0],[0,0,0,0],[0,0,0,0],[0,1,0,0]],),2),
            (([[1,0,0],[0,1,0],[0,0,1]],),3),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().numSpecial(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
