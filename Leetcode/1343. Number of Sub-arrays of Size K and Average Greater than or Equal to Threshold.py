'''
Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average greater than or equal to threshold.

 

Example 1:

Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
Output: 3
Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).
Example 2:

Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
Output: 6
Explanation: The first 6 sub-arrays of size 3 have averages greater than 5. Note that averages are not integers.
 

Constraints:

1 <= arr.length <= 105
1 <= arr[i] <= 104
1 <= k <= arr.length
0 <= threshold <= 104
'''
import unittest
from typing import *

from heapq import heappush, heappop

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        total = 0
        left = 0
        target = threshold * k
        for right in range(len(arr)):
            if right - left == k:
                total -= arr[left]
                left += 1
            total += arr[right]
            if right >= k - 1 and total >= target:
                res += 1
        return res

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([11,13,17,23,29,31,7,5,2,3],3,5),6),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().numOfSubarrays(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()