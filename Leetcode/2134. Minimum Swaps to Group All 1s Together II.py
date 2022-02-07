'''
A swap is defined as taking two distinct positions in an array and swapping the values in them.

A circular array is defined as an array where we consider the first element and the last element to be adjacent.

Given a binary circular array nums, return the minimum number of swaps required to group all 1's present in the array together at any location.

 

Example 1:

Input: nums = [0,1,0,1,1,0,0]
Output: 1
Explanation: Here are a few of the ways to group all the 1's together:
[0,0,1,1,1,0,0] using 1 swap.
[0,1,1,1,0,0,0] using 1 swap.
[1,1,0,0,0,0,1] using 2 swaps (using the circular property of the array).
There is no way to group all 1's together with 0 swaps.
Thus, the minimum number of swaps required is 1.
Example 2:

Input: nums = [0,1,1,1,0,0,1,1,0]
Output: 2
Explanation: Here are a few of the ways to group all the 1's together:
[1,1,1,0,0,0,0,1,1] using 2 swaps (using the circular property of the array).
[1,1,1,1,1,0,0,0,0] using 2 swaps.
There is no way to group all 1's together with 0 or 1 swaps.
Thus, the minimum number of swaps required is 2.
Example 3:

Input: nums = [1,1,0,0,1]
Output: 0
Explanation: All the 1's are already grouped together due to the circular property of the array.
Thus, the minimum number of swaps required is 0.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
'''
from typing import *
from math import gcd

import unittest


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        pre_sum = [0 for _ in range(len(nums) + 1)]
        count = 0
        for i in range(1, len(nums) + 1): 
            pre_sum[i] = pre_sum[i - 1] + nums[i - 1]
            if nums[i - 1] == 1:
                count += 1
        
        max_v = 0
        for i in range(len(nums) - count):
            max_v = max(pre_sum[i + count] - pre_sum[i], max_v)
        
        for i in range(count):
            # pre for [0:i]
            left = pre_sum[i]
            # next for [len(nums) - (count-i):]
            right = pre_sum[-1] - pre_sum[-1 -(count - i)]
            max_v = max(left + right, max_v)
        return count - max_v


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ([0,1,0,1,1,0,0], 1),
            ([0,1,1,1,0,0,1,1,0], 2),
            ([1,1,0,0,1], 0),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().minSwaps(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
