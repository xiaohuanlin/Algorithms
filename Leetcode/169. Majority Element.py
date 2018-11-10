'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2

'''
import unittest

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_dict = {}
        length = len(nums)//2
        for num in nums:
            nums_dict[num] = nums_dict.setdefault(num, 0) + 1
            if nums_dict[num] > length:
                return num


class TestSolution(unittest.TestCase):

    def test_majorityElement(self):
        examples = (
            ([3,2,3], 3),
            ([2,2,1,1,1,2,2], 2),
            ([1], 1)
        )
        for first,second in examples:
            self.assert_function(first, second)
        
    def assert_function(self, first, second):
        self.assertEqual(Solution().majorityElement(first), second)

unittest.main()