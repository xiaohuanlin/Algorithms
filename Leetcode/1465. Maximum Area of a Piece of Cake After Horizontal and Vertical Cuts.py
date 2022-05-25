'''
You are given a rectangular cake of size h x w and two arrays of integers horizontalCuts and verticalCuts where:

horizontalCuts[i] is the distance from the top of the rectangular cake to the ith horizontal cut and similarly, and
verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.
Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays horizontalCuts and verticalCuts. Since the answer can be a large number, return this modulo 109 + 7.

 

Example 1:


Input: h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
Output: 4 
Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green piece of cake has the maximum area.
Example 2:


Input: h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]
Output: 6
Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green and yellow pieces of cake have the maximum area.
Example 3:

Input: h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]
Output: 9
 

Constraints:

2 <= h, w <= 109
1 <= horizontalCuts.length <= min(h - 1, 105)
1 <= verticalCuts.length <= min(w - 1, 105)
1 <= horizontalCuts[i] < h
1 <= verticalCuts[i] < w
All the elements in horizontalCuts are distinct.
All the elements in verticalCuts are distinct.
'''
import unittest

from typing import *

from bisect import bisect, bisect_left
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        
        prev = 0
        max_h_delta = 0
        
        for i in range(len(horizontalCuts)):
            max_h_delta = max(max_h_delta, horizontalCuts[i] - prev)
            prev = horizontalCuts[i]
        max_h_delta = max(max_h_delta, h - prev)
        
        prev = 0
        max_w_delta = 0
        
        for i in range(len(verticalCuts)):
            max_w_delta = max(max_w_delta, verticalCuts[i] - prev)
            prev = verticalCuts[i]
        max_w_delta = max(max_w_delta, w - prev)
        return (max_h_delta * max_w_delta) % int(1e9 + 7)


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((5, 4, [3,1], [1]), 6),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maxArea(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
