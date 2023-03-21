'''
You are given a 0-indexed integer array nums. You are allowed to permute nums into a new array perm of your choosing.

We define the greatness of nums be the number of indices 0 <= i < nums.length for which perm[i] > nums[i].

Return the maximum possible greatness you can achieve after permuting nums.



Example 1:

Input: nums = [1,3,5,2,1,3,1]
Output: 4
Explanation: One of the optimal rearrangements is perm = [2,5,1,3,3,1,1].
At indices = 0, 1, 3, and 4, perm[i] > nums[i]. Hence, we return 4.
Example 2:

Input: nums = [1,2,3,4]
Output: 3
Explanation: We can prove the optimal perm is [2,3,4,1].
At indices = 0, 1, and 2, perm[i] > nums[i]. Hence, we return 3.


Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
'''
import unittest

from typing import *


from collections import Counter
class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        nums.sort()
        while fast < len(nums):
            while fast < len(nums) and nums[fast] <= nums[slow]:
                fast += 1
            if fast >= len(nums):
                break
            slow += 1
            fast += 1
        return slow


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,3,5,2,1,3,1],),4),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maximizeGreatness(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
