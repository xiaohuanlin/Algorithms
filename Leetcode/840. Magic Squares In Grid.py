'''

A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).



Example 1:

Input: [[4,3,8,4],
        [9,5,1,9],
        [2,7,6,2]]
Output: 1
Explanation:
The following subgrid is a 3 x 3 magic square:
438
951
276

while this one is not:
384
519
762

In total, there is only one magic square inside the given grid.
Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
0 <= grid[i][j] <= 15

'''
import unittest


class Solution:
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        count = 0
        for i in range(row - 2):
            for j in range(col - 2):
                if self.isMagicSquares(grid, i, j):
                    count += 1
        return count

    def isMagicSquares(self, grid, i, j):
        standard_square = list(range(1,10))
        if sorted(grid[row][col] for row in range(i, i+3) for col in range(j, j+3)) != standard_square:
            return False
        # calculate row sum
        result = 0
        for row in range(i, i+3):
            if result == 0:
                result = sum(grid[row][j:j+3])
            else:
                if result != sum(grid[row][j:j+3]):
                    return False

        # calculate col sum
        for col in range(j, j+3):
            if result != sum(grid[row][j] for row in range(i, i+3)):
                return False

        # calculate dia number
        dia_1 = grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2]
        dia_2 = grid[i+2][j] + grid[i+1][j+1] + grid[i][j+2]
        if result != dia_1 or result != dia_2:
            return False
        return True


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ([[4, 3, 8, 4],
              [9, 5, 1, 9],
              [2, 7, 6, 2]], 1),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().numMagicSquaresInside(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
