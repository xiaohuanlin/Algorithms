'''

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
import unittest


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # result = []
        #
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         value = nums[i] + nums[j]
        #         if -value in nums:
        #             if nums.count(-value) == 2:
        #                 if -value == nums[i] and -value == nums[j]:
        #                     continue
        #             if nums.count(-value) == 1:
        #                 if -value == nums[i] or -value == nums[j]:
        #                     continue
        #             ele = sorted([nums[i], nums[j], -value])
        #             if ele not in result:
        #                 result.append(ele)
        # return result
        # -----------------------------------------------
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l +=1
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res



class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ([0,0], []),
            ([0,0,1], []),
            ([-1, 0, 1, 2, -1, -4], [
                [-1, 0, 1],
                [-1, -1, 2]
            ]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().threeSum(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
