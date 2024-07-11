'''
Given an integer array nums, return the most frequent even element.

If there is a tie, return the smallest one. If there is no such element, return -1.

 

Example 1:

Input: nums = [0,1,2,2,4,4,1]
Output: 2
Explanation:
The even elements are 0, 2, and 4. Of these, 2 and 4 appear the most.
We return the smallest one, which is 2.
Example 2:

Input: nums = [4,4,4,9,2,4]
Output: 4
Explanation: 4 is the even element appears the most.
Example 3:

Input: nums = [29,47,21,41,13,37,25,7]
Output: -1
Explanation: There is no even element.
 

Constraints:

1 <= nums.length <= 2000
0 <= nums[i] <= 105
'''
from typing import *
import unittest


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        c = Counter(nums)
        max_f = 0
        max_v = -1
        for k in sorted(c.keys()):
            if k % 2 == 0:
                if c[k] > max_f:
                    max_f = c[k]
                    max_v = k
        return max_v


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([4,4,4,9,2,4],),4),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().mostFrequentEven(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()