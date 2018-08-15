'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
'''
import unittest

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # use the Divide and Conquer to do that, specifically, the quickly sort.
        
        # for deeper user, can use the XOR.
        result = 0
        for num in nums:
            result ^= num
        return result


class TestSolution(unittest.TestCase):

    def test_singleNumber(self):
        examples = (
            ([2,2,1], 1),
            ([4,1,2,1,2], 4),
        )
        for first,second in examples:
            self.assert_function(first, second)
        
    def assert_function(self, first, second):
        self.assertEqual(Solution().singleNumber(first), second)

unittest.main()
