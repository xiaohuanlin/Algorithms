'''
The distance of a pair of integers a and b is defined as the absolute difference between a and b.

Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.

 

Example 1:

Input: nums = [1,3,1], k = 1
Output: 0
Explanation: Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.
Example 2:

Input: nums = [1,1,1], k = 2
Output: 0
Example 3:

Input: nums = [1,6,1], k = 3
Output: 5
 

Constraints:

n == nums.length
2 <= n <= 104
0 <= nums[i] <= 106
1 <= k <= n * (n - 1) / 2
'''

from typing import *

import unittest

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        def count_dis(dis):
            left = 0
            right = 0
            res = 0
            while left < len(nums):
                while right < len(nums) and nums[right] - nums[left] <= dis:
                    right += 1
                res += (right - left - 1)
                left += 1

            return res
        
        start = 0
        end = max(nums) - min(nums)
        
        while start < end:
            middle = start + (end - start) // 2
            count = count_dis(middle)
            if count < k:
                start = middle + 1
            else:
                end = middle
        return start
    
        
class TestSolution(unittest.TestCase):
    def test_case(self):
        examples = (
            (([1,3,1],1),0),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().smallestDistancePair(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

