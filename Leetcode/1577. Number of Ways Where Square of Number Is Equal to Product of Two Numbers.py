'''
Given two arrays of integers nums1 and nums2, return the number of triplets formed (type 1 and type 2) under the following rules:

Type 1: Triplet (i, j, k) if nums1[i]2 == nums2[j] * nums2[k] where 0 <= i < nums1.length and 0 <= j < k < nums2.length.
Type 2: Triplet (i, j, k) if nums2[i]2 == nums1[j] * nums1[k] where 0 <= i < nums2.length and 0 <= j < k < nums1.length.
 

Example 1:

Input: nums1 = [7,4], nums2 = [5,2,8,9]
Output: 1
Explanation: Type 1: (1, 1, 2), nums1[1]2 = nums2[1] * nums2[2]. (42 = 2 * 8). 
Example 2:

Input: nums1 = [1,1], nums2 = [1,1,1]
Output: 9
Explanation: All Triplets are valid, because 12 = 1 * 1.
Type 1: (0,0,1), (0,0,2), (0,1,2), (1,0,1), (1,0,2), (1,1,2).  nums1[i]2 = nums2[j] * nums2[k].
Type 2: (0,0,1), (1,0,1), (2,0,1). nums2[i]2 = nums1[j] * nums1[k].
Example 3:

Input: nums1 = [7,7,8,3], nums2 = [1,2,9,7]
Output: 2
Explanation: There are 2 valid triplets.
Type 1: (3,0,2).  nums1[3]2 = nums2[0] * nums2[2].
Type 2: (3,0,1).  nums2[3]2 = nums1[0] * nums1[1].
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
1 <= nums1[i], nums2[i] <= 105
'''
from typing import *

import unittest


from collections import defaultdict
class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        nums1_map = defaultdict(int)
        nums2_map = defaultdict(int)

        for n in nums1:
            nums1_map[n**2] += 1
        for n in nums2:
            nums2_map[n**2] += 1

        cnt = 0
        for i in range(len(nums1)):
            for j in range(i+1, len(nums1)):
                if nums1[i] * nums1[j] in nums2_map:
                    cnt += nums2_map[nums1[i] * nums1[j]]

        for i in range(len(nums2)):
            for j in range(i+1, len(nums2)):
                if nums2[i] * nums2[j] in nums1_map:
                    cnt += nums1_map[nums2[i] * nums2[j]]
        return cnt

        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([7,7,8,3],[1,2,9,7]),2),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().numTriplets(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
