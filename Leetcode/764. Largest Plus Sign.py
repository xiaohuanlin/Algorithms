'''
You are given an integer n. You have an n x n binary grid grid with all values initially 1's except for some indices given in the array mines. The ith element of the array mines is defined as mines[i] = [xi, yi] where grid[xi][yi] == 0.

Return the order of the largest axis-aligned plus sign of 1's contained in grid. If there is none, return 0.

An axis-aligned plus sign of 1's of order k has some center grid[r][c] == 1 along with four arms of length k - 1 going up, down, left, and right, and made of 1's. Note that there could be 0's or 1's beyond the arms of the plus sign, only the relevant area of the plus sign is checked for 1's.

 

Example 1:


Input: n = 5, mines = [[4,2]]
Output: 2
Explanation: In the above grid, the largest plus sign can only be of order 2. One of them is shown.
Example 2:


Input: n = 1, mines = [[0,0]]
Output: 0
Explanation: There is no plus sign, so return 0.
'''
from typing import *

import unittest
from pprint import pprint


class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        dp_left_top = [[(1, 1) for _ in range(n)] for _ in range(n)]
        dp_right_bottom = [[(1, 1) for _ in range(n)] for _ in range(n)]
        mines_set = set((i, j) for i,j in mines)
        for i,j in mines_set:
            dp_left_top[i][j] = (0, 0)
            dp_right_bottom[i][j] = (0, 0)

        for i in range(1, n):
            for j in range(1, n):
                if (i, j) in mines_set:
                    dp_left_top[i][j] = (0, 0)
                    continue
                x = 1
                y = 1
                if (i, j-1) not in mines_set:
                    x = dp_left_top[i][j-1][0] + 1
                if (i-1, j) not in mines_set:
                    y = dp_left_top[i-1][j][1] + 1
                dp_left_top[i][j] = (x, y)
        
        for i in range(n-2, -1, -1):
            for j in range(n-2, -1, -1):
                if (i, j) in mines_set:
                    dp_right_bottom[i][j] = (0, 0)
                    continue
                x = 1
                y = 1
                if (i, j+1) not in mines_set:
                    x = dp_right_bottom[i][j+1][0] + 1
                if (i+1, j) not in mines_set:
                    y = dp_right_bottom[i+1][j][1] + 1
                dp_right_bottom[i][j] = (x, y)
        
        res = 0
        for i in range(n):
            for j in range(n):
                length = min(dp_left_top[i][j][0], dp_left_top[i][j][1], dp_right_bottom[i][j][0], dp_right_bottom[i][j][1])
                res = max(res, length)
        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((5, [[4,2]],), 2),
            ((1, [[0,0]],), 0),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().orderOfLargestPlusSign(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
