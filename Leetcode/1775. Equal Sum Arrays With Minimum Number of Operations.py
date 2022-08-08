'''
You are given two arrays of integers nums1 and nums2, possibly of different lengths. The values in the arrays are between 1 and 6, inclusive.

In one operation, you can change any integer's value in any of the arrays to any value between 1 and 6, inclusive.

Return the minimum number of operations required to make the sum of values in nums1 equal to the sum of values in nums2. Return -1​​​​​ if it is not possible to make the sum of the two arrays equal.

 

Example 1:

Input: nums1 = [1,2,3,4,5,6], nums2 = [1,1,2,2,2,2]
Output: 3
Explanation: You can make the sums of nums1 and nums2 equal with 3 operations. All indices are 0-indexed.
- Change nums2[0] to 6. nums1 = [1,2,3,4,5,6], nums2 = [6,1,2,2,2,2].
- Change nums1[5] to 1. nums1 = [1,2,3,4,5,1], nums2 = [6,1,2,2,2,2].
- Change nums1[2] to 2. nums1 = [1,2,2,4,5,1], nums2 = [6,1,2,2,2,2].
Example 2:

Input: nums1 = [1,1,1,1,1,1,1], nums2 = [6]
Output: -1
Explanation: There is no way to decrease the sum of nums1 or to increase the sum of nums2 to make them equal.
Example 3:

Input: nums1 = [6,6], nums2 = [1]
Output: 3
Explanation: You can make the sums of nums1 and nums2 equal with 3 operations. All indices are 0-indexed. 
- Change nums1[0] to 2. nums1 = [2,6], nums2 = [1].
- Change nums1[1] to 2. nums1 = [2,2], nums2 = [1].
- Change nums2[0] to 4. nums1 = [2,2], nums2 = [4].
 

Constraints:

1 <= nums1.length, nums2.length <= 105
1 <= nums1[i], nums2[i] <= 6
'''

from typing import *

import unittest

from heapq import heappush, heappop
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        nums2.sort()
        nums1.sort()
        total_sum1 = sum(nums1)
        total_sum2 = sum(nums2)
        if total_sum1 > total_sum2:
            diff = total_sum1 - total_sum2
        else:
            diff = total_sum2 - total_sum1
            nums1, nums2 = nums2, nums1
        
        nums1_start = len(nums1) - 1
        nums2_start = 0
        count = 0
        while diff > 0:
            if nums1_start >= 0 and nums2_start < len(nums2):
                increase = 6 - nums2[nums2_start]
                decrease = nums1[nums1_start] - 1
                if increase > decrease:
                    nums2_start += 1
                    diff -= increase
                else:
                    nums1_start -= 1
                    diff -= decrease
            elif nums1_start < 0 and nums2_start < len(nums2):
                increase = 6 - nums2[nums2_start]
                nums2_start += 1
                diff -= increase
            elif nums1_start >= 0 and nums2_start >= len(nums2):
                decrease = nums1[nums1_start] - 1
                nums1_start -= 1
                diff -= decrease
            else:
                return -1
            count += 1
        return count
    
        
class TestSolution(unittest.TestCase):
    def test_case(self):
        examples = (
            (([1,2,3,4,5,6], [1,1,2,2,2,2]), 3),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().minOperations(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

