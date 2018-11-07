'''

You have a list of points in the plane. Return the area of the largest triangle that can be formed by any 3 of the points.

Example:
Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2
Explanation:
The five points are show in the figure below. The red triangle is the largest.


Notes:

3 <= points.length <= 50.
No points will be duplicated.
 -50 <= points[i][j] <= 50.
Answers within 10^-6 of the true value will be accepted as correct.

'''
import unittest


class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        largest = 0
        from itertools import combinations
        points_com = combinations(points, 3)
        for p1, p2, p3 in points_com:
            area = self.get_area(p1, p2, p3)
            # print(area)
            if area > largest:
                largest = area
        return largest

    def get_area(self, p1, p2, p3):
        # print(p1,p2,p3)
        return abs((p2[1] - p1[1]) * p3[0] - p1[0] * (p2[1] - p1[1]) - (p2[0] - p1[0]) * p3[1] + p1[1] * (
                    p2[0] - p1[0])) / 2


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            # ([[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]], 2),
            ([[8,3],[5,6],[3,5]], 4.5),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().largestTriangleArea(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
