'''
There are n tasks assigned to you. The task times are represented as an integer array tasks of length n, where the ith task takes tasks[i] hours to finish. A work session is when you work for at most sessionTime consecutive hours and then take a break.

You should finish the given tasks in a way that satisfies the following conditions:

If you start a task in a work session, you must complete it in the same work session.
You can start a new task immediately after finishing the previous one.
You may complete the tasks in any order.
Given tasks and sessionTime, return the minimum number of work sessions needed to finish all the tasks following the conditions above.

The tests are generated such that sessionTime is greater than or equal to the maximum element in tasks[i].



Example 1:

Input: tasks = [1,2,3], sessionTime = 3
Output: 2
Explanation: You can finish the tasks in two work sessions.
- First work session: finish the first and the second tasks in 1 + 2 = 3 hours.
- Second work session: finish the third task in 3 hours.
Example 2:

Input: tasks = [3,1,3,1,1], sessionTime = 8
Output: 2
Explanation: You can finish the tasks in two work sessions.
- First work session: finish all the tasks except the last one in 3 + 1 + 3 + 1 = 8 hours.
- Second work session: finish the last task in 1 hour.
Example 3:

Input: tasks = [1,2,3,4,5], sessionTime = 15
Output: 1
Explanation: You can finish all the tasks in one work session.


Constraints:

n == tasks.length
1 <= n <= 14
1 <= tasks[i] <= 10
max(tasks[i]) <= sessionTime <= 15
'''
import unittest

from typing import *
from functools import cache

class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        res = float('inf')

        @cache
        def seek(index, sessions):
            nonlocal res
            if index == len(tasks):
                res = min(res, len(sessions))
                return

            seek(index+1, tuple(sorted(sessions + (tasks[index],))))

            for i in range(len(sessions)):
                if sessions[i] + tasks[index] <= sessionTime:
                    seek(index+1, tuple((s if idx != i else s + tasks[index]) for idx, s in enumerate(sessions)))

        seek(0, ())
        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([9,8,8,10,10,8,10,4,8,9,9,3,10],15),11),
            (([2,3,3,4,4,4,5,6,7,10],12),4),
            (([1,2,3],3),2),
            (([3,1,3,1,1],8),2),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().minSessions(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
