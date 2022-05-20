'''
An n x n grid is composed of 1 x 1 squares where each 1 x 1 square consists of a '/', '\', or blank space ' '. These characters divide the square into contiguous regions.

Given the grid grid represented as a string array, return the number of regions.

Note that backslash characters are escaped, so a '\' is represented as '\\'.

 

Example 1:


Input: grid = [" /","/ "]
Output: 2
Example 2:


Input: grid = [" /","  "]
Output: 1
Example 3:


Input: grid = ["/\\","\\/"]
Output: 5
Explanation: Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.
 

Constraints:

n == grid.length == grid[i].length
1 <= n <= 30
grid[i][j] is either '/', '\', or ' '.
'''
import unittest

from typing import *

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        row = len(grid)
        col = len(grid[0])
        graph = [[0 for _ in range(3 * col)] for _ in range(3 * row)]
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '/':
                    graph[3 * i + 2][3 * j] = 1
                    graph[3 * i + 1][3 * j + 1] = 1
                    graph[3 * i][3 * j + 2] = 1
                elif grid[i][j] == '\\':
                    graph[3 * i][3 * j] = 1
                    graph[3 * i + 1][3 * j + 1] = 1
                    graph[3 * i + 2][3 * j + 2] = 1
        
        count = 0
        
        def dfs(i, j):
            if i < 0 or i >= len(graph) or j < 0 or j >= len(graph[0]):
                return
            if graph[i][j] == 1:
                return
            graph[i][j] = 1
            for x_d, y_d in ((0,1),(0,-1),(1,0),(-1,0)):
                dfs(x_d + i, y_d + j)
            
        
        for i in range(len(graph)):
            for j in range(len(graph[0])):
                if graph[i][j] == 0:
                    dfs(i, j)
                    count += 1
        return count

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([" /","  "],), 1),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().regionsBySlashes(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()