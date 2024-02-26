'''
There exist n rectangles in a 2D plane. You are given two 0-indexed 2D integer arrays bottomLeft and topRight, both of size n x 2, where bottomLeft[i] and topRight[i] represent the bottom-left and top-right coordinates of the ith rectangle respectively.

You can select a region formed from the intersection of two of the given rectangles. You need to find the largest area of a square that can fit inside this region if you select the region optimally.

Return the largest possible area of a square, or 0 if there do not exist any intersecting regions between the rectangles.



Example 1:


Input: bottomLeft = [[1,1],[2,2],[3,1]], topRight = [[3,3],[4,4],[6,6]]
Output: 1
Explanation: A square with side length 1 can fit inside either the intersecting region of rectangle 0 and rectangle 1, or the intersecting region of rectangle 1 and rectangle 2. Hence the largest area is side * side which is 1 * 1 == 1.
It can be shown that a square with a greater side length can not fit inside any intersecting region.
Example 2:


Input: bottomLeft = [[1,1],[2,2],[1,2]], topRight = [[3,3],[4,4],[3,4]]
Output: 1
Explanation: A square with side length 1 can fit inside either the intersecting region of rectangle 0 and rectangle 1, the intersecting region of rectangle 1 and rectangle 2, or the intersection region of all 3 rectangles. Hence the largest area is side * side which is 1 * 1 == 1.
It can be shown that a square with a greater side length can not fit inside any intersecting region.
Note that the region can be formed by the intersection of more than 2 rectangles.
Example 3:


Input: bottomLeft = [[1,1],[3,3],[3,1]], topRight = [[2,2],[4,4],[4,2]]
Output: 0
Explanation: No pair of rectangles intersect, hence, we return 0.
'''
import unittest

from typing import *


class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        res = 0
        for i in range(len(bottomLeft)):
            for j in range(len(bottomLeft)):
                if i == j:
                    continue
                x0, y0 = bottomLeft[i]
                x1, y1 = topRight[i]
                x2, y2 = bottomLeft[j]
                x3, y3 = topRight[j]
                if x1 > x2 and y1 > y2 and x0 < x3 and y0 < y3:
                    # calculate the area
                    l = min(x1 - x2, y1 - y2, x3 - x0, y3 - y0, x1 - x0, y1 - y0, x3 - x2, y3 - y2)
                    res = max(res, l ** 2)
        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([[1,1],[2,2],[3,1]],[[3,3],[4,4],[6,6]],), 1),
            # (([[1,1],[3,3],[3,1]],[[2,2],[4,4],[4,2]],), 0),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().largestSquareArea(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
