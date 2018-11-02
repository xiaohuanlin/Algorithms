'''

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.



Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

Explanation: The perimeter is the 16 yellow stripes in the image below:

'''
import unittest


class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # row = len(grid)
        # col = len(grid[0])
        # count = 0
        # for i in range(row):
        #     for j in range(col):
        #         if grid[i][j] == 1:
        #             # check the neighbor number
        #             for x, y in ((0, -1), (1, 0), (-1, 0), (0, 1)):
        #                 if i+x > row-1 or i+x < 0 or j+y > col-1 or j+y < 0:
        #                     count += 1
        #                 elif grid[i+x][j+y] == 0:
        #                     count += 1
        # return count
        # ----------------------
        row = len(grid)
        col = len(grid[0])
        count = 0
        for i in range(row):
            for j in range(col):
                if i == row - 1 or grid[i][j] != grid[i+1][j]:
                    count += 1
                    if i == row - 1 and grid[i][j] == 0:
                        count -= 1
                if j == col - 1 or grid[i][j+1] != grid[i][j]:
                    count += 1
                    if j == col - 1 and grid[i][j] == 0:
                        count -= 1

                # count the first row and col
                if i == 0 and grid[i][j] == 1:
                    count += 1
                if j == 0 and grid[i][j] == 1:
                    count += 1

        return count


class TestSolution(unittest.TestCase):

    def test_islandPerimeter(self):
        examples = (
            ([[0,1,0,0],
             [1,1,1,0],
             [0,1,0,0],
             [1,1,0,0]], 16),
            ([[1],
              [0]], 4),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().islandPerimeter(first), second, msg="first: {}; second: {}".format(first, second))

unittest.main()