'''
You are given an integer array nums.
A subsequence sub of nums with length x is called valid if it satisfies:

(sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x - 2] + sub[x - 1]) % 2.
Return the length of the longest valid subsequence of nums.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: nums = [1,2,3,4]

Output: 4

Explanation:

The longest valid subsequence is [1, 2, 3, 4].

Example 2:

Input: nums = [1,2,1,1,2,1,2]

Output: 6

Explanation:

The longest valid subsequence is [1, 2, 1, 2, 1, 2].

Example 3:

Input: nums = [1,3]

Output: 2

Explanation:

The longest valid subsequence is [1, 3].

 

Constraints:

2 <= nums.length <= 2 * 105
1 <= nums[i] <= 107
'''
import unittest

from typing import *


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        maxzero = 0
        maxone = 0
        zero = 0
        one = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                maxzero = maxone + 1
                zero += 1
            else:
                maxone = maxzero + 1
                one += 1
        return max(maxzero, maxone, zero, one)


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,2,3,4],), 4),
            (([1,2,1,1,2,1,2],), 6),
            (([1,3],), 2),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maximumLength(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

