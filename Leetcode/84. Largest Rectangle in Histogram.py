'''
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:


Input: heights = [2,4]
Output: 4
 

Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104
'''

from typing import *

import unittest

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        next_less = [0 for _ in range(len(heights))]
        for i in range(len(heights) - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            next_less[i] = len(heights) if not stack else stack[-1]
            stack.append(i)
        
        stack.clear()
        prev_less = [0 for _ in range(len(heights))]
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            prev_less[i] = -1 if not stack else stack[-1]
            stack.append(i)
        
        res = 0
        for i in range(len(heights)):
            res = max(res, (next_less[i] - i - 1 + i - prev_less[i]) * heights[i])
        return res


class TestSolution(unittest.TestCase):
    def test_case(self):
        examples = (
            (([2,1,5,6,2,3], ), 10),
            (([2,4], ), 4),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().largestRectangleArea(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

