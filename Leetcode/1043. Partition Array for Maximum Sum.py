'''
Given an integer array arr, partition the array into (contiguous) subarrays of length at most k. After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a 32-bit integer.

 

Example 1:

Input: arr = [1,15,7,9,2,5,10], k = 3
Output: 84
Explanation: arr becomes [15,15,15,9,10,10,10]
Example 2:

Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
Output: 83
Example 3:

Input: arr = [1], k = 1
Output: 1
 

Constraints:

1 <= arr.length <= 500
0 <= arr[i] <= 109
1 <= k <= arr.length
'''
import unittest

from typing import *

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0 for _ in range(len(arr) + 1)]
        for i in range(1, len(arr) + 1):
            max_v = 0
            for j in range(1, k + 1):
                if i - j < 0:
                    continue
                max_v = max(max_v, arr[i-j])
                dp[i] = max(dp[i], dp[i-j] + max_v * j)
        return dp[-1]


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,15,7,9,2,5,10], 3), 84),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maxSumAfterPartitioning(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()