'''
Given a m x n matrix mat and an integer k, return a matrix answer where each answer[i][j] is the sum of all elements mat[r][c] for:

i - k <= r <= i + k,
j - k <= c <= j + k, and
(r, c) is a valid position in the matrix.


Example 1:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[12,21,16],[27,45,33],[24,39,28]]
Example 2:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2
Output: [[45,45,45],[45,45,45],[45,45,45]]


Constraints:

m == mat.length
n == mat[i].length
1 <= m, n, k <= 100
1 <= mat[i][j] <= 100
'''
import unittest

from typing import *

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        sums = [[0 for _ in range(col+1)] for _ in range(row+1)]
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                sums[i][j] = sums[i-1][j] + sums[i][j-1] - sums[i-1][j-1] + mat[i-1][j-1]

        res = [[0 for _ in range(col)] for _ in range(row)]
        for i in range(row):
            for j in range(col):
                left_top = (max(i - k, 0), max(j - k, 0))
                left_bottom = (min(i + k + 1, row), max(j - k, 0))
                right_top = (max(i - k, 0), min(j + k + 1, col))
                right_bottom = (min(i + k + 1, row), min(j + k + 1, col))
                res[i][j] = sums[left_top[0]][left_top[1]] + sums[right_bottom[0]][right_bottom[1]] - sums[left_bottom[0]][left_bottom[1]] - sums[right_top[0]][right_top[1]]
        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([[1,2,3],[4,5,6],[7,8,9]], 1), [[12,21,16],[27,45,33],[24,39,28]]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().matrixBlockSum(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
