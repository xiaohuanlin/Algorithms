'''
You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:

The length of the subarray is k, and
All the elements of the subarray are distinct.
Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.

A subarray is a contiguous non-empty sequence of elements within an array.



Example 1:

Input: nums = [1,5,4,2,9,9,9], k = 3
Output: 15
Explanation: The subarrays of nums with length 3 are:
- [1,5,4] which meets the requirements and has a sum of 10.
- [5,4,2] which meets the requirements and has a sum of 11.
- [4,2,9] which meets the requirements and has a sum of 15.
- [2,9,9] which does not meet the requirements because the element 9 is repeated.
- [9,9,9] which does not meet the requirements because the element 9 is repeated.
We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions
Example 2:

Input: nums = [4,4,4], k = 3
Output: 0
Explanation: The subarrays of nums with length 3 are:
- [4,4,4] which does not meet the requirements because the element 4 is repeated.
We return 0 because no subarrays meet the conditions.


Constraints:

1 <= k <= nums.length <= 105
1 <= nums[i] <= 105
'''
import unittest

from typing import *
from collections import defaultdict
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        windows = set()
        maps = defaultdict(int)
        left = 0
        total = 0
        res = 0
        for i in range(len(nums)):
            windows.add(nums[i])
            maps[nums[i]] += 1
            total += nums[i]

            if i - left >= k:
                total -= nums[left]
                maps[nums[left]] -= 1
                if maps[nums[left]] == 0:
                    windows.remove(nums[left])

                left += 1

            if i - left == k - 1 and k == len(windows):
                res = max(res, total)
        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,5,4,2,9,9,9],3),15),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maximumSubarraySum(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
