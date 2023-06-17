'''
Given a 0-indexed integer array nums, find a 0-indexed integer array answer where:

answer.length == nums.length.
answer[i] = |leftSum[i] - rightSum[i]|.
Where:

leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.
Return the array answer.

 

Example 1:

Input: nums = [10,4,8,3]
Output: [15,1,11,22]
Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].
Example 2:

Input: nums = [1]
Output: [0]
Explanation: The array leftSum is [0] and the array rightSum is [0].
The array answer is [|0 - 0|] = [0].
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 105
'''
from typing import *

import unittest
    
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sum = [0 for _ in range(len(nums))]
        for i in range(len(nums)-1):
            left_sum[i+1] = left_sum[i] + nums[i]

        right_sum = [0 for _ in range(len(nums))]
        for i in range(len(nums)-1)[::-1]:
            right_sum[i] = right_sum[i+1] + nums[i+1]
        
        res = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            res[i] = abs(left_sum[i] - right_sum[i])
        return res
        
        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([10,4,8,3],),[15,1,11,22]),
            (([1],),[0]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().leftRightDifference(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
