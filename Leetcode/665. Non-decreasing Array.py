'''

Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:
Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:
Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.
Note: The n belongs to [1, 10,000].

'''
import unittest


class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # if len(nums) <= 2:
        #     return True
        # diff = [nex - pre for pre, nex in zip(nums, nums[1:])]
        # bool_diff = [num < 0 for num in diff]
        # sum_diff = sum(bool_diff)
        # # print(diff, sum_diff)
        # if sum_diff == 1:
        #     # check the pre of 1 and next of 1:
        #     index = bool_diff.index(1)
        #     if index == 0 or index == len(diff)-1:
        #         return True
        #     if diff[index] + diff[index - 1] > 0 or diff[index] + diff[index + 1] > 0:
        #         return True
        #     else:
        #         return False
        # elif sum_diff == 0:
        #     return True
        # return False
        # ---------------------------------------
        # change the first element to second or change second element to first
        # first_choice = nums[:]
        # second_choice = nums[:]
        # for i in range(len(nums)-1):
        #     if nums[i] > nums[i+1]:
        #         first_choice[i] = nums[i+1]
        #         second_choice[i+1] = nums[i]
        #         break
        # return first_choice == sorted(first_choice) or second_choice == sorted(second_choice)
        # ------------------------------------------------------
        des_count = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                des_count += 1
                if i == 0:
                    # delete nums[i], use the pre num to represent current number
                    nums[i] = nums[i+1]
                elif nums[i-1] <= nums[i+1]:
                    nums[i] = nums[i-1]
                else:
                    # or delete nums[i+1], use the pre num to represent current number
                    nums[i+1] = nums[i]

            if des_count > 1:
                return False
        return True



class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ([4,2,3], True),
            ([4,2,1], False),
            ([3,4,2,3], False),
            ([3, 4, 5, 1], True),
            ([1,3,2], True),
            ([2,3,3,2,4], True),
            ([-1,4,2,3], True),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().checkPossibility(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
