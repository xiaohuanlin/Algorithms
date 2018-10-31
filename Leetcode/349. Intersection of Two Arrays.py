'''

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.

'''
import unittest


class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        value_list = []
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        while len(nums1) != 0 and len(nums2) != 0:
            if nums1[0] == nums2[0]:
                if nums1[0] not in value_list:
                    value_list.append(nums1[0])
                nums1.pop(0)
                nums2.pop(0)
            elif nums1[0] < nums2[0]:
                nums1.pop(0)
            elif nums1[0] > nums2[0]:
                nums2.pop(0)
        return value_list


class TestSolution(unittest.TestCase):

    def test_intersection(self):
        examples = (
            (([1,2,2,1], [2,2]), [2]),
            (([4,9,5], [9,4,9,8,4]), [9,4]),
            (([], []), [])
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().intersection(*first), second, msg="first: {}; second: {}".format(first, second))


unittest.main()