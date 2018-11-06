'''

The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]
Note:
The given array size will in the range [2, 10000].
The given array's numbers won't have any order.

'''
import unittest


class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # num_dict = dict(zip(range(1,len(nums)+1), [0] * len(nums)))
        # # print(num_dict)
        # for num in nums:
        #     num_dict[num] += 1
        # for key, value in num_dict.items():
        #     if value == 0:
        #         miss_key = key
        #     if value == 2:
        #         dup_key = key
        # return [dup_key, miss_key]
        # ------------------------------------
        n = len(nums)
        sum_n = n * (n+1) // 2
        sum_nums = sum(nums)
        sum_nums_set = sum(set(nums))
        # print(sum_n, sum_nums, sum_nums_set)
        return [sum_nums-sum_nums_set, sum_n-sum_nums_set]


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ([1,2,2,4], [2,3]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().findErrorNums(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
