'''
You are given a 2D binary array grid. Find a rectangle with horizontal and vertical sides with the smallest area, such that all the 1's in grid lie inside this rectangle.

Return the minimum possible area of the rectangle.

 

Example 1:

Input: grid = [[0,1,0],[1,0,1]]

Output: 6

Explanation:



The smallest rectangle has a height of 2 and a width of 3, so it has an area of 2 * 3 = 6.

Example 2:

Input: grid = [[0,0],[1,0]]

Output: 1

Explanation:



The smallest rectangle has both height and width 1, so its area is 1 * 1 = 1.

 

Constraints:

1 <= grid.length, grid[i].length <= 1000
grid[i][j] is either 0 or 1.
The input is generated such that there is at least one 1 in grid.
'''
import unittest

from typing import *


class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        y_min = x_min = float('inf')
        y_max = x_max = float('-inf')

        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    x_min = min(x_min, i)
                    x_max = max(x_max, i)
                    y_min = min(y_min, j)
                    y_max = max(y_max, j)
        return (x_max - x_min + 1) * (y_max - y_min + 1)
        
        
        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([[0,1,0],[1,0,1]],),6),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().minimumArea(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
