'''
You are given an array of integers nums. Return the length of the longest
subarray
 of nums which is either
strictly increasing
 or
strictly decreasing
.



Example 1:

Input: nums = [1,4,3,3,2]

Output: 2

Explanation:

The strictly increasing subarrays of nums are [1], [2], [3], [3], [4], and [1,4].

The strictly decreasing subarrays of nums are [1], [2], [3], [3], [4], [3,2], and [4,3].

Hence, we return 2.

Example 2:

Input: nums = [3,3,3,3]

Output: 1

Explanation:

The strictly increasing subarrays of nums are [3], [3], [3], and [3].

The strictly decreasing subarrays of nums are [3], [3], [3], and [3].

Hence, we return 1.

Example 3:

Input: nums = [3,2,1]

Output: 3

Explanation:

The strictly increasing subarrays of nums are [3], [2], and [1].

The strictly decreasing subarrays of nums are [3], [2], [1], [3,2], [2,1], and [3,2,1].

Hence, we return 3.



Constraints:

1 <= nums.length <= 50
1 <= nums[i] <= 50
'''
import unittest

from typing import *

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        window = []
        minv = float('inf')
        maxv = float('-inf')

        start = 0
        res = 1
        for end in range(len(nums)):
            window.append(nums[end])
            minv = min(nums[end], minv)
            maxv = max(nums[end], maxv)
            while len(window) > 1 and \
                not (
                    (
                        (window[0] == minv and window[-1] == maxv) or
                        (window[0] == maxv and window[-1] == minv)
                    ) and
                    (len(set(window)) == len(window))
                ):
                start += 1
                window.pop(0)
                if window:
                    minv = min(window)
                    maxv = max(window)
                else:
                    minv = float('inf')
                    maxv = float('-inf')
            res = max(res, end - start + 1)
        return res

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,4,3,3,2],),2),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().longestMonotonicSubarray(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
