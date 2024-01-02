'''
You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.

Return the sum of all the unique elements of nums.

 

Example 1:

Input: nums = [1,2,3,2]
Output: 4
Explanation: The unique elements are [1,3], and the sum is 4.
Example 2:

Input: nums = [1,1,1,1,1]
Output: 0
Explanation: There are no unique elements, and the sum is 0.
Example 3:

Input: nums = [1,2,3,4,5]
Output: 15
Explanation: The unique elements are [1,2,3,4,5], and the sum is 15.
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
'''
import unittest

from typing import *


from collections import Counter

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        c = Counter(nums)
        return sum(k for k, v in c.items() if v == 1)


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,2,3,4,5],),15),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().sumOfUnique(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
