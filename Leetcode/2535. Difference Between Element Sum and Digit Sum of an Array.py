'''
You are given a positive integer array nums.

The element sum is the sum of all the elements in nums.
The digit sum is the sum of all the digits (not necessarily distinct) that appear in nums.
Return the absolute difference between the element sum and digit sum of nums.

Note that the absolute difference between two integers x and y is defined as |x - y|.

 

Example 1:

Input: nums = [1,15,6,3]
Output: 9
Explanation: 
The element sum of nums is 1 + 15 + 6 + 3 = 25.
The digit sum of nums is 1 + 1 + 5 + 6 + 3 = 16.
The absolute difference between the element sum and digit sum is |25 - 16| = 9.
Example 2:

Input: nums = [1,2,3,4]
Output: 0
Explanation:
The element sum of nums is 1 + 2 + 3 + 4 = 10.
The digit sum of nums is 1 + 2 + 3 + 4 = 10.
The absolute difference between the element sum and digit sum is |10 - 10| = 0.
 

Constraints:

1 <= nums.length <= 2000
1 <= nums[i] <= 2000
'''
import unittest

from typing import *

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        def get_dig(num):
            res = 0
            while num != 0:
                res += (num % 10)
                num //= 10
            return res

        ele_sum = 0
        dig_sum = 0
        for n in nums:
            ele_sum += n
            dig_sum += get_dig(n)
        return abs(ele_sum - dig_sum)

        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,15,6,3],),9),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().differenceOfSum(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
