'''
You are given an array nums consisting of positive integers.

A special subsequence is defined as a subsequence of length 4, represented by indices (p, q, r, s), where p < q < r < s. This subsequence must satisfy the following conditions:

nums[p] * nums[r] == nums[q] * nums[s]
There must be at least one element between each pair of indices. In other words, q - p > 1, r - q > 1 and s - r > 1.
Return the number of different special subsequences in nums.



Example 1:

Input: nums = [1,2,3,4,3,6,1]

Output: 1

Explanation:

There is one special subsequence in nums.

(p, q, r, s) = (0, 2, 4, 6):
This corresponds to elements (1, 3, 3, 1).
nums[p] * nums[r] = nums[0] * nums[4] = 1 * 3 = 3
nums[q] * nums[s] = nums[2] * nums[6] = 3 * 1 = 3
Example 2:

Input: nums = [3,4,3,4,3,4,3,4]

Output: 3

Explanation:

There are three special subsequences in nums.

(p, q, r, s) = (0, 2, 4, 6):
This corresponds to elements (3, 3, 3, 3).
nums[p] * nums[r] = nums[0] * nums[4] = 3 * 3 = 9
nums[q] * nums[s] = nums[2] * nums[6] = 3 * 3 = 9
(p, q, r, s) = (1, 3, 5, 7):
This corresponds to elements (4, 4, 4, 4).
nums[p] * nums[r] = nums[1] * nums[5] = 4 * 4 = 16
nums[q] * nums[s] = nums[3] * nums[7] = 4 * 4 = 16
(p, q, r, s) = (0, 2, 5, 7):
This corresponds to elements (3, 3, 4, 4).
nums[p] * nums[r] = nums[0] * nums[5] = 3 * 4 = 12
nums[q] * nums[s] = nums[2] * nums[7] = 3 * 4 = 12


Constraints:

7 <= nums.length <= 1000
1 <= nums[i] <= 1000
'''
import unittest

from typing import *
from collections import defaultdict
from bisect import bisect_left


class Solution:
    def numberOfSubsequences(self, nums: List[int]) -> int:
        left = defaultdict(list)
        right = defaultdict(list)
        for i in range(len(nums)):
            for j in range(i+2,len(nums)):
                left[nums[i]/nums[j]].append(j)
                right[nums[j]/nums[i]].append(i)

        res = 0
        for k, v in left.items():
            v.sort()
            for a in right[k]:
                res += bisect_left(v, a-1)
        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([3,4,3,4,3,4,3,4],),3),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().numberOfSubsequences(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

