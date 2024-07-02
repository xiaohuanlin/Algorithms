'''
You are given an integer array nums. In one operation, you can add or subtract 1 from any element of nums.

Return the minimum number of operations to make all elements of nums divisible by 3.



Example 1:

Input: nums = [1,2,3,4]

Output: 3

Explanation:

All array elements can be made divisible by 3 using 3 operations:

Subtract 1 from 1.
Add 1 to 2.
Subtract 1 from 4.
Example 2:

Input: nums = [3,6,9]

Output: 0



Constraints:

1 <= nums.length <= 50
1 <= nums[i] <= 50
'''
from typing import *
import unittest


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum(n % 3 != 0 for n in nums)


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,2,3,4],),3),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().minimumOperations(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
