'''
You are given a 2D boolean matrix grid.

Return an integer that is the number of right triangles that can be made with the 3 elements of grid such that all of them have a value of 1.

Note:

A collection of 3 elements of grid is a right triangle if one of its elements is in the same row with another element and in the same column with the third element. The 3 elements do not have to be next to each other.


Example 1:

0	1	0
0	1	1
0	1	0
0	1	0
0	1	1
0	1	0
Input: grid = [[0,1,0],[0,1,1],[0,1,0]]

Output: 2

Explanation:

There are two right triangles.

Example 2:

1	0	0	0
0	1	0	1
1	0	0	0
Input: grid = [[1,0,0,0],[0,1,0,1],[1,0,0,0]]

Output: 0

Explanation:

There are no right triangles.

Example 3:

1	0	1
1	0	0
1	0	0
1	0	1
1	0	0
1	0	0
Input: grid = [[1,0,1],[1,0,0],[1,0,0]]

Output: 2

Explanation:

There are two right triangles.



Constraints:

1 <= grid.length <= 1000
1 <= grid[i].length <= 1000
0 <= grid[i][j] <= 1
'''
import unittest

from typing import *


class Solution:

    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        rows_presum = [[0 for _ in range(col)] for _ in range(row)]
        cols_presum = [[0 for _ in range(col)] for _ in range(row)]

        for i in range(row):
            for j in range(col):
                rows_presum[i][j] = rows_presum[i][j-1] + grid[i][j]
                cols_presum[i][j] = cols_presum[i-1][j] + grid[i][j]

        res = 0
        for i in range(row):
            for j in range(col):
                top = cols_presum[i-1][j] if i > 0 else 0
                right = rows_presum[i][-1] - rows_presum[i][j]
                bottom = cols_presum[-1][j] - cols_presum[i][j]
                left = rows_presum[i][j-1] if j > 0 else 0
                if grid[i][j] == 1:
                    res += top * right + right * bottom + bottom * left + left * top
        return res



class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([[1,0,1],[1,0,0],[1,0,0]],),2),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().numberOfRightTriangles(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
