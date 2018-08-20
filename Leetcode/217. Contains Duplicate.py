'''
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
'''
import unittest

class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # return len(set(nums)) != len(nums)
        # ----------------------------------
        nums_dict = {}
        for num in nums:
            if not nums_dict.get(num, 0):
                nums_dict[num] = 1
            else:
                return True
        return False


class TestSolution(unittest.TestCase):
    
    def test_containsDuplicate(self):
        examples = (
            ([1,2,3,1], True),
            ([1,2,3,4], False),
        )
        for first,second in examples:
            self.assert_function(first, second)
        
    def assert_function(self, first, second):
        self.assertEqual(Solution().containsDuplicate(first), second)

unittest.main()