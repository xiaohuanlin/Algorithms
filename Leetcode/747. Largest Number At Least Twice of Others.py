'''

In a given integer array nums, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as every other number in the array.

If it is, return the index of the largest element, otherwise return -1.

Example 1:

Input: nums = [3, 6, 1, 0]
Output: 1
Explanation: 6 is the largest integer, and for every other number in the array x,
6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.


Example 2:

Input: nums = [1, 2, 3, 4]
Output: -1
Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.


Note:

nums will have a length in the range [1, 50].
Every nums[i] will be an integer in the range [0, 99].

'''
import unittest


class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num, max_index, second_max = 0, 0, 0

        for index, num in enumerate(nums):
            if num > max_num:
                max_index, max_num, second_max = index, num, max_num
            elif num > second_max:
                second_max = num
            # print(max_num, max_index, second_max)
        return max_index if max_num >= second_max * 2 else -1



class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ([3, 6, 1, 0], 1),
            ([1, 2, 3, 4], -1),
            ([1,], -1),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().dominantIndex(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
