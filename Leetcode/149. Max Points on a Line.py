'''
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

 

Example 1:


Input: points = [[1,1],[2,2],[3,3]]
Output: 3
Example 2:


Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
 

Constraints:

1 <= points.length <= 300
points[i].length == 2
-104 <= xi, yi <= 104
All the points are unique.
'''
import unittest

from typing import *
from collections import defaultdict


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        maps = defaultdict(set)
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if x1-x2 == 0:
                    maps[(float('inf'), x1)].add((x1,y1))
                    maps[(float('inf'), x1)].add((x2,y2))
                else:
                    slope = (y1-y2)/(x1-x2)
                    intercept = y1 - slope * x1
                    maps[(slope, intercept)].add((x1,y1))
                    maps[(slope, intercept)].add((x2,y2))
        if not maps:
            return len(points)
        return max(len(v) for v in maps.values())


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([[1, 1], [2, 2], [3, 3]],), 3),
            (([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]],), 4),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maxPoints(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

