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
        # if there are only one points, the v will means 4 * v + 2 sides
        row = len(grid)
        col = len(grid[0])
        area, hor_de, vir_de = 0, 0, 0
        for i in range(row):
            for j in range(col):
                area += self.get_area(grid, i, j)
                if j != col - 1:
                    hor_de += min(grid[i][j], grid[i][j + 1])
                if i != row - 1:
                    vir_de += min(grid[i][j], grid[i + 1][j])
        return area - (hor_de + vir_de) * 2

    def get_area(self, grid, x, y):
        return 4 * grid[x][y] + 2 if grid[x][y] > 0 else 0


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
        self.assertEqual(Solution().surfaceArea(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
