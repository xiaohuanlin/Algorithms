'''
You are given an integer array nums with the following properties:

nums.length == 2 * n.
nums contains n + 1 unique elements.
Exactly one element of nums is repeated n times.
Return the element that is repeated n times.
'''

from typing import *
import unittest

from collections import Counter


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        return Counter(nums).most_common(1)[0][0]


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([2,1,2,5,3,2],),2),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().repeatedNTimes(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
