'''
Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.

You must write an algorithm that runs in linear time and uses linear extra space.

 

Example 1:

Input: nums = [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.
Example 2:

Input: nums = [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
'''
import unittest
from typing import *


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        min_v = min(nums)
        max_v = max(nums)
        res = 0
        # bucket sort
        bucket_num = 2 * len(nums)
        bucket_size = ((max_v- min_v) // bucket_num) + 1
        bucket_min = [float('+inf') for _ in range(bucket_num)]
        bucket_max = [float('-inf') for _ in range(bucket_num)]
        for num in nums:
            idx = (num - min_v) // bucket_size
            bucket_max[idx] = max(bucket_max[idx], num)
            bucket_min[idx] = min(bucket_min[idx], num)
        
        prev = bucket_max[0]
        for i in range(bucket_num):
            if bucket_max[i] == float('-inf'):
                continue
            res = max(bucket_min[i] - prev, res)
            prev = bucket_max[i]
        return res



class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([3,6,9,1], ), 3),
            (([10], ), 0),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maximumGap(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
