'''
Given an array arr of 4 digits, find the latest 24-hour time that can be made using each digit exactly once.

24-hour times are formatted as "HH:MM", where HH is between 00 and 23, and MM is between 00 and 59. The earliest 24-hour time is 00:00, and the latest is 23:59.

Return the latest 24-hour time in "HH:MM" format. If no valid time can be made, return an empty string.

 

Example 1:

Input: arr = [1,2,3,4]
Output: "23:41"
Explanation: The valid 24-hour times are "12:34", "12:43", "13:24", "13:42", "14:23", "14:32", "21:34", "21:43", "23:14", and "23:41". Of these times, "23:41" is the latest.
Example 2:

Input: arr = [5,5,5,5]
Output: ""
Explanation: There are no valid 24-hour times as "55:55" is not valid.
 

Constraints:

arr.length == 4
0 <= arr[i] <= 9
'''
from typing import *

import unittest


class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        result = []

        def dfs(w, l):
            if not l:
                result.append(w)
            
            for i in range(len(l)):
                s = l[i]
                l.pop(i)
                dfs(w + s, l)
                l.insert(i, s)
        dfs("", [str(i) for i in arr])

        new_result = []
        for r in result:
            hour, minute = int(r[:2]), int(r[2:])
            if hour > 23:
                continue
            if minute > 59:
                continue
            new_result.append((hour * 60 + minute, r[:2] + ":" + r[2:]))
        return max(new_result)[1] if new_result else ""

        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,2,3,4], ), "23:41"),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().largestTimeFromDigits(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
