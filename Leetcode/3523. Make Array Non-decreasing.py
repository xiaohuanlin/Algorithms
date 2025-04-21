'''
You are given an integer array nums. In one operation, you can select a subarray and replace it with a single element equal to its maximum value.

Return the maximum possible size of the array after performing zero or more operations such that the resulting array is non-decreasing.

 

Example 1:

Input: nums = [4,2,5,3,5]

Output: 3

Explanation:

One way to achieve the maximum size is:

Replace subarray nums[1..2] = [2, 5] with 5 → [4, 5, 3, 5].
Replace subarray nums[2..3] = [3, 5] with 5 → [4, 5, 5].
The final array [4, 5, 5] is non-decreasing with size 3.

Example 2:

Input: nums = [1,2,3]

Output: 3

Explanation:

No operation is needed as the array [1,2,3] is already non-decreasing.

 

Constraints:

1 <= nums.length <= 2 * 105
1 <= nums[i] <= 2 * 105
'''
import unittest

from typing import *


class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        maxv = 0
        res = 0
        for n in nums:
            if n >= maxv:
                res += 1
                maxv = n
        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([4,2,5,3,5],),3),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maximumPossibleSize(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

