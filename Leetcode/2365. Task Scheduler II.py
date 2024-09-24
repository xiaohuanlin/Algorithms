'''
], space = 3
Output: 9
Explanation:
One way to complete all tasks in 9 days is as follows:
Day 1: Complete the 0th task.
Day 2: Complete the 1st task.
Day 3: Take a break.
Day 4: Take a break.
Day 5: Complete the 2nd task.
Day 6: Complete the 3rd task.
Day 7: Take a break.
Day 8: Complete the 4th task.
Day 9: Complete the 5th task.
It can be shown that the tasks cannot be completed in less than 9 days.
Example 2:

Input: tasks = [5,8,8,5], space = 2
Output: 6
Explanation:
One way to complete all tasks in 6 days is as follows:
Day 1: Complete the 0th task.
Day 2: Complete the 1st task.
Day 3: Take a break.
Day 4: Take a break.
Day 5: Complete the 2nd task.
Day 6: Complete the 3rd task.
It can be shown that the tasks cannot be completed in less than 6 days.


Constraints:

1 <= tasks.length <= 105
1 <= tasks[i] <= 109
1 <= space <= tasks.length
'''
from typing import *
import unittest


class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        maps = {}
        maxv = 0
        for i in range(len(tasks)):
            prev = maps.get(tasks[i], -space)
            maps[tasks[i]] = maxv = max(maxv + 1, prev + space + 1)
        return maxv


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,2,1,2,3,1],3),9),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().taskSchedulerII(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
