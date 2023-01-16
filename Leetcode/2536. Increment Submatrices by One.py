'''
You are given a positive integer n, indicating that we initially have an n x n 0-indexed integer matrix mat filled with zeroes.

You are also given a 2D integer array query. For each query[i] = [row1i, col1i, row2i, col2i], you should do the following operation:

Add 1 to every element in the submatrix with the top left corner (row1i, col1i) and the bottom right corner (row2i, col2i). That is, add 1 to mat[x][y] for for all row1i <= x <= row2i and col1i <= y <= col2i.
Return the matrix mat after performing every query.

 

Example 1:


Input: n = 3, queries = [[1,1,2,2],[0,0,1,1]]
Output: [[1,1,0],[1,2,1],[0,1,1]]
Explanation: The diagram above shows the initial matrix, the matrix after the first query, and the matrix after the second query.
- In the first query, we add 1 to every element in the submatrix with the top left corner (1, 1) and bottom right corner (2, 2).
- In the second query, we add 1 to every element in the submatrix with the top left corner (0, 0) and bottom right corner (1, 1).
Example 2:


Input: n = 2, queries = [[0,0,1,1]]
Output: [[1,1],[1,1]]
Explanation: The diagram above shows the initial matrix and the matrix after the first query.
- In the first query we add 1 to every element in the matrix.
 

Constraints:

1 <= n <= 500
1 <= queries.length <= 104
0 <= row1i <= row2i < n
0 <= col1i <= col2i < n
'''

from typing import *
import unittest

class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        m = [[0 for _ in range(n+1)] for _ in range(n+1)]
        
        for r1, c1, r2, c2 in queries:
            m[r1][c1] += 1
            m[r2+1][c2+1] += 1
            m[r1][c2+1] -= 1
            m[r2+1][c1] -= 1

        pre_m = [[0 for _ in range(n+2)] for _ in range(n+2)]
        for i in range(n+1)[::-1]:
            for j in range(n+1)[::-1]:
                pre_m[i][j] = pre_m[i][j+1] + pre_m[i+1][j] - pre_m[i+1][j+1] + m[i][j]

        res = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                res[i][j] = pre_m[i+1][j+1]
        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((3, [[1,1,2,2],[0,0,1,1]]), [[1,1,0],[1,2,1],[0,1,1]]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().rangeAddQueries(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()