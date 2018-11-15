'''

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

'''
import unittest


class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        min_diff = float('+inf')
        min_sum = 0
        for i in range(len(nums)):
            first_ele = nums[i]
            j, k = i+1, len(nums) - 1
            while j < k:
                second_ele = nums[j]
                third_ele = nums[k]
                sum_value = first_ele + second_ele + third_ele
                abs_diff = abs(sum_value - target)
                if abs_diff < min_diff:
                    min_diff = abs_diff
                    min_sum = sum_value
                elif sum_value > target:
                    k -= 1
                else:
                    j += 1
        return min_sum


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([-1, 2, 1, -4], 1), 2),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().threeSumClosest(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
