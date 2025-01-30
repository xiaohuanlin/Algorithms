'''
Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.
Example 2:

Input: nums = [1,2,4,8]
Output: [1,2,4,8]
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 2 * 109
All the integers in nums are unique.
'''
import unittest

from typing import *
from collections import defaultdict


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        maps = defaultdict(list)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] % nums[i] == 0:
                    maps[j].append(i)

        dp = [[nums[i]] for i in range(len(nums))]
        for i in range(len(nums)):
            for j in maps[i]:
                if len(dp[j]) + 1 > len(dp[i]):
                    dp[i] = [k for k in dp[j]]
                    dp[i].append(nums[i])
        
        res = []
        for w in dp:
            if len(w) > len(res):
                res = w
        return res
            

    
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,2,4,8],),[1,2,4,8]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().largestDivisibleSubset(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
