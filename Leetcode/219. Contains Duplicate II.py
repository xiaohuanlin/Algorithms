'''
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false

'''
import unittest

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        nums_dict = {}
        for i in range(len(nums)):
            value = nums_dict.setdefault(nums[i], i)
            if 0 < i - value <= k:
                return True
            else:
                nums_dict[nums[i]] = i
        return False 


class TestSolution(unittest.TestCase):
    
    def test_containsNearbyDuplicate(self):
        examples = (
            (([1,2,3,1], 3), True),
            (([1,0,0,1], 1), True),
            (([1,2,3,1,2,3], 2), False),
        )
        for first,second in examples:
            self.assert_function(first, second)
        
    def assert_function(self, first, second):
        self.assertEqual(Solution().containsNearbyDuplicate(*first), second)

unittest.main()