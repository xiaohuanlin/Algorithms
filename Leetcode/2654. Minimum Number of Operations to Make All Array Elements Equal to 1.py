'''
You are given a 0-indexed array nums consisiting of positive integers. You can do the following operation on the array any number of times:

Select an index i such that 0 <= i < n - 1 and replace either of nums[i] or nums[i+1] with their gcd value.
Return the minimum number of operations to make all elements of nums equal to 1. If it is impossible, return -1.

The gcd of two integers is the greatest common divisor of the two integers.

 

Example 1:

Input: nums = [2,6,3,4]
Output: 4
Explanation: We can do the following operations:
- Choose index i = 2 and replace nums[2] with gcd(3,4) = 1. Now we have nums = [2,6,1,4].
- Choose index i = 1 and replace nums[1] with gcd(6,1) = 1. Now we have nums = [2,1,1,4].
- Choose index i = 0 and replace nums[0] with gcd(2,1) = 1. Now we have nums = [1,1,1,4].
- Choose index i = 2 and replace nums[3] with gcd(1,4) = 1. Now we have nums = [1,1,1,1].
Example 2:

Input: nums = [2,10,6,14]
Output: -1
Explanation: It can be shown that it is impossible to make all the elements equal to 1.
 

Constraints:

2 <= nums.length <= 50
1 <= nums[i] <= 106
 

Follow-up:

The O(n) time complexity solution works, but could you find an O(1) constant time complexity solution?
'''
from typing import *
import unittest
from math import gcd

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        one = nums.count(1)
        if one > 0:
            return len(nums) - one
            
        left = 0
        g = gcd(nums[0], nums[1])
        l = float('inf')
        for right in range(len(nums)):
            g = gcd(g, nums[right])
            while left < right and g == 1:
                l = min(l, right - left + 1)
                left += 1
                g = gcd(*nums[left: right+1])
        if l == float('inf'):
            return -1
        return len(nums) + l - 2
                
                    

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([2,10,6,14],),-1),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().minOperations(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
