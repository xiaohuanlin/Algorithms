'''
You are given a binary matrix matrix of size m x n, and you are allowed to rearrange the columns of the matrix in any order.

Return the area of the largest submatrix within matrix where every element of the submatrix is 1 after reordering the columns optimally.



Example 1:


Input: matrix = [[0,0,1],[1,1,1],[1,0,1]]
Output: 4
Explanation: You can rearrange the columns as shown above.
The largest submatrix of 1s, in bold, has an area of 4.
Example 2:


Input: matrix = [[1,0,1,0,1]]
Output: 3
Explanation: You can rearrange the columns as shown above.
The largest submatrix of 1s, in bold, has an area of 3.
Example 3:

Input: matrix = [[1,1,0],[1,0,1]]
Output: 2
Explanation: Notice that you must rearrange entire columns, and there is no way to make a submatrix of 1s larger than an area of 2.


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m * n <= 105
matrix[i][j] is either 0 or 1.
'''
import unittest

from typing import *

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        col = len(matrix[0])
        current_height = [0 for _ in range(col)]
        res = 0
        for r in matrix:
            # maintain height
            for i in range(len(r)):
                if r[i] == 1:
                    current_height[i] += 1
                else:
                    current_height[i] = 0

            sorted_height = sorted(current_height)
            for i in range(len(sorted_height)):
                res = max(res, sorted_height[i] * (len(current_height) - i))
        return res



class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([[0,0,1],[1,1,1],[1,0,1]], ), 4),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().largestSubmatrix(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
