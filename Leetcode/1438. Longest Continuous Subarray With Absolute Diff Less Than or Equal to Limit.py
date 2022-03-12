'''
Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.

 

Example 1:

Input: nums = [8,2,4,7], limit = 4
Output: 2 
Explanation: All subarrays are: 
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4. 
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4. 
Therefore, the size of the longest subarray is 2.
Example 2:

Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4 
Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.
Example 3:

Input: nums = [4,2,2,2,4,4,2,2], limit = 0
Output: 3
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
0 <= limit <= 109
'''
import unittest
from typing import *
from bisect import bisect, bisect_left

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        i = 0
        j = 0
        window = []
        res = 0
        while i < len(nums) and j < len(nums):
            if window and window[-1] - window[0] > limit:
                # to left
                p = bisect_left(window, nums[i])
                del window[p]
                i += 1
            else:
                # to right
                p = bisect(window, nums[j])
                window.insert(p, nums[j])
                j += 1
                if window[-1] - window[0] <= limit:
                    res = max(res, len(window))
        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([8,2,4,7], 4), 2),
            (([10,1,2,4,7,2], 5), 4),
            (([4,2,2,2,4,4,2,2], 0), 3),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().longestSubarray(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
