'''
You are given a 2D integer array grid with size m x n. You are also given an integer k.

Your task is to calculate the number of paths you can take from the top-left cell (0, 0) to the bottom-right cell (m - 1, n - 1) satisfying the following constraints:

You can either move to the right or down. Formally, from the cell (i, j) you may move to the cell (i, j + 1) or to the cell (i + 1, j) if the target cell exists.
The XOR of all the numbers on the path must be equal to k.
Return the total number of such paths.

Since the answer can be very large, return the result modulo 109 + 7.

 

Example 1:

Input: grid = [[2, 1, 5], [7, 10, 0], [12, 6, 4]], k = 11

Output: 3

Explanation: 

The 3 paths are:

(0, 0) → (1, 0) → (2, 0) → (2, 1) → (2, 2)
(0, 0) → (1, 0) → (1, 1) → (1, 2) → (2, 2)
(0, 0) → (0, 1) → (1, 1) → (2, 1) → (2, 2)
Example 2:

Input: grid = [[1, 3, 3, 3], [0, 3, 3, 2], [3, 0, 1, 1]], k = 2

Output: 5

Explanation:

The 5 paths are:

(0, 0) → (1, 0) → (2, 0) → (2, 1) → (2, 2) → (2, 3)
(0, 0) → (1, 0) → (1, 1) → (2, 1) → (2, 2) → (2, 3)
(0, 0) → (1, 0) → (1, 1) → (1, 2) → (1, 3) → (2, 3)
(0, 0) → (0, 1) → (1, 1) → (1, 2) → (2, 2) → (2, 3)
(0, 0) → (0, 1) → (0, 2) → (1, 2) → (2, 2) → (2, 3)
Example 3:

Input: grid = [[1, 1, 1, 2], [3, 0, 3, 2], [3, 0, 2, 2]], k = 10

Output: 0

 

Constraints:

1 <= m == grid.length <= 300
1 <= n == grid[r].length <= 300
0 <= grid[r][c] < 16
0 <= k < 16
'''
from functools import cache
import unittest

from typing import *


class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        @cache
        def get_result(x, y, v):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                return 0
            if x == 0 and y == 0 and v == grid[0][0]:
                return 1
            return (get_result(x-1, y, v ^ grid[x][y]) + get_result(x, y-1, v ^ grid[x][y])) % int(1e9 + 7)
        
        return get_result(len(grid)-1, len(grid[0])-1, k)


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([[2, 1, 5], [7, 10, 0], [12, 6, 4]], 11), 3),
            (([[1, 3, 3, 3], [0, 3, 3, 2], [3, 0, 1, 1]], 2), 5),
            (([[1, 1, 1, 2], [3, 0, 3, 2], [3, 0, 2, 2]], 10), 0),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().countPathsWithXorValue(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
