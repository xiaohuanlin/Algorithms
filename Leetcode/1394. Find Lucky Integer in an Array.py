'''
Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.

Return the largest lucky integer in the array. If there is no lucky integer return -1.

 

Example 1:

Input: arr = [2,2,3,4]
Output: 2
Explanation: The only lucky number in the array is 2 because frequency[2] == 2.
Example 2:

Input: arr = [1,2,2,3,3,3]
Output: 3
Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.
Example 3:

Input: arr = [2,2,2,3,3]
Output: -1
Explanation: There are no lucky numbers in the array.
 

Constraints:

1 <= arr.length <= 500
1 <= arr[i] <= 500
'''
import unittest

from typing import *

from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        res = -1
        for k, v in Counter(arr).items():
            if k == v:
                res = max(res, k)
        return res
        


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,2,2,3,3,3],),3),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().findLucky(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
