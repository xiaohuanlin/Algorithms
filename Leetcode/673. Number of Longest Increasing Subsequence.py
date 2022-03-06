'''
Given an integer array nums, return the number of longest increasing subsequences.

Notice that the sequence has to be strictly increasing.

 

Example 1:

Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:

Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.

 

Constraints:

1 <= nums.length <= 2000
-106 <= nums[i] <= 106
'''
from typing import *

import unittest


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        max_length = 0
        max_count = 0
        dp = [(1, 1) for _ in range(len(nums))]
        for i in range(len(nums)):
            i_max_length = 1
            i_max_count = 1
            for j in range(0, i):
                if nums[j] >= nums[i]:
                    continue
                j_max_length, j_max_count = dp[j]
                j_max_length += 1
                if j_max_length > i_max_length:
                    i_max_length = j_max_length
                    i_max_count = j_max_count
                elif j_max_length == i_max_length:
                    i_max_count += j_max_count
            dp[i] = (i_max_length, i_max_count)
            if i_max_length > max_length:
                max_length = i_max_length
                max_count = i_max_count
            elif i_max_length == max_length:
                max_count += i_max_count
        return max_count


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([3,2,1,3,2,1],), 3),
            (([1,1,2,2,3,3],), 8),
            (([1,3,5,4,7],), 2),
            (([2,2,2,2,2],), 5),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().findNumberOfLIS(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
