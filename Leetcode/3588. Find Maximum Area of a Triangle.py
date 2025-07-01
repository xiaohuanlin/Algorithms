'''
You are given a 2D array coords of size n x 2, representing the coordinates of n points in an infinite Cartesian plane.

Find twice the maximum area of a triangle with its corners at any three elements from coords, such that at least one side of this triangle is parallel to the x-axis or y-axis. Formally, if the maximum area of such a triangle is A, return 2 * A.

If no such triangle exists, return -1.

Note that a triangle cannot have zero area.

 

Example 1:

Input: coords = [[1,1],[1,2],[3,2],[3,3]]

Output: 2

Explanation:



The triangle shown in the image has a base 1 and height 2. Hence its area is 1/2 * base * height = 1.

Example 2:

Input: coords = [[1,1],[2,2],[3,3]]

Output: -1

Explanation:

The only possible triangle has corners (1, 1), (2, 2), and (3, 3). None of its sides are parallel to the x-axis or the y-axis.

 

Constraints:

1 <= n == coords.length <= 105
1 <= coords[i][0], coords[i][1] <= 106
All coords[i] are unique.
'''
import unittest
from typing import *


class Solution:
    def maxArea(self, coords: List[List[int]]) -> int:
        x = []
        y = []
        for i in range(len(coords)):
            x.append((coords[i][0], coords[i][1]))
            y.append((coords[i][1], coords[i][0]))
        x.sort()
        y.sort()
        res = -1
        for i in range(len(x)):
            j = i
            while j < len(x) and x[i][0] == x[j][0]:
                j += 1
            if j == i + 1:
                continue
            h = max(x[-1][0] - x[i][0], x[i][0] - x[0][0])
            if h == 0:
                continue
            res = max(res, abs(x[i][1] - x[j-1][1]) * h)

        for i in range(len(y)):
            j = i
            while j < len(y) and y[i][0] == y[j][0]:
                j += 1
            if j == i + 1:
                continue
            h = max(y[-1][0] - y[i][0], y[i][0] - y[0][0])
            if h == 0:
                continue
            res = max(res, abs(y[i][1] - y[j-1][1]) * h)
        return res
        
        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([[1,1],[1,2],[3,2],[3,3]],), 2),
            (([[1,1],[2,2],[3,3]],), -1),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maxArea(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
