'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''
import unittest


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         while i > 0 and nums[i-1] == 0:
        #             nums[i], nums[i-1] = nums[i-1], nums[i]
        #             i -= 1
        count = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[count], nums[i] = nums[i], nums[count]
                count += 1
        return nums


class TestSolution(unittest.TestCase):

    def test_moveZeroes(self):
        examples = (
            ([0,1,0,3,12], [1,3,12,0,0]),
            ([1,2,3], [1,2,3]),
            ([1,0,2,0,3], [1,2,3,0,0]),
            ([0,0,1], [1,0,0]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().moveZeroes(first), second, msg="first: {}; second: {}".format(first, second))


unittest.main()