'''
You are given an integer array nums and an integer k.

Your task is to partition nums into k non-empty subarrays. For each subarray, compute the bitwise XOR of all its elements.

Return the minimum possible value of the maximum XOR among these k subarrays.

 

Example 1:

Input: nums = [1,2,3], k = 2

Output: 1

Explanation:

The optimal partition is [1] and [2, 3].

XOR of the first subarray is 1.
XOR of the second subarray is 2 XOR 3 = 1.
The maximum XOR among the subarrays is 1, which is the minimum possible.

Example 2:

Input: nums = [2,3,3,2], k = 3

Output: 2

Explanation:

The optimal partition is [2], [3, 3], and [2].

XOR of the first subarray is 2.
XOR of the second subarray is 3 XOR 3 = 0.
XOR of the third subarray is 2.
The maximum XOR among the subarrays is 2, which is the minimum possible.

Example 3:

Input: nums = [1,1,2,3,1], k = 2

Output: 0

Explanation:

The optimal partition is [1, 1] and [2, 3, 1].

XOR of the first subarray is 1 XOR 1 = 0.
XOR of the second subarray is 2 XOR 3 XOR 1 = 0.
The maximum XOR among the subarrays is 0, which is the minimum possible.

 

Constraints:

1 <= nums.length <= 250
1 <= nums[i] <= 109
1 <= k <= n
'''
import unittest
from typing import *


class Solution:
    def minXor(self, nums: List[int], k: int) -> int:
        presum = [0]
        for i in range(len(nums)):
            presum.append(presum[-1] ^ nums[i])
        
        dp = [[float('inf') for _ in range(len(nums) + 1)] for _ in range(k)]
        dp[0] = presum[:]
        for i in range(k):
            dp[i][0] = float('inf')

        for i in range(1, k):
            for j in range(1, len(nums)+1):
                for m in range(i-1, j):
                    res = presum[j] ^ presum[m]
                    if res > dp[i][j]: 
                        continue
                    dp[i][j] = min(dp[i][j], max(dp[i-1][m], res))
        return dp[-1][-1]  
        
        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,2,3], 2), 1),
            (([2,3,3,2], 3), 2),
            (([1,1,2,3,1], 2), 0),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().minXor(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
