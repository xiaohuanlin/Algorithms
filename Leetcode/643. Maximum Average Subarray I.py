'''

Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
Note:
1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].

'''
import unittest


class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # pre = nums[:k]
        # max_sum_num = sum_num = sum(pre)
        # for num in nums[k:]:
        #     pre.append(num)
        #     value = pre.pop(0)
        #     sum_num = sum_num + num - value
        #     if sum_num > max_sum_num:
        #         max_sum_num = sum_num
        #     # print(pre, sum_num, max_sum_num)
        # return max_sum_num/k
        # ---------------------------------------
        max_sum_num = sum_num = sum(nums[:k])
        for pre, nex in zip(nums, nums[k:]):
            sum_num = sum_num + nex - pre
            if sum_num > max_sum_num:
                max_sum_num = sum_num
            # print(pre, sum_num, max_sum_num)
        return max_sum_num/k


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,12,-5,-6,50,3], 4), 12.75),
            (([0,4,0,3,2], 1), 4.0),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().findMaxAverage(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
