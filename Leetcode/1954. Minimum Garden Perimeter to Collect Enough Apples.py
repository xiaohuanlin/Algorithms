'''
In a garden represented as an infinite 2D grid, there is an apple tree planted at every integer coordinate. The apple tree planted at an integer coordinate (i, j) has |i| + |j| apples growing on it.

You will buy an axis-aligned square plot of land that is centered at (0, 0).

Given an integer neededApples, return the minimum perimeter of a plot such that at least neededApples apples are inside or on the perimeter of that plot.

The value of |x| is defined as:

x if x >= 0
-x if x < 0


Example 1:


Input: neededApples = 1
Output: 8
Explanation: A square plot of side length 1 does not contain any apples.
However, a square plot of side length 2 has 12 apples inside (as depicted in the image above).
The perimeter is 2 * 4 = 8.
Example 2:

Input: neededApples = 13
Output: 16
Example 3:

Input: neededApples = 1000000000
Output: 5040


Constraints:

1 <= neededApples <= 1015
'''
import unittest

from typing import *

class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        def is_ok(num, need):
            return 2*num*(num+1)*(2*num+1) >= need

        start = 0
        end = neededApples
        while start < end:
            middle = start + (end - start) // 2
            if is_ok(middle, neededApples):
                end = middle
            else:
                start = middle + 1
        return start * 8


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((13,),16),
            ((100000000000000,),233920),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().minimumPerimeter(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
