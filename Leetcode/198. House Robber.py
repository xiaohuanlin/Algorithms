'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
'''
import unittest

class Solution:
    def __init__(self):
        self.cache_dict = {}

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # if nums == []:
        #     return 0

        # if len(nums) <= 2:
        #     return max(nums)

        # return max(self.rob(nums[:-2]) + nums[-1], self.rob(nums[:-3]) + nums[-2])
        # ---------------------------------------------------------------------
        if nums == []:
            return 0
        if len(nums) <= 2:
            return max(nums)

        res_num = [nums[0], max(nums[:2]), max(nums[1],nums[0]+nums[2])]
        i = 3
        while i < len(nums):
            new_num = max(res_num[i-2] + nums[i], res_num[i-1])
            res_num.append(new_num)
            i += 1
        return res_num[len(nums)-1]


class TestSolution(unittest.TestCase):

    def test_rob(self):
        examples = (
            ([0], 0),
            ([1,2,3], 4),
            ([1,2,3,1], 4),
            ([2,7,9,3,1], 12),
        )
        for first,second in examples:
            self.assert_function(first, second)
        
    def assert_function(self, first, second):
        self.assertEqual(Solution().rob(first), second)

unittest.main()