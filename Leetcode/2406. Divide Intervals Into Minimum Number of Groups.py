'''
You are given a 2D integer array intervals where intervals[i] = [lefti, righti] represents the inclusive interval [lefti, righti].

You have to divide the intervals into one or more groups such that each interval is in exactly one group, and no two intervals that are in the same group intersect each other.

Return the minimum number of groups you need to make.

Two intervals intersect if there is at least one common number between them. For example, the intervals [1, 5] and [5, 8] intersect.



Example 1:

Input: intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]
Output: 3
Explanation: We can divide the intervals into the following groups:
- Group 1: [1, 5], [6, 8].
- Group 2: [2, 3], [5, 10].
- Group 3: [1, 10].
It can be proven that it is not possible to divide the intervals into fewer than 3 groups.
Example 2:

Input: intervals = [[1,3],[5,6],[8,10],[11,13]]
Output: 1
Explanation: None of the intervals overlap, so we can put all of them in one group.


Constraints:

1 <= intervals.length <= 105
intervals[i].length == 2
1 <= lefti <= righti <= 106
'''

from typing import *

import unittest

from bisect import bisect_left, insort

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        ends = []
        for s, e in sorted(intervals):
            if not ends or ends[0] >= s:
                insort(ends, e)
            else:
                i = bisect_left(ends, s)
                ends.pop(i-1)
                insort(ends, e)
        return len(ends)



class TestSolution(unittest.TestCase):
    def test_case(self):
        examples = (
            (([[5,10],[6,8],[1,5],[2,3],[1,10]],),3),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().minGroups(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

