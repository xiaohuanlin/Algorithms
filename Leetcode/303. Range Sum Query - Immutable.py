'''

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.

'''
import unittest


class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.num_size = len(nums)
        self.sum_num = {0:0}
        sum_num = 0
        for i in range(self.num_size):
            sum_num += nums[i]
            self.sum_num[i+1] = sum_num
        print(self.sum_num)


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        i = i if i > 0 else 0
        j = j if j < self.num_size else self.num_size
        return self.sum_num[j+1] - self.sum_num[i]


# Your NumArray object will be instantiated and called as such:
obj = NumArray([1,2,3,4])
param_1 = obj.sumRange(0,2)
print(param_1)

