'''
There is a dungeon with n x m rooms arranged as a grid.

You are given a 2D array moveTime of size n x m, where moveTime[i][j] represents the minimum time in seconds when you can start moving to that room. You start from the room (0, 0) at time t = 0 and can move to an adjacent room. Moving between adjacent rooms takes exactly one second.

Return the minimum time to reach the room (n - 1, m - 1).

Two rooms are adjacent if they share a common wall, either horizontally or vertically.

 

Example 1:

Input: moveTime = [[0,4],[4,4]]

Output: 6

Explanation:

The minimum time required is 6 seconds.

At time t == 4, move from room (0, 0) to room (1, 0) in one second.
At time t == 5, move from room (1, 0) to room (1, 1) in one second.
Example 2:

Input: moveTime = [[0,0,0],[0,0,0]]

Output: 3

Explanation:

The minimum time required is 3 seconds.

At time t == 0, move from room (0, 0) to room (1, 0) in one second.
At time t == 1, move from room (1, 0) to room (1, 1) in one second.
At time t == 2, move from room (1, 1) to room (1, 2) in one second.
Example 3:

Input: moveTime = [[0,1],[1,2]]

Output: 3

 

Constraints:

2 <= n == moveTime.length <= 50
2 <= m == moveTime[i].length <= 50
0 <= moveTime[i][j] <= 109
'''
import unittest

from typing import *

from heapq import heappush, heappop

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        row = len(moveTime)
        col = len(moveTime[0])
        dp = [[float('inf') for _ in range(col)] for _ in range(row)]
        q = [(0, 0, 0)]
        while q:
            t, i, j = heappop(q)
            if t >= dp[i][j]:
                continue
            if i == row - 1 and j == col - 1:
                return t
            dp[i][j] = t
            for d_x, d_y in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                x = i + d_x
                y = j + d_y
                if x >= 0 and x < row and y >= 0 and y < col and dp[x][y] == float('inf'):
                    heappush(q, (max(t, moveTime[x][y]) + 1, x, y))
        return -1
    
    
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([[0,0,0],[0,0,0]],),3),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().minTimeToReach(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
