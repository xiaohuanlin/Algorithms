'''
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

 

Example 1:

Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation: 
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
Example 2:

Input: nums = [6,5,4,8]
Output: [2,1,0,3]
Example 3:

Input: nums = [7,7,7,7]
Output: [0,0,0,0]
 

Constraints:

2 <= nums.length <= 500
0 <= nums[i] <= 100
'''
from typing import *

import unittest

from bisect import bisect_left

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l = sorted(nums)
        res = []
        for n in nums:
            res.append(bisect_left(l, n))
        return res

        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([8,1,2,2,3],),[4,0,1,1,3]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().smallerNumbersThanCurrent(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
