'''
You are given a 2D integer array grid of size m x n, where each cell contains a positive integer.

A cornered path is defined as a set of adjacent cells with at most one turn. More specifically, the path should exclusively move either horizontally or vertically up to the turn (if there is one), without returning to a previously visited cell. After the turn, the path will then move exclusively in the alternate direction: move vertically if it moved horizontally, and vice versa, also without returning to a previously visited cell.

The product of a path is defined as the product of all the values in the path.

Return the maximum number of trailing zeros in the product of a cornered path found in grid.

Note:

Horizontal movement means moving in either the left or right direction.
Vertical movement means moving in either the up or down direction.
 

Example 1:


Input: grid = [[23,17,15,3,20],[8,1,20,27,11],[9,4,6,2,21],[40,9,1,10,6],[22,7,4,5,3]]
Output: 3
Explanation: The grid on the left shows a valid cornered path.
It has a product of 15 * 20 * 6 * 1 * 10 = 18000 which has 3 trailing zeros.
It can be shown that this is the maximum trailing zeros in the product of a cornered path.

The grid in the middle is not a cornered path as it has more than one turn.
The grid on the right is not a cornered path as it requires a return to a previously visited cell.
Example 2:


Input: grid = [[4,3,2],[7,6,1],[8,8,8]]
Output: 0
Explanation: The grid is shown in the figure above.
There are no cornered paths in the grid that result in a product with a trailing zero.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 105
1 <= m * n <= 105
1 <= grid[i][j] <= 1000
'''
from typing import *

import unittest
    
from functools import lru_cache
class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        max_length = 0
        two_five = [[[[0, 0] for _ in range(2)] for _ in range(col + 1)] for _ in range(row + 1)]
        
        @lru_cache(None)
        def count_two(num):
            count = 0
            while num % 2 == 0:
                num = num // 2
                count += 1
            return count
        
        @lru_cache(None)
        def count_five(num):
            count = 0
            while num % 5 == 0:
                num = num // 5
                count += 1
            return count
        
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                # count left to right num
                two_five[i][j][0][0] = two_five[i][j-1][0][0] + count_two(grid[i-1][j-1])
                two_five[i][j][0][1] = two_five[i][j-1][0][1] + count_five(grid[i-1][j-1])

        for j in range(1, col + 1):
            for i in range(1, row + 1):
                # count up to down num
                two_five[i][j][1][0] = two_five[i-1][j][1][0] + count_two(grid[i-1][j-1])
                two_five[i][j][1][1] = two_five[i-1][j][1][1] + count_five(grid[i-1][j-1])
                
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                # up-left
                two_sum = (two_five[i][j][1][0] - two_five[0][j][1][0]) + (two_five[i][j][0][0] - two_five[i][0][0][0]) - count_two(grid[i-1][j-1])
                five_sum = (two_five[i][j][1][1] - two_five[0][j][1][1]) + (two_five[i][j][0][1] - two_five[i][0][0][1]) - count_five(grid[i-1][j-1])
                max_length = max(max_length, min(two_sum, five_sum))
                # up-right
                two_sum = (two_five[i][j][1][0] - two_five[0][j][1][0]) + (two_five[i][col][0][0] - two_five[i][j][0][0])
                five_sum = (two_five[i][j][1][1] - two_five[0][j][1][1]) + (two_five[i][col][0][1] - two_five[i][j][0][1])
                max_length = max(max_length, min(two_sum, five_sum))
                # down-right
                two_sum = (two_five[row][j][1][0] - two_five[i][j][1][0]) + (two_five[i][col][0][0] - two_five[i][j][0][0]) + count_two(grid[i-1][j-1])
                five_sum = (two_five[row][j][1][1] - two_five[i][j][1][1]) + (two_five[i][col][0][1] - two_five[i][j][0][1]) + count_five(grid[i-1][j-1])
                max_length = max(max_length, min(two_sum, five_sum))
                # down-left
                two_sum = (two_five[row][j][1][0] - two_five[i][j][1][0]) + (two_five[i][j][0][0] - two_five[i][0][0][0])
                five_sum = (two_five[row][j][1][1] - two_five[i][j][1][1]) + (two_five[i][j][0][1] - two_five[i][0][0][1])
                max_length = max(max_length, min(two_sum, five_sum))
        return max_length
        
        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([[23,17,15,3,20],[8,1,20,27,11],[9,4,6,2,21],[40,9,1,10,6],[22,7,4,5,3]],),3),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maxTrailingZeros(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
