'''

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

'''
import unittest


class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1, 0, -1, 0, -2, 2], 0), [
                                            [-1, 0, 0, 1],
                                            [-2, -1, 1, 2],
                                            [-2, 0, 0, 2]
                                        ]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().fourSum(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
