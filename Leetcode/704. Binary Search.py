'''

Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.


Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1


Note:

You may assume that all elements in nums are unique.
n will be in the range [1, 10000].
The value of each element in nums will be in the range [-9999, 9999].

'''
import unittest


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while right - left > 1:
            mid = (left + right) // 2
            # print(left, mid, right)
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid
            else:
                return mid
        if nums[left] == target:
            return left

        if nums[right] == target:
            return right
        # print(left, right)
        return -1


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([-1,0,3,5,9,12], 9), 4),
            (([-1,0,3,5,9,12], 2), -1),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().search(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
