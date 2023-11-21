'''
You are given an n x n integer matrix grid.

Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:

maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.
In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.

Return the generated matrix.

 

Example 1:


Input: grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
Output: [[9,9],[8,6]]
Explanation: The diagram above shows the original matrix and the generated matrix.
Notice that each value in the generated matrix corresponds to the largest value of a contiguous 3 x 3 matrix in grid.
Example 2:


Input: grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]
Output: [[2,2,2],[2,2,2],[2,2,2]]
Explanation: Notice that the 2 is contained within every contiguous 3 x 3 matrix in grid.
 

Constraints:

n == grid.length == grid[i].length
3 <= n <= 100
1 <= grid[i][j] <= 100
'''
import unittest

from typing import *


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        row = len(grid)
        col = len(grid[0])

        res = [[0 for _ in range(col-2)] for _ in range(row-2)]
        for i in range(row):
            for j in range(col):
                for x_d in {-2, -1, 0}:
                    for y_d in {-2, -1, 0}:
                        if i + x_d >= 0 and i + x_d < row -2 and j + y_d >= 0 and j + y_d < col - 2:
                            res[i+x_d][j+y_d] = max(res[i+x_d][j+y_d], grid[i][j])
        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]],),[[9,9],[8,6]]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().largestLocal(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
