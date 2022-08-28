'''
312. Burst Balloons
Hard

6705

171

Add to List

Share
You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.

 

Example 1:

Input: nums = [3,1,5,8]
Output: 167
Explanation:
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
Example 2:

Input: nums = [1,5]
Output: 10
 

Constraints:

n == nums.length
1 <= n <= 300
0 <= nums[i] <= 100
'''

from typing import *

import unittest


from functools import lru_cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums.insert(0, 1)
        nums.append(1)
        
        @lru_cache(None)
        def get(i, j):
            max_v = 0
            for k in range(i+1, j):
                max_v = max(max_v, get(i, k) + get(k, j) + nums[k] * nums[i] * nums[j])
            return max_v
        
        return get(0, len(nums) - 1)

        
class TestSolution(unittest.TestCase):
    def test_case(self):
        examples = (
            (([3,1,5,8],), 167),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maxCoins(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

