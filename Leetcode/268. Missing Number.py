'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
'''
import unittest


class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return (set(range(len(nums) + 1)) - set(nums)).pop()
        return sum(range(len(nums) + 1)) - sum(nums)


class TestSolution(unittest.TestCase):

    def test_missingNumber(self):
        examples = (
            ([3,0,1], 2),
            ([9,6,4,2,3,5,7,0,1], 8),
            ([0,], 1)
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().missingNumber(first), second, msg="first: {}; second: {}".format(first, second))


unittest.main()