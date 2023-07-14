'''
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
 

Constraints:

1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6
'''
from typing import *

import unittest


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            res[i] = nums[i] + res[i-1]
        return res

        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([3,1,2,10,1],),[3,4,6,16,17]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().runningSum(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
