'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
'''
import unittest

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        half_index = len(nums)//2
        half = nums[half_index]
        print(nums, half)
        if target == half:
            return half_index
        elif target > half:
            return half_index + 1 + self.searchInsert(nums[half_index+1:], target)
        else:
            return self.searchInsert(nums[:half_index], target)
        

class TestSolution(unittest.TestCase):

    def test_strStr(self):
        examples = ((([1,3,5,6], 5), 2),
                    (([1,3,5,6], 2), 1),
                    (([1,3,5,6], 7), 4),
                    (([1,3,5,6], 0), 0),
        )
        for first,second in examples:
            self.assert_function(first, second)
        
    def assert_function(self, first, second):
        self.assertEqual(Solution().searchInsert(*first), second)

unittest.main()