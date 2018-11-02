'''

Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000

'''
import unittest


class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # count = 0
        # max_value = 0
        #
        # for i in range(len(nums)):
        #     # print(i, count, max_value)
        #     if nums[i] == 1:
        #         if i == len(nums) - 1 or nums[i] != nums[i+1]:
        #             if count + 1 > max_value:
        #                 max_value = count + 1
        #             count = 0
        #         else:
        #             count += 1
        # return max_value
        # ------------------
        num_list = bytearray(nums).split(b'\x00')
        # print(num_list)
        return max(len(l) for l in num_list)


class TestSolution(unittest.TestCase):

    def test_findMaxConsecutiveOnes(self):
        examples = (
            ([1,1,0,1,1,1], 3),
            ([1,], 1),
            ([0,], 0),
            ([], 0),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().findMaxConsecutiveOnes(first), second, msg="first: {}; second: {}".format(first, second))

unittest.main()