'''
We are given hours, a list of the number of hours worked per day for a given employee.

A day is considered to be a tiring day if and only if the number of hours worked is (strictly) greater than 8.

A well-performing interval is an interval of days for which the number of tiring days is strictly larger than the number of non-tiring days.

Return the length of the longest well-performing interval.

 

Example 1:

Input: hours = [9,9,6,0,6,6,9]
Output: 3
Explanation: The longest well-performing interval is [9,9,6].
Example 2:

Input: hours = [6,6,6]
Output: 0
 

Constraints:

1 <= hours.length <= 104
0 <= hours[i] <= 16
'''
from typing import *

import unittest


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        res = 0
        score = 0
        mem = {}
        for i in range(len(hours)):
            score += 1 if hours[i] > 8 else -1

            if score > 0:
                res = i + 1
            else:
                mem.setdefault(score, i)
                # find the smaller one to get the result
                if score - 1 in mem:
                    res = max(res, i - mem[score - 1])
        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([9,9,6,0,6,6,9],),3),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().longestWPI(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
