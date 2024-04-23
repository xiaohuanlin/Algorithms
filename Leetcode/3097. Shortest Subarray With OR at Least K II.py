'''
You are given an array nums of non-negative integers and an integer k.

An array is called special if the bitwise OR of all of its elements is at least k.

Return the length of the shortest special non-empty
subarray
 of nums, or return -1 if no special subarray exists.



Example 1:

Input: nums = [1,2,3], k = 2

Output: 1

Explanation:

The subarray [3] has OR value of 3. Hence, we return 1.

Example 2:

Input: nums = [2,1,8], k = 10

Output: 3

Explanation:

The subarray [2,1,8] has OR value of 11. Hence, we return 3.

Example 3:

Input: nums = [1,2], k = 0

Output: 1

Explanation:

The subarray [1] has OR value of 1. Hence, we return 1.



Constraints:

1 <= nums.length <= 2 * 105
0 <= nums[i] <= 109
0 <= k <= 109
'''
import unittest

from typing import *


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        window = [0 for _ in range(32)]

        def to_value():
            value = 0
            for i in range(32)[::-1]:
                value <<= 1
                value += bool(window[i])
            return value

        res = float('inf')
        left = 0
        for right in range(len(nums)):
            # add num
            for i in range(32):
                window[i] += bool(nums[right] & (1 << i))
            while left <= right and to_value() >= k:
                res = min(res, right - left + 1)

                # remove num
                for i in range(32):
                    window[i] -= bool(nums[left] & (1 << i))
                left += 1
        return res if res != float('inf') else -1



class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,12,26,2], 8), 1),
            (([2,1,8], 10), 3),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().minimumSubarrayLength(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
