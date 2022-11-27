'''
You are given a 0-indexed integer array nums, where nums[i] is a digit between 0 and 9 (inclusive).

The triangular sum of nums is the value of the only element present in nums after the following process terminates:

Let nums comprise of n elements. If n == 1, end the process. Otherwise, create a new 0-indexed integer array newNums of length n - 1.
For each index i, where 0 <= i < n - 1, assign the value of newNums[i] as (nums[i] + nums[i+1]) % 10, where % denotes modulo operator.
Replace the array nums with newNums.
Repeat the entire process starting from step 1.
Return the triangular sum of nums.

 

Example 1:


Input: nums = [1,2,3,4,5]
Output: 8
Explanation:
The above diagram depicts the process from which we obtain the triangular sum of the array.
Example 2:

Input: nums = [5]
Output: 5
Explanation:
Since there is only one element in nums, the triangular sum is the value of that element itself.
 

Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 9
'''
from typing import *

import unittest

from math import comb

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            res = (res + comb(len(nums) - 1, i) * nums[i]) % 10
        return res

        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,2,3,4,5],),8)
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().canChoose(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()


