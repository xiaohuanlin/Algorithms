'''
You are given two integers m and n representing a 0-indexed m x n grid. You are also given two 2D integer arrays guards and walls where guards[i] = [rowi, coli] and walls[j] = [rowj, colj] represent the positions of the ith guard and jth wall respectively.

A guard can see every cell in the four cardinal directions (north, east, south, or west) starting from their position unless obstructed by a wall or another guard. A cell is guarded if there is at least one guard that can see it.

Return the number of unoccupied cells that are not guarded.

 

Example 1:


Input: m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]
Output: 7
Explanation: The guarded and unguarded cells are shown in red and green respectively in the above diagram.
There are a total of 7 unguarded cells, so we return 7.
Example 2:


Input: m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]]
Output: 4
Explanation: The unguarded cells are shown in green in the above diagram.
There are a total of 4 unguarded cells, so we return 4.
 

Constraints:

1 <= m, n <= 105
2 <= m * n <= 105
1 <= guards.length, walls.length <= 5 * 104
2 <= guards.length + walls.length <= m * n
guards[i].length == walls[j].length == 2
0 <= rowi, rowj < m
0 <= coli, colj < n
All the positions in guards and walls are unique.
'''

from typing import *

import unittest

from bisect import bisect

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        rows = {}
        cols = {}
        for wall in walls:
            rows.setdefault(wall[0], []).append((wall[1], 0))
            cols.setdefault(wall[1], []).append((wall[0], 0))
            
        for guard in guards:
            rows.setdefault(guard[0], []).append((guard[1], 1))
            cols.setdefault(guard[1], []).append((guard[0], 1))
            
        for _, row in rows.items():
            row.sort()
            
        for _, col in cols.items():
            col.sort()
    
        res = 0
        for i in range(m):
            for j in range(n):
                right = bisect(rows.get(i, []), (j, 0))
                right_guard = right < len(rows.get(i, [])) and (rows[i][right][1] == 1 or rows[i][right][0] == j)
                left = right - 1
                left_guard = left >= 0 and (rows[i][left][1] == 1 or rows[i][left][0] == j)
                
                down = bisect(cols.get(j, []), (i, 0))
                down_guard = down < len(cols.get(j, [])) and (cols[j][down][1] == 1 or cols[j][down][0] == i)
                up = down - 1
                up_guard = up >= 0 and (cols[j][up][1] == 1 or cols[j][up][0] == i)

                if not (right_guard or left_guard or down_guard or up_guard):  
                    res += 1
        return res

        
class TestSolution(unittest.TestCase):
    def test_case(self):
        examples = (
            ((4, 6, [[0,0],[1,1],[2,3]], [[0,1],[2,2],[1,4]]), 7),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().countUnguarded(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

