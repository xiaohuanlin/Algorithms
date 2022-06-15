'''
Given an array nums and an integer target, return the maximum number of non-empty non-overlapping subarrays such that the sum of values in each subarray is equal to target.

 

Example 1:

Input: nums = [1,1,1,1,1], target = 2
Output: 2
Explanation: There are 2 non-overlapping subarrays [1,1,1,1,1] with sum equals to target(2).
Example 2:

Input: nums = [-1,3,5,1,4,2,-9], target = 6
Output: 2
Explanation: There are 3 subarrays with sum equal to 6.
([5,1], [4,2], [3,5,1,4,2,-9]) but only the first 2 are non-overlapping.
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
0 <= target <= 106
'''
import unittest

from typing import *

class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        store = set()
        res = 0
        total = 0
        
        for num in nums:
            if total in store:
                res += 1
                store = set()
            store.add(target + total)
            total += num
            
        if total in store:
            res += 1
        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,1,1,1,1], 2), 2),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maxNonOverlapping(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
