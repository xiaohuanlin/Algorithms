'''
Given a 2D integer array nums, return all elements of nums in diagonal order as shown in the below images.

 

Example 1:


Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,4,2,7,5,3,8,6,9]
Example 2:


Input: nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i].length <= 105
1 <= sum(nums[i].length) <= 105
1 <= nums[i][j] <= 105
'''
import unittest

from typing import *

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        maps = {}
        row = len(nums)
        for i in range(row):
            for j in range(len(nums[i])):
                maps.setdefault(i + j, []).append(nums[i][j])
        res = []
        for _, v in sorted(maps.items()):
            res.extend(v[::-1])
        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]], ), [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().findDiagonalOrder(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()