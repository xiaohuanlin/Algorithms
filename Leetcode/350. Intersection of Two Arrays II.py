'''

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

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
            (([1,2,2,1], [2,2]), [2, 2]),
            (([4,9,5], [9,4,9,8,4]), [4, 9]),
            (([], []), [])
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().intersection(*first), second, msg="first: {}; second: {}".format(first, second))


unittest.main()