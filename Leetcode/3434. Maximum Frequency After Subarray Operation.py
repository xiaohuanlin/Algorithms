'''
You are given an array nums of length n. You are also given an integer k.

You perform the following operation on nums once:

Select a 
subarray
 nums[i..j] where 0 <= i <= j <= n - 1.
Select an integer x and add x to all the elements in nums[i..j].
Find the maximum frequency of the value k after the operation.

 

Example 1:

Input: nums = [1,2,3,4,5,6], k = 1

Output: 2

Explanation:

After adding -5 to nums[2..5], 1 has a frequency of 2 in [1, 2, -2, -1, 0, 1].

Example 2:

Input: nums = [10,2,3,4,5,5,4,3,2,2], k = 10

Output: 4

Explanation:

After adding 8 to nums[1..9], 10 has a frequency of 4 in [10, 10, 11, 12, 13, 13, 12, 11, 10, 10].

 

Constraints:

1 <= n == nums.length <= 105
1 <= nums[i] <= 50
1 <= k <= 50
'''
from typing import *

import unittest


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int: 
        res = 0
        for t in range(1, 51):
            if t == k:
                continue
            prev = 0
            for i in range(len(nums)):
                if nums[i] == t:
                    value = 1
                elif nums[i] == k:
                    value = -1
                else:
                    value = 0
                prev = max(prev + value, value)
                res = max(res, prev)
        return res + Counter(nums)[k]


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,2,3,4,5,6], 1), 2),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maxFrequency(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
