'''
You are given an array points where points[i] = [xi, yi] represents the coordinates of a point on an infinite plane.

Your task is to find the maximum area of a rectangle that:

Can be formed using four of these points as its corners.
Does not contain any other point inside or on its border.
Has its edges parallel to the axes.
Return the maximum area that you can obtain or -1 if no such rectangle is possible.



Example 1:

Input: points = [[1,1],[1,3],[3,1],[3,3]]

Output: 4

Explanation:

Example 1 diagram

We can make a rectangle with these 4 points as corners and there is no other point that lies inside or on the border. Hence, the maximum possible area would be 4.

Example 2:

Input: points = [[1,1],[1,3],[3,1],[3,3],[2,2]]

Output: -1

Explanation:

Example 2 diagram

There is only one rectangle possible is with points [1,1], [1,3], [3,1] and [3,3] but [2,2] will always lie inside it. Hence, returning -1.

Example 3:

Input: points = [[1,1],[1,3],[3,1],[3,3],[1,2],[3,2]]

Output: 2

Explanation:

Example 3 diagram

The maximum area rectangle is formed by the points [1,3], [1,2], [3,2], [3,3], which has an area of 2. Additionally, the points [1,1], [1,2], [3,1], [3,2] also form a valid rectangle with the same area.



Constraints:

1 <= points.length <= 10
points[i].length == 2
0 <= xi, yi <= 100
All the given points are unique.
'''
import unittest

from typing import *

from collections import defaultdict


class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int:
        maps = defaultdict(set)
        for p in points:
            maps[p[0]].add(p[1])

        res = -1
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                if x1 == x2 or y1 == y2:
                    continue
                if y2 in maps[x1] and y1 in maps[x2]:
                    for z in range(len(points)):
                        x3, y3 = points[z]
                        if z == i or z == j or ((x3==x1) and (y3==y2)) or ((x3==x2) and (y3==y1)):
                            continue
                        if (x1-x3) * (x2-x3) <= 0 and (y1-y3) * (y2-y3) <= 0:
                            break
                    else:
                        res = max(res, abs(x1-x2) * abs(y1-y2))
        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([[1,1],[1,3],[3,1],[3,3],[1,2],[3,2]],),2),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maxRectangleArea(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

