'''
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,4,4,5,6,7] might become:

[4,5,6,7,0,1,4] if it was rotated 4 times.
[0,1,4,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.

You must decrease the overall operation steps as much as possible.

 

Example 1:

Input: nums = [1,3,5]
Output: 1
Example 2:

Input: nums = [2,2,2,0,1]
Output: 0
 

Constraints:

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
nums is sorted and rotated between 1 and n times.
 

Follow up: This problem is similar to Find Minimum in Rotated Sorted Array, but nums may contain duplicates. Would this affect the runtime complexity? How and why?
'''
import unittest
from typing import *


class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        min_v = float('+inf')
        while start < end:
            middle = start + (end - start) // 2
            if nums[start] == nums[end]:
                if nums[middle] == nums[start]:
                    # all same, search all nums
                    for i in range(start, end):
                        min_v = min(min_v, nums[i])
                    break
                elif nums[middle] > nums[start]:
                    start = middle + 1
                else:
                    end = middle
            elif nums[start] > nums[end]:
                if nums[middle] >= nums[start]:
                    start = middle + 1
                else:
                    end = middle
            else:
                break
        return min(min_v, nums[start])


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,3,5], ), 1),
            (([2,2,2,0,1], ), 0),
            (([1,2,2,2,0,1,1], ), 0)
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().findMin(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
