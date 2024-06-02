'''
You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that has the largest sum.

Return any such subsequence as an integer array of length k.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: nums = [2,1,3,3], k = 2
Output: [3,3]
Explanation:
The subsequence has the largest sum of 3 + 3 = 6.
Example 2:

Input: nums = [-1,-2,3,4], k = 3
Output: [-1,3,4]
Explanation: 
The subsequence has the largest sum of -1 + 3 + 4 = 6.
Example 3:

Input: nums = [3,4,3,3], k = 2
Output: [3,4]
Explanation:
The subsequence has the largest sum of 3 + 4 = 7. 
Another possible subsequence is [4, 3].
 

Constraints:

1 <= nums.length <= 1000
-105 <= nums[i] <= 105
1 <= k <= nums.length
'''
from typing import *
import unittest


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        l = sorted([(nums[i], i) for i in range(len(nums))], reverse=True)[:k]
        n_l = sorted([(v, k) for k, v in l])
        return [n for _, n in n_l]


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([2,1,3,3], 2), [3,3]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maxSubsequence(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()