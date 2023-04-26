'''
You are given an integer array nums of size n.

Consider a non-empty subarray from nums that has the maximum possible bitwise AND.

In other words, let k be the maximum value of the bitwise AND of any subarray of nums. Then, only subarrays with a bitwise AND equal to k should be considered.
Return the length of the longest such subarray.

The bitwise AND of an array is the bitwise AND of all the numbers in it.

A subarray is a contiguous sequence of elements within an array.

 

Example 1:

Input: nums = [1,2,3,3,2,2]
Output: 2
Explanation:
The maximum possible bitwise AND of a subarray is 3.
The longest subarray with that value is [3,3], so we return 2.
Example 2:

Input: nums = [1,2,3,4]
Output: 1
Explanation:
The maximum possible bitwise AND of a subarray is 4.
The longest subarray with that value is [4], so we return 1.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 106
'''
from typing import *
import unittest

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = 1
        i = 0
        max_v = 0
        while i < len(nums):
            j = i
            while j < len(nums) and nums[i] == nums[j]:
                j += 1
            
            if nums[i] > max_v:
                max_v = nums[i]
                res = j - i
            elif nums[i] == max_v:
                res = max(res, j - i)

            i = j
        return res
                    

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,2,3,3,2,2],),2),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().longestSubarray(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
