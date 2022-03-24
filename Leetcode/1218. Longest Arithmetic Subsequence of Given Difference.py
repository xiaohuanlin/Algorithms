'''
Given an integer array arr and an integer difference, return the length of the longest subsequence in arr which is an arithmetic sequence such that the difference between adjacent elements in the subsequence equals difference.

A subsequence is a sequence that can be derived from arr by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: arr = [1,2,3,4], difference = 1
Output: 4
Explanation: The longest arithmetic subsequence is [1,2,3,4].
Example 2:

Input: arr = [1,3,5,7], difference = 1
Output: 1
Explanation: The longest arithmetic subsequence is any single element.
Example 3:

Input: arr = [1,5,7,8,5,3,4,2,1], difference = -2
Output: 4
Explanation: The longest arithmetic subsequence is [7,5,3,1].
 

Constraints:

1 <= arr.length <= 105
-104 <= arr[i], difference <= 104
'''
import unittest
from typing import *

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        max_v = 0
        for i in range(len(arr)):
            current_v = arr[i]
            dp[current_v] = max(dp.setdefault(current_v, 0), dp.setdefault(current_v - difference, 0) + 1)
            max_v = max(max_v, dp[current_v])
        return max_v


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,2,3,4], 1), 4),
            (([1,3,5,7], 1), 1),
            (([1,5,7,8,5,3,4,2,1], -2), 4),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().longestSubsequence(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
