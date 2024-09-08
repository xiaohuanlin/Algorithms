'''
You are given an integer array nums of length n.

Your goal is to start at index 0 and reach index n - 1. You can only jump to indices greater than your current index.

The score for a jump from index i to index j is calculated as (j - i) * nums[i].

Return the maximum possible total score by the time you reach the last index.

 

Example 1:

Input: nums = [1,3,1,5]

Output: 7

Explanation:

First, jump to index 1 and then jump to the last index. The final score is 1 * 1 + 2 * 3 = 7.

Example 2:

Input: nums = [4,3,1,3,2]

Output: 16

Explanation:

Jump directly to the last index. The final score is 4 * 4 = 16.

 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105
'''
import unittest

from typing import *


class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        current_max = 0
        res = 0
        for n in nums[:len(nums) - 1]:
            current_max = max(n, current_max)
            res += current_max
        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([4,3,1,3,2],),16),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().findMaximumScore(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
