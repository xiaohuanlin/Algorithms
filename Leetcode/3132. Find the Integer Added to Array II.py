'''
You are given two integer arrays nums1 and nums2.

From nums1 two elements have been removed, and all other elements have been increased (or decreased in the case of negative) by an integer, represented by the variable x.

As a result, nums1 becomes equal to nums2. Two arrays are considered equal when they contain the same integers with the same frequencies.

Return the minimum possible integer x that achieves this equivalence.

 

Example 1:

Input: nums1 = [4,20,16,12,8], nums2 = [14,18,10]

Output: -2

Explanation:

After removing elements at indices [0,4] and adding -2, nums1 becomes [18,14,10].

Example 2:

Input: nums1 = [3,5,5,3], nums2 = [7,7]

Output: 2

Explanation:

After removing elements at indices [0,3] and adding 2, nums1 becomes [7,7].

 

Constraints:

3 <= nums1.length <= 200
nums2.length == nums1.length - 2
0 <= nums1[i], nums2[i] <= 1000
The test cases are generated in a way that there is an integer x such that nums1 can become equal to nums2 by removing two elements and adding x to each element of nums1.
'''
import unittest
from typing import *


class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        res = float('inf')
        for i in range(len(nums1)):
            for j in range(i+1, len(nums1)):
                tmp1 = nums1[i]
                tmp2 = nums1[j]
                nums1[i] = -1
                nums1[j] = -1

                m = 0
                delta = None
                for k in range(len(nums1)):
                    if nums1[k] == -1:
                        continue
                    if delta is None or (m < len(nums2) and nums2[m] - nums1[k] == delta):
                        delta = nums2[m] - nums1[k]
                        m += 1
                    else:
                        break
                else:
                    res = min(res, delta)
                
                nums1[i] = tmp1
                nums1[j] = tmp2
        return res
        

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([4,20,16,12,8], [14,18,10]), -2),
            (([3,5,5,3], [7,7]), 2),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().minimumAddedInteger(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

