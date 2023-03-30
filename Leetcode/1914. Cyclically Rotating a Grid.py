'''
You are given an m x n integer matrix grid​​​, where m and n are both even integers, and an integer k.

The matrix is composed of several layers, which is shown in the below image, where each color is its own layer:



A cyclic rotation of the matrix is done by cyclically rotating each layer in the matrix. To cyclically rotate a layer once, each element in the layer will take the place of the adjacent element in the counter-clockwise direction. An example rotation is shown below:


Return the matrix after applying k cyclic rotations to it.



Example 1:


Input: grid = [[40,10],[30,20]], k = 1
Output: [[10,20],[40,30]]
Explanation: The figures above represent the grid at every state.
Example 2:


Input: grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], k = 2
Output: [[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]]
Explanation: The figures above represent the grid at every state.


Constraints:

m == grid.length
n == grid[i].length
2 <= m, n <= 50
Both m and n are even integers.
1 <= grid[i][j] <= 5000
1 <= k <= 109
'''
import unittest

from typing import *


class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        row = len(grid)
        col = len(grid[0])
        i = 0
        j = 0
        while i != row and j != col:
            store = []
            x = i
            y = j
            # top
            while y < col:
                store.append(grid[x][y])
                y += 1
            y -= 1
            x += 1
            # right
            while x < row:
                store.append(grid[x][y])
                x += 1
            x -= 1
            y -= 1
            # bottom
            while y >= j:
                store.append(grid[x][y])
                y -= 1
            y += 1
            x -= 1
            # left
            while x > i:
                store.append(grid[x][y])
                x -= 1

            m = 0
            # top
            while y < col:
                grid[x][y] = store[(m+k) % len(store)]
                m += 1
                y += 1
            y -= 1
            x += 1
            # right
            while x < row:
                grid[x][y] = store[(m+k) % len(store)]
                m += 1
                x += 1
            x -= 1
            y -= 1
            # bottom
            while y >= j:
                grid[x][y] = store[(m+k) % len(store)]
                m += 1
                y -= 1
            y += 1
            x -= 1
            # left
            while x > i:
                grid[x][y] = store[(m+k) % len(store)]
                m += 1
                x -= 1

            i += 1
            j += 1
            row -= 1
            col -= 1
        return grid


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], 2), [[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().rotateGrid(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
