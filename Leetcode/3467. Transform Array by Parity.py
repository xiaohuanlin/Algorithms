'''
You are given an integer array nums. Transform nums by performing the following operations in the exact order specified:

Replace each even number with 0.
Replace each odd numbers with 1.
Sort the modified array in non-decreasing order.
Return the resulting array after performing these operations.

 

Example 1:

Input: nums = [4,3,2,1]

Output: [0,0,1,1]

Explanation:

Replace the even numbers (4 and 2) with 0 and the odd numbers (3 and 1) with 1. Now, nums = [0, 1, 0, 1].
After sorting nums in non-descending order, nums = [0, 0, 1, 1].
Example 2:

Input: nums = [1,5,1,4,2]

Output: [0,0,1,1,1]

Explanation:

Replace the even numbers (4 and 2) with 0 and the odd numbers (1, 5 and 1) with 1. Now, nums = [1, 1, 1, 0, 0].
After sorting nums in non-descending order, nums = [0, 0, 1, 1, 1].
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 1000
'''
import unittest

from typing import *


class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        res = [0 for _ in range(len(nums))]
        i = len(nums)-1
        for n in nums:
            if n % 2 == 1:
                res[i] = 1
                i -= 1
        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([4, 3, 2, 1],), [0, 0, 1, 1]),
            (([1, 5, 1, 4, 2],), [0, 0, 1, 1, 1]),
            (([2, 4],), [0, 0]),
            (([1],), [1]),
            (([],), []),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().transformArray(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

