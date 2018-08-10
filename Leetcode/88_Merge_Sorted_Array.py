'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
'''
import unittest

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # iter the nums1 and nums2 with right to left, and change the nums
        nums1_index, nums2_index, result_index = m-1, n-1, m+n-1
        
        while nums1_index >= 0 and nums2_index >= 0:
            if nums1[nums1_index] > nums2[nums2_index]:
                nums1[result_index] = nums1[nums1_index]
                nums1_index -= 1
            else:
                nums1[result_index] = nums2[nums2_index]
                nums2_index -= 1
            result_index -= 1

        # maybe the nums2 still have some number
        if nums2_index >= 0:
            nums1[:result_index+1] = nums2[:nums2_index+1]

        return nums1


class TestSolution(unittest.TestCase):

    def test_merge(self):
        examples = (
            (([1,2,3,0,0,0],3,[2,5,6],3), [1,2,2,3,5,6]),
            (([1,4,5,7,0,0,0],4,[2,3,6],3), [1,2,3,4,5,6,7]),
            (([0],0,[1],1),[1])
        )
        for first,second in examples:
            self.assert_function(first, second)
        
    def assert_function(self, first, second):
        self.assertEqual(Solution().merge(*first), second)

unittest.main()