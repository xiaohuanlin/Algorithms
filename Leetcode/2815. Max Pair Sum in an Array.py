'''
You are given an integer array nums. You have to find the maximum sum of a pair of numbers from nums such that the largest digit in both numbers is equal.

For example, 2373 is made up of three distinct digits: 2, 3, and 7, where 7 is the largest among them.

Return the maximum sum or -1 if no such pair exists.

 

Example 1:

Input: nums = [112,131,411]

Output: -1

Explanation:

Each numbers largest digit in order is [2,3,4].

Example 2:

Input: nums = [2536,1613,3366,162]

Output: 5902

Explanation:

All the numbers have 6 as their largest digit, so the answer is 2536 + 3366 = 5902.

Example 3:

Input: nums = [51,71,17,24,42]

Output: 88

Explanation:

Each number's largest digit in order is [5,7,7,4,4].

So we have only two possible pairs, 71 + 17 = 88 and 24 + 42 = 66.

 

Constraints:

2 <= nums.length <= 100
1 <= nums[i] <= 104
'''
import unittest

from typing import *

from collections import defaultdict


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        res = defaultdict(list)
        for n in nums:
            k = max(str(n))
            if len(res[k]) <= 1:
                res[k].append(n)
            elif len(res[k]) == 2:
                res[k].append(n)
                res[k] = sorted(res[k], reverse=True)[:-1]
        ans = -1
        for _, v in res.items():
            if len(v) == 2:
                ans = max(ans, sum(v))
        return ans
    
    
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([2536,1613,3366,162],),5902),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maxSum(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
