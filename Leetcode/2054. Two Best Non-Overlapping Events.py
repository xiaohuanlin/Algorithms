'''
You are given a 0-indexed 2D integer array of events where events[i] = [startTimei, endTimei, valuei]. The ith event starts at startTimei and ends at endTimei, and if you attend this event, you will receive a value of valuei. You can choose at most two non-overlapping events to attend such that the sum of their values is maximized.

Return this maximum sum.

Note that the start time and end time is inclusive: that is, you cannot attend two events where one of them starts and the other ends at the same time. More specifically, if you attend an event with end time t, the next event must start at or after t + 1.

 

Example 1:


Input: events = [[1,3,2],[4,5,2],[2,4,3]]
Output: 4
Explanation: Choose the green events, 0 and 1 for a sum of 2 + 2 = 4.
Example 2:

Example 1 Diagram
Input: events = [[1,3,2],[4,5,2],[1,5,5]]
Output: 5
Explanation: Choose event 2 for a sum of 5.
Example 3:


Input: events = [[1,5,3],[1,5,1],[6,6,5]]
Output: 8
Explanation: Choose events 0 and 2 for a sum of 3 + 5 = 8.
 

Constraints:

2 <= events.length <= 105
events[i].length == 3
1 <= startTimei <= endTimei <= 109
1 <= valuei <= 106
'''
from typing import *
import unittest
from bisect import bisect_left, bisect_right

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        sorted_value = [(0, 0)]
        events = sorted(events, key=lambda x: x[1])
        max_first = 0
        max_v = 0
        for start, end, value in events:
            p = bisect_left(sorted_value, (start, 0))
            first = sorted_value[p-1]
            max_v = max(max_v, first[1] + value)
            max_first = max(max_first, value)
            sorted_value.append((end, max_first))
        return max_v


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([[1,5,3],[1,5,1],[6,6,5]],),8),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maxTwoEvents(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
