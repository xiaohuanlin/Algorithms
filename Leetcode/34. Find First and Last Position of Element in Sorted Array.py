"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""

import unittest
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return self.helper(nums, target, 0, len(nums) - 1) if nums else [-1, -1]

    def helper(self, nums: List[int], target: int, start: int, end: int) -> List[int]:
        if start < end:
            middle = (start + end) // 2
            left_data = self.helper(nums, target, start, middle)
            right_data = self.helper(nums, target, middle + 1, end)

            if left_data != [-1, -1] and right_data != [-1, -1] or (
                    left_data == [-1, -1] and right_data == [-1, -1]
            ):
                # That means for cases:
                # 1. [-1, -1] [-1, -1] => [-1, -1]
                # 2. [a, b] [c, d] => [a, d]
                left, right = left_data[0], right_data[1]
            else:
                # That means for cases:
                # 1. [-1, -1] [c, d] => [c, d]
                # 2. [a, b] [-1, -1] => [a, b]
                left, right = left_data if right_data == [-1, -1] else right_data

        else:
            # in this case, only one value
            left, right = (-1, -1) if nums[start] != target else (start, end)

        return [left, right]


class TestSolution(unittest.TestCase):

    def test_searchRange(self):
        examples = (
            (([5, 7, 7, 8, 8, 10], 8), [3, 4]),
            (([5, 7, 7, 8, 8, 10], 6), [-1, -1]),
            (([], 0), [-1, -1])
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().searchRange(*first), second)


unittest.main()
