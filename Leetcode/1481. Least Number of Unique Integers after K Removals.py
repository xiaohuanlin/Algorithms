'''
Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

 

Example 1:

Input: arr = [5,5,4], k = 1
Output: 1
Explanation: Remove the single 4, only 5 is left.
Example 2:
Input: arr = [4,3,1,1,3,3,2], k = 3
Output: 2
Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.
 

Constraints:

1 <= arr.length <= 10^5
1 <= arr[i] <= 10^9
0 <= k <= arr.length
'''

from typing import *

import unittest


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counts = {}
        for i in arr:
            counts[i] = counts.setdefault(i, 0) + 1

        l = list(counts.values())
        l.sort()
        for i, num in enumerate(l):
            k -= num
            if k < 0:
                return len(l) - i
        return 0
        

    
class TestSolution(unittest.TestCase):
    def test_case(self):
        examples = (
            (([5], 1), 0),
            (([5,5,4], 1), 1),
            (([4,3,1,1,3,3,2], 3), 2),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().findLeastNumOfUniqueInts(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

