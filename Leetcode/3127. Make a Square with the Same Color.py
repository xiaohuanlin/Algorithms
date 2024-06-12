'''
You are given a 2D matrix grid of size 3 x 3 consisting only of characters 'B' and 'W'. Character 'W' represents the white color, and character 'B' represents the black color.

Your task is to change the color of at most one cell so that the matrix has a 2 x 2 square where all cells are of the same color.

Return true if it is possible to create a 2 x 2 square of the same color, otherwise, return false.



Example 1:










Input: grid = [["B","W","B"],["B","W","W"],["B","W","B"]]

Output: true

Explanation:

It can be done by changing the color of the grid[0][2].

Example 2:










Input: grid = [["B","W","B"],["W","B","W"],["B","W","B"]]

Output: false

Explanation:

It cannot be done by changing at most one cell.

Example 3:










Input: grid = [["B","W","B"],["B","W","W"],["B","W","W"]]

Output: true

Explanation:

The grid already contains a 2 x 2 square of the same color.



Constraints:

grid.length == 3
grid[i].length == 3
grid[i][j] is either 'W' or 'B'.
'''
import unittest

from typing import *


class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        for i in range(len(grid) - 1):
            for j in range(len(grid) - 1):
                l = [grid[i][j], grid[i][j+1], grid[i+1][j], grid[i+1][j+1]]
                if l.count('W') <= 1 or l.count('B') <= 1:
                    return True
        return False


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([["B","W","B"],["B","W","W"],["B","W","W"]],), True),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().canMakeSquare(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
