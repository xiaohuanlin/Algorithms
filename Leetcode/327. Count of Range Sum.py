'''
Given an integer array nums and two integers lower and upper, return the number of range sums that lie in [lower, upper] inclusive.

Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j inclusive, where i <= j.

 

Example 1:

Input: nums = [-2,5,-1], lower = -2, upper = 2
Output: 3
Explanation: The three ranges are: [0,0], [2,2], and [0,2] and their respective sums are: -2, -1, 2.
Example 2:

Input: nums = [0], lower = 0, upper = 0
Output: 1
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
-105 <= lower <= upper <= 105
The answer is guaranteed to fit in a 32-bit integer.
'''
import unittest

from typing import *
import heapq


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        presum = [0]
        for i in range(len(nums)):
            presum.append(presum[-1] + nums[i])

        def mergesort(start, end):
            if start >= end:
                return 0

            middle = (start + end) // 2
            cnt = mergesort(start, middle) + mergesort(middle+1, end)
            i = j = middle+1
            for left in presum[start:middle+1]:
                while i <= end and presum[i] - left < lower:
                    i += 1
                while j <= end and presum[j] - left <= upper:
                    j += 1
                cnt += j - i
            presum[start:end+1] = sorted(presum[start:end+1])
            return cnt
        return mergesort(0, len(nums))


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([-2,5,-1],-2,2),3),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().countRangeSum(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

