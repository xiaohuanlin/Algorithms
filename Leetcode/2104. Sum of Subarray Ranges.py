'''
You are given an integer array nums. The range of a subarray of nums is the difference between the largest and smallest element in the subarray.

Return the sum of all subarray ranges of nums.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,2,3]
Output: 4
Explanation: The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0 
[2], range = 2 - 2 = 0
[3], range = 3 - 3 = 0
[1,2], range = 2 - 1 = 1
[2,3], range = 3 - 2 = 1
[1,2,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.
Example 2:

Input: nums = [1,3,3]
Output: 4
Explanation: The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0
[3], range = 3 - 3 = 0
[3], range = 3 - 3 = 0
[1,3], range = 3 - 1 = 2
[3,3], range = 3 - 3 = 0
[1,3,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 2 + 0 + 2 = 4.
Example 3:

Input: nums = [4,-2,-3,4,1]
Output: 59
Explanation: The sum of all subarray ranges of nums is 59.
 

Constraints:

1 <= nums.length <= 1000
-109 <= nums[i] <= 109
 

Follow-up: Could you find a solution with O(n) time complexity?
'''
import unittest
from typing import *

from functools import lru_cache
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        # for max value
        prev_max = [0 for _ in range(len(nums))]
        stack = []
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            prev_max[i] = stack[-1] if stack else -1
            stack.append(i)
        
        next_max = [0 for _ in range(len(nums))]
        stack = []
        for i in range(len(nums))[::-1]:
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            next_max[i] = stack[-1] if stack else len(nums)
            stack.append(i)
        
        sum_max = sum((next_max[i] - i) * (i - prev_max[i]) * nums[i] for i in range(len(nums)))
        
        # for min value
        prev_min = [0 for _ in range(len(nums))]
        stack = []
        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                stack.pop()
            prev_min[i] = stack[-1] if stack else -1
            stack.append(i)
        
        next_min = [0 for _ in range(len(nums))]
        stack = []
        for i in range(len(nums))[::-1]:
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            next_min[i] = stack[-1] if stack else len(nums)
            stack.append(i)
            
        
        sum_min = sum((next_min[i] - i) * (i - prev_min[i]) * nums[i] for i in range(len(nums)))
        return sum_max - sum_min

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([4,-2,-3,4,1],),59),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().subArrayRanges(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()