'''
You are given an integer n representing the dimensions of an n x n grid, with the origin at the bottom-left corner of the grid. You are also given a 2D array of coordinates rectangles, where rectangles[i] is in the form [startx, starty, endx, endy], representing a rectangle on the grid. Each rectangle is defined as follows:

(startx, starty): The bottom-left corner of the rectangle.
(endx, endy): The top-right corner of the rectangle.
Note that the rectangles do not overlap. Your task is to determine if it is possible to make either two horizontal or two vertical cuts on the grid such that:

Each of the three resulting sections formed by the cuts contains at least one rectangle.
Every rectangle belongs to exactly one section.
Return true if such cuts can be made; otherwise, return false.

 

Example 1:

Input: n = 5, rectangles = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]

Output: true

Explanation:



The grid is shown in the diagram. We can make horizontal cuts at y = 2 and y = 4. Hence, output is true.

Example 2:

Input: n = 4, rectangles = [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]

Output: true

Explanation:



We can make vertical cuts at x = 2 and x = 3. Hence, output is true.

Example 3:

Input: n = 4, rectangles = [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]]

Output: false

Explanation:

We cannot make two horizontal or two vertical cuts that satisfy the conditions. Hence, output is false.

 

Constraints:

3 <= n <= 109
3 <= rectangles.length <= 105
0 <= rectangles[i][0] < rectangles[i][2] <= n
0 <= rectangles[i][1] < rectangles[i][3] <= n
No two rectangles overlap.
'''
import unittest

from typing import *


class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        rows = []
        cols = []
        for sx, sy, ex, ey in rectangles:
            rows.append((sx, ex))
            cols.append((sy, ey))
        rows.sort()
        cols.sort()

        cntx = 0
        prevx = 0
        cnty = 0
        prevy = 0
        for sx, ex in rows:
            if sx >= prevx:
                cntx += 1
                if cntx >= 3:
                    return True
            prevx = max(prevx, ex)
        for sy, ey in cols:
            if sy >= prevy:
                cnty += 1
                if cnty >= 3:
                    return True
            prevy = max(prevy, ey)
        return False


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((5, [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]), True),
            ((4, [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]), True),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().checkValidCuts(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
