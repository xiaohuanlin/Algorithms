'''
You are given an integer array nums containing distinct positive integers and an integer target.

Determine if you can partition nums into two non-empty disjoint subsets, with each element belonging to exactly one subset, such that the product of the elements in each subset is equal to target.

Return true if such a partition exists and false otherwise.

A subset of an array is a selection of elements of the array.
 

Example 1:

Input: nums = [3,1,6,8,4], target = 24

Output: true

Explanation: The subsets [3, 8] and [1, 6, 4] each have a product of 24. Hence, the output is true.

Example 2:

Input: nums = [2,5,3,7], target = 15

Output: false

Explanation: There is no way to partition nums into two non-empty disjoint subsets such that both subsets have a product of 15. Hence, the output is false.

 

Constraints:

3 <= nums.length <= 12
1 <= target <= 1015
1 <= nums[i] <= 100
All elements of nums are distinct.
'''
import unittest

from typing import *


class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        def dfs(i, selected, value):
            if i >= len(nums):
                return False
            if value == target:
                res = 1
                for j in range(len(nums)):
                    if j in selected:
                        continue
                    res *= nums[j]
                return res == target
            if dfs(i+1, selected, value):
                return True
            selected.append(i)
            if dfs(i+1, selected, value * nums[i]):
                return True
            selected.pop()
            return False
        
        return dfs(0, [], 1)

        
        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([3,1,6,8,4], 24), True),
            (([2,5,3,7], 15), False),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().checkEqualPartitions(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
