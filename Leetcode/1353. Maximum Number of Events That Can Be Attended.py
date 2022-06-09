'''
You are given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.

You can attend an event i at any day d where startTimei <= d <= endTimei. You can only attend one event at any time d.

Return the maximum number of events you can attend.

 

Example 1:


Input: events = [[1,2],[2,3],[3,4]]
Output: 3
Explanation: You can attend all the three events.
One way to attend them all is as shown.
Attend the first event on day 1.
Attend the second event on day 2.
Attend the third event on day 3.
Example 2:

Input: events= [[1,2],[2,3],[3,4],[1,2]]
Output: 4
 

Constraints:

1 <= events.length <= 105
events[i].length == 2
1 <= startDayi <= endDayi <= 105
'''
import unittest
from typing import *

from heapq import heappush, heappop

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        heap = []
        
        i = 0
        res = 0
        for d in range(1, 100001):
            # remove colse event
            while heap and heap[0] < d:
                heappop(heap)
                
            # add all event start for d
            while i < len(events) and events[i][0] == d:
                heappush(heap, events[i][1])
                i += 1
            
            if heap:
                heappop(heap)
                res += 1
        return res

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([[1,2],[2,3],[3,4],[1,2]],),4),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maxEvents(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()