'''
You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.

Return the number of servers that communicate with any other server.

 

Example 1:



Input: grid = [[1,0],[0,1]]
Output: 0
Explanation: No servers can communicate with others.
Example 2:



Input: grid = [[1,0],[1,1]]
Output: 3
Explanation: All three servers can communicate with at least one other server.
Example 3:



Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
Output: 4
Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m <= 250
1 <= n <= 250
grid[i][j] == 0 or 1
'''
from asyncore import close_all
from typing import *

import unittest


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        row_set = {}
        col_set = {}
        connected = set()
        for i in range(row):
            for j in range(col):
                if grid[i][j] != 1:
                    continue
                if i in row_set or j in col_set:
                    if i in row_set:
                        connected.add(row_set[i])
                    if j in col_set:
                        connected.add(col_set[j])
                    connected.add((i, j))

                row_set.setdefault(i, (i, j))
                col_set.setdefault(j, (i, j))
                            
        return len(connected)
                    
                


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ([[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]], 4),
            ([[1,0],[1,1]], 3),
            ([[1,0],[0,1]], 0)
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().countServers(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
