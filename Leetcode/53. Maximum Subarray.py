'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''

import unittest

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Kadane algo
        # keep focus on the x and max_ending_here
        max_ending_here = nums[0]
        max_so_far = nums[0]

        for x in nums[1:]:
            # remeber that compare max_ending_here with X instead of origin max_ending_here
            # keep fluent
            max_ending_here = max(x, max_ending_here + x)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far


class TestSolution(unittest.TestCase):

    def test_maxSubArray(self):
        examples = (([-2,1,-3,4,-1,2,1,-5,4], 6),
                    ([1, -2, 0], 1),
                    ([1, -2, 5], 5),
        )
        for first,second in examples:
            self.assert_function(first, second)
        
    def assert_function(self, first, second):
        self.assertEqual(Solution().maxSubArray(first), second)

unittest.main()