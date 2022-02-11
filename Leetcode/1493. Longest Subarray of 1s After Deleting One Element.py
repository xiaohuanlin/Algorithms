'''
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
'''
from typing import *
from collections import deque

import unittest
from collections import defaultdict


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        next_zero = [len(nums) for _ in range(len(nums))]
        prev_zero = [0 for _ in range(len(nums))]

        # next
        zero_index = len(nums)
        for i in range(len(nums) - 1, -1, -1):
            next_zero[i] = zero_index
            if nums[i] == 0:
                zero_index = i
        
        # prev
        zero_index = -1
        for i in range(len(nums)):
            prev_zero[i] = zero_index
            if nums[i] == 0:
                zero_index = i
        
        res = 0
        for i in range(len(nums)):
            res = max(res, i - prev_zero[i] - 1 + next_zero[i] - i - 1)
        return res

    
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,1,0,1], ), 3),
            (([0,1,1,1,0,1,1,0,1], ), 5),
            (([1,1,1], ), 2),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().longestSubarray(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

