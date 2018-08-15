'''
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
'''
import unittest

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # find the right index of the number
        number_dict = {
            numbers[index]: index for index in range(len(numbers))
        }
        for index in range(len(numbers)):
            num_res = target - numbers[index]
            num_res_index = number_dict.get(num_res)
            if num_res_index and index != num_res_index:
                return [min(index+1, num_res_index+1), max(index+1, num_res_index+1)]


class TestSolution(unittest.TestCase):

    def test_twoSum(self):
        examples = (
            (([2,7,11,15], 9), [1,2]),
            (([1,2,7,11,15], 16), [1,5]),
        )
        for first,second in examples:
            self.assert_function(first, second)
        
    def assert_function(self, first, second):
        self.assertEqual(Solution().twoSum(*first), second)

unittest.main()