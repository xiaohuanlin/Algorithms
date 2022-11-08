'''
Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors. If there is no such integer in the array, return 0.

 

Example 1:

Input: nums = [21,4,7]
Output: 32
Explanation: 
21 has 4 divisors: 1, 3, 7, 21
4 has 3 divisors: 1, 2, 4
7 has 2 divisors: 1, 7
The answer is the sum of divisors of 21 only.
Example 2:

Input: nums = [21,21]
Output: 64
Example 3:

Input: nums = [1,2,3,4,5]
Output: 0
 

Constraints:

1 <= nums.length <= 104
1 <= nums[i] <= 105
'''

from typing import *
import unittest

from math import sqrt

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def count_with_sum(num):
            count = 0
            total = 0
            for i in range(1, int(sqrt(num))+1):
                if num % i == 0:
                    if num // i != i:
                        count += 2
                        total += (i + num // i)
                    else:
                        count += 1
                        total += i
                if count > 4:
                    return False, total
            return count == 4, total
        
        res = 0
        for n in nums:
            is_four, s = count_with_sum(n)
            if is_four:
                res += s
        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,2,3,4,5],),0),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().sumFourDivisors(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()