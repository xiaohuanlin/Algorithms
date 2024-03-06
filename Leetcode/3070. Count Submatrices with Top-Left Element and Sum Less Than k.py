'''
You are given a 0-indexed integer matrix grid and an integer k.

Return the number of
submatrices
 that contain the top-left element of the grid, and have a sum less than or equal to k.



Example 1:


Input: grid = [[7,6,3],[6,6,1]], k = 18
Output: 4
Explanation: There are only 4 submatrices, shown in the image above, that contain the top-left element of grid, and have a sum less than or equal to 18.
Example 2:


Input: grid = [[7,2,9],[1,5,0],[2,6,6]], k = 20
Output: 6
Explanation: There are only 6 submatrices, shown in the image above, that contain the top-left element of grid, and have a sum less than or equal to 20.


Constraints:

m == grid.length
n == grid[i].length
1 <= n, m <= 1000
0 <= grid[i][j] <= 1000
1 <= k <= 109
'''

from typing import *

import unittest


class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        row = len(grid)
        col = len(grid[0])
        sums = [[0 for _ in range(col+1)] for _ in range(row+1)]

        res = 0
        for i in range(1, row+1):
            for j in range(1, col+1):
                sums[i][j] = sums[i-1][j] + sums[i][j-1] - sums[i-1][j-1] + grid[i-1][j-1]
                if sums[i][j] <= k:
                    res += 1
        return res


class TestSolution(unittest.TestCase):
    def test_case(self):
        examples = (
            (([[7,2,9],[1,5,0],[2,6,6]],20),6),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().countSubmatrices(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

