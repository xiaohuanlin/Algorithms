'''
You are given an m x n binary matrix matrix.

You can choose any number of columns in the matrix and flip every cell in that column (i.e., Change the value of the cell from 0 to 1 or vice versa).

Return the maximum number of rows that have all values equal after some number of flips.

 

Example 1:

Input: matrix = [[0,1],[1,1]]
Output: 1
Explanation: After flipping no values, 1 row has all values equal.
Example 2:

Input: matrix = [[0,1],[1,0]]
Output: 2
Explanation: After flipping values in the first column, both rows have equal values.
Example 3:

Input: matrix = [[0,0,0],[0,0,1],[1,1,0]]
Output: 2
Explanation: After flipping values in the first two columns, the last two rows have equal values.
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is either 0 or 1.
'''

from typing import *

import unittest


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        maps = {}
        for row in matrix:
            key = tuple(row)
            reverse_key = tuple(int(n != 1) for n in row)
            if key in maps:
                maps[key] += 1
            elif reverse_key in maps:
                maps[reverse_key] += 1
            else:
                maps[key] = 1
        return max(maps.values())
        
class TestSolution(unittest.TestCase):
    def test_case(self):
        examples = (
            (([[0,0,0],[0,0,1],[1,1,0]],),2),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maxEqualRowsAfterFlips(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

