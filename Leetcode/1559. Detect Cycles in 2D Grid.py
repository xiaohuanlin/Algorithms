'''
Given a 2D array of characters grid of size m x n, you need to find if there exists any cycle consisting of the same value in grid.

A cycle is a path of length 4 or more in the grid that starts and ends at the same cell. From a given cell, you can move to one of the cells adjacent to it - in one of the four directions (up, down, left, or right), if it has the same value of the current cell.

Also, you cannot move to the cell that you visited in your last move. For example, the cycle (1, 1) -> (1, 2) -> (1, 1) is invalid because from (1, 2) we visited (1, 1) which was the last visited cell.

Return true if any cycle of the same value exists in grid, otherwise, return false.

 

Example 1:



Input: grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
Output: true
Explanation: There are two valid cycles shown in different colors in the image below:

Example 2:



Input: grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
Output: true
Explanation: There is only one valid cycle highlighted in the image below:

Example 3:



Input: grid = [["a","b","b"],["b","z","b"],["b","b","a"]]
Output: false
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 500
grid consists only of lowercase English letters.
'''

from typing import *

import unittest

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        row = len(grid)
        col = len(grid[0])
        cache = set()

        def dfs(x, y, parent_x, parent_y, cur_path, visited_path):
            if (x, y) in cur_path and len(cur_path) >= 3:
                return True
            cur_path.add((x, y))
            
            if (x, y) in visited_path:
                return False
            visited_path.add((x, y))
            
            for x_d, y_d in ((0,1), (1,0), (-1,0), (0,-1)):
                next_x = x_d + x
                next_y = y_d + y
                if next_x == parent_x and next_y == parent_y:
                    continue

                if next_x >= 0 and next_x < row and next_y >= 0 and next_y < col and grid[x][y] == grid[next_x][next_y]:
                    if dfs(next_x, next_y, x, y, cur_path, visited_path):
                        return True
            cur_path.remove((x, y))
            return False
                
        
        for i in range(row):
            for j in range(col):
                if (i, j) in cache:
                    continue
                cur_path = set()
                visited_path = set()
                if dfs(i, j, -1, -1, cur_path, visited_path):
                    return True
                cache |= visited_path
        return False
        
class TestSolution(unittest.TestCase):
    def test_case(self):
        examples = (
            (([["a","b","b"],["b","z","b"],["b","b","a"]],), False),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().containsCycle(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

