'''
You start at the cell (rStart, cStart) of an rows x cols grid facing east. The northwest corner is at the first row and column in the grid, and the southeast corner is at the last row and column.

You will walk in a clockwise spiral shape to visit every position in this grid. Whenever you move outside the grid's boundary, we continue our walk outside the grid (but may return to the grid boundary later.). Eventually, we reach all rows * cols spaces of the grid.

Return an array of coordinates representing the positions of the grid in the order you visited them.

 

Example 1:


Input: rows = 1, cols = 4, rStart = 0, cStart = 0
Output: [[0,0],[0,1],[0,2],[0,3]]
Example 2:


Input: rows = 5, cols = 6, rStart = 1, cStart = 4
Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]
 

Constraints:

1 <= rows, cols <= 100
0 <= rStart < rows
0 <= cStart < cols
'''

from typing import *
import unittest


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        res = []
        count = 0
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

        while len(res) < rows * cols:
            unit = count // 2 + 1
            x, y = directions[count % 4]
            for _ in range(unit):
                if rStart >= 0 and rStart < rows and cStart >= 0 and cStart < cols:
                    res.append([rStart, cStart])
                rStart += x
                cStart += y

            count += 1
        return res
        
        

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((1, 4, 0, 0), [[0,0],[0,1],[0,2],[0,3]]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().spiralMatrixIII(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()