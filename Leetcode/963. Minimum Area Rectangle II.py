'''
You are given an array of points in the X-Y plane points where points[i] = [xi, yi].

Return the minimum area of any rectangle formed from these points, with sides not necessarily parallel to the X and Y axes. If there is not any such rectangle, return 0.

Answers within 10-5 of the actual answer will be accepted.

 

Example 1:


Input: points = [[1,2],[2,1],[1,0],[0,1]]
Output: 2.00000
Explanation: The minimum area rectangle occurs at [1,2],[2,1],[1,0],[0,1], with an area of 2.
Example 2:


Input: points = [[0,1],[2,1],[1,1],[1,0],[2,0]]
Output: 1.00000
Explanation: The minimum area rectangle occurs at [1,0],[1,1],[2,1],[2,0], with an area of 1.
Example 3:


Input: points = [[0,3],[1,2],[3,1],[1,3],[2,1]]
Output: 0
Explanation: There is no possible rectangle to form from these points.
 

Constraints:

1 <= points.length <= 50
points[i].length == 2
0 <= xi, yi <= 4 * 104
All the given points are unique.
'''
import unittest

from typing import *


from math import sqrt

class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        n = len(points)
        sets = set((x, y) for x, y in points)
        res = float('inf')
        for i in range(n):
            xi, yi = points[i]
            for j in range(i+1, n):
                xj, yj = points[j]
                for k in range(j+1, n):
                    xk, yk = points[k]
                    doti = (xi - xj) * (xi - xk) + (yi - yj) * (yi - yk)
                    dotj = (xj - xi) * (xj - xk) + (yj - yi) * (yj - yk)
                    dotk = (xk - xj) * (xk - xi) + (yk - yj) * (yk - yi)
                    if doti == 0 and ((xj + xk - xi), (yj + yk - yi)) in sets:
                        area = sqrt(
                            ((xi - xj) ** 2 + (yi - yj) ** 2) *
                            ((xi - xk) ** 2 + (yi - yk) ** 2)
                        )
                        res = min(res, area)
                    elif dotj == 0 and ((xi + xk - xj), (yi + yk - yj)) in sets:
                        area = sqrt(
                            ((xj - xi) ** 2 + (yj - yi) ** 2) *
                            ((xj - xk) ** 2 + (yj - yk) ** 2)
                        )
                        res = min(res, area)
                    elif dotk == 0 and ((xj + xi - xk), (yj + yi - yk)) in sets:
                        area = sqrt(
                            ((xk - xj) ** 2 + (yk - yj) ** 2) *
                            ((xk - xi) ** 2 + (yk - yi) ** 2)
                        )
                        res = min(res, area)
        return res if res != float('inf') else 0

                    

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([[0,1],[2,1],[1,1],[1,0],[2,0]],),1),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().minAreaFreeRect(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
