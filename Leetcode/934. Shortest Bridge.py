'''
In a given 2D binary array grid, there are two islands.  (An island is a 4-directionally connected group of 1s not connected to any other 1s.)

Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.

Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)

 

Example 1:

Input: grid = [[0,1],[1,0]]
Output: 1
Example 2:

Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
 

Constraints:

2 <= grid.length == grid[0].length <= 100
grid[i][j] == 0 or grid[i][j] == 1
'''
from typing import *

import unittest


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        island = set()

        row = len(grid)
        col = len(grid[0])

        for i in range(row):
            for j in range(col):
                if grid[i][j] != 1:
                    continue

                # add all elements to island_1
                self.calculate_island(i, j, island, grid)
                break
            else:
                continue
            break

        queue = list(island)
        step = 0
        while queue:
            size = len(queue)
            for i in range(size):
                element = queue.pop(0)
                directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
                for direction in directions:
                    iter_i = element[0] + direction[0]
                    iter_j = element[1] + direction[1]

                    if (iter_i >= 0 and iter_i < len(grid) and iter_j >= 0 and iter_j < len(grid[0]) and grid[iter_i][iter_j] != -1):
                        if grid[iter_i][iter_j] == 0:
                            grid[iter_i][iter_j] = -1
                            queue.append((iter_i, iter_j))
                        else:
                            return step
            step += 1
        return -1

    def calculate_island(self, iter_i: int, iter_j: int, is_land: Set, grid: List[List]):
        if (iter_i >= 0 and iter_i < len(grid) and iter_j >= 0 and iter_j < len(grid[0]) and grid[iter_i][iter_j] == 1):
            grid[iter_i][iter_j] = -1
            is_land.add((iter_i, iter_j))

            directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
            for direction in directions:
                self.calculate_island(iter_i + direction[0], iter_j + direction[1], is_land, grid)



class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ([[0,1],[1,0]], 1),
            ([[0,1,0],[0,0,0],[0,0,1]], 2),
            ([[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]], 1),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().shortestBridge(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
