'''
You are given an integer array nums. Your task is to remove all elements from the array by performing one of the following operations at each step until nums is empty:

Choose any two elements from the first three elements of nums and remove them. The cost of this operation is the maximum of the two elements removed.
If fewer than three elements remain in nums, remove all the remaining elements in a single operation. The cost of this operation is the maximum of the remaining elements.
Return the minimum cost required to remove all the elements.



Example 1:

Input: nums = [6,2,8,4]

Output: 12

Explanation:

Initially, nums = [6, 2, 8, 4].

In the first operation, remove nums[0] = 6 and nums[2] = 8 with a cost of max(6, 8) = 8. Now, nums = [2, 4].
In the second operation, remove the remaining elements with a cost of max(2, 4) = 4.
The cost to remove all elements is 8 + 4 = 12. This is the minimum cost to remove all elements in nums. Hence, the output is 12.

Example 2:

Input: nums = [2,1,3,3]

Output: 5

Explanation:

Initially, nums = [2, 1, 3, 3].

In the first operation, remove nums[0] = 2 and nums[1] = 1 with a cost of max(2, 1) = 2. Now, nums = [3, 3].
In the second operation remove the remaining elements with a cost of max(3, 3) = 3.
The cost to remove all elements is 2 + 3 = 5. This is the minimum cost to remove all elements in nums. Hence, the output is 5.



Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 106
'''
from typing import *

import unittest
from functools import lru_cache


class Solution:
    def minCost(self, nums: List[int]) -> int:

        @lru_cache
        def dfs(keep, start):
            if start > len(nums):
                return 0
            elif start == len(nums):
                return nums[keep]
            elif start == len(nums) - 1:
                return max(nums[keep], nums[start])

            res = float('inf')
            res = min(res, dfs(keep, start+2) + max(nums[start], nums[start+1]))
            res = min(res, dfs(start, start+2) + max(nums[start+1], nums[keep]))
            res = min(res, dfs(start+1, start+2) + max(nums[start], nums[keep]))
            return res

        return dfs(0, 1)


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([3,9,20,11,22],),42),
            (([1,20,7,8,18],),35),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().minCost(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
