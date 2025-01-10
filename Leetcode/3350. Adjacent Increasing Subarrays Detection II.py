'''
Given an array nums of n integers, your task is to find the maximum value of k for which there exist two adjacent 
subarrays
 of length k each, such that both subarrays are strictly increasing. Specifically, check if there are two subarrays of length k starting at indices a and b (a < b), where:

Both subarrays nums[a..a + k - 1] and nums[b..b + k - 1] are strictly increasing.
The subarrays must be adjacent, meaning b = a + k.
Return the maximum possible value of k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [2,5,7,8,9,2,3,4,3,1]

Output: 3

Explanation:

The subarray starting at index 2 is [7, 8, 9], which is strictly increasing.
The subarray starting at index 5 is [2, 3, 4], which is also strictly increasing.
These two subarrays are adjacent, and 3 is the maximum possible value of k for which two such adjacent strictly increasing subarrays exist.
Example 2:

Input: nums = [1,2,3,4,4,4,4,5,6,7]

Output: 2

Explanation:

The subarray starting at index 0 is [1, 2], which is strictly increasing.
The subarray starting at index 2 is [3, 4], which is also strictly increasing.
These two subarrays are adjacent, and 2 is the maximum possible value of k for which two such adjacent strictly increasing subarrays exist.
 

Constraints:

2 <= nums.length <= 2 * 105
-109 <= nums[i] <= 109
'''
import unittest

from typing import *


class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        prev = None
        start = None
        end = None
        res = 1
        for i in range(len(nums) - 1):
            if nums[i] < nums[i+1]:
                if start is None:
                    start = i
            else:
                if start is not None:
                    # end of the array
                    end = i
                    if prev and prev[1] == start - 1:
                        res = max(res, min(prev[1] - prev[0] + 1, end - start + 1))
                    res = max(res, (end - start + 1) // 2)
                    prev = [start, end]
                    start = None
                    end = None
        else:
            if start is not None:
                # end of the array
                end = i + 1
                if prev and prev[1] == start - 1:
                    res = max(res, min(prev[1] - prev[0] + 1, end - start + 1))
                res = max(res, (end - start + 1) // 2)
        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,2,3,4,4,4,4,5,6,7],),2),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maxIncreasingSubarrays(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
