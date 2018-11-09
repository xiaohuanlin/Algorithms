'''

On a N * N grid, we place some 1 * 1 * 1 cubes.

Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).

Return the total surface area of the resulting shapes.



Example 1:

Input: [[2]]
Output: 10
Example 2:

Input: [[1,2],[3,4]]
Output: 34
Example 3:

Input: [[1,0],[0,2]]
Output: 16
Example 4:

Input: [[1,1,1],[1,0,1],[1,1,1]]
Output: 32
Example 5:

Input: [[2,2,2],[2,1,2],[2,2,2]]
Output: 46


Note:

1 <= N <= 50
0 <= grid[i][j] <= 50

'''
import unittest


class Solution:
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ([[2]], 10),
            ([[1,2],[3,4]], 34),
            ([[1,0],[0,2]], 16),
            ([[1,1,1],[1,0,1],[1,1,1]], 32),
            ([[2,2,2],[2,1,2],[2,2,2]], 46)
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().surfaceArea(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
