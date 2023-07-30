'''
LeetCode company workers use key-cards to unlock office doors. Each time a worker uses their key-card, the security system saves the worker's name and the time when it was used. The system emits an alert if any worker uses the key-card three or more times in a one-hour period.

You are given a list of strings keyName and keyTime where [keyName[i], keyTime[i]] corresponds to a person's name and the time when their key-card was used in a single day.

Access times are given in the 24-hour time format "HH:MM", such as "23:51" and "09:49".

Return a list of unique worker names who received an alert for frequent keycard use. Sort the names in ascending order alphabetically.

Notice that "10:00" - "11:00" is considered to be within a one-hour period, while "22:51" - "23:52" is not considered to be within a one-hour period.

 

Example 1:

Input: keyName = ["daniel","daniel","daniel","luis","luis","luis","luis"], keyTime = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]
Output: ["daniel"]
Explanation: "daniel" used the keycard 3 times in a one-hour period ("10:00","10:40", "11:00").
Example 2:

Input: keyName = ["alice","alice","alice","bob","bob","bob","bob"], keyTime = ["12:01","12:00","18:00","21:00","21:20","21:30","23:00"]
Output: ["bob"]
Explanation: "bob" used the keycard 3 times in a one-hour period ("21:00","21:20", "21:30").
 

Constraints:

1 <= keyName.length, keyTime.length <= 105
keyName.length == keyTime.length
keyTime[i] is in the format "HH:MM".
[keyName[i], keyTime[i]] is unique.
1 <= keyName[i].length <= 10
keyName[i] contains only lowercase English letters.
'''
from typing import *

import unittest


from collections import defaultdict
from bisect import bisect

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        def transfer_to_time(t_str):
            h, t = t_str.split(':')
            total_a = int(h) * 60 + int(t)
            return total_a

        maps = defaultdict(list)
        res = set()
        for i in range(len(keyName)):
            if keyName[i] in res:
                continue
            l = maps[keyName[i]]
            t = transfer_to_time(keyTime[i])
            idx = bisect(l, t)
            l.insert(idx, t)
            if (idx - 2 >= 0 and max(l[idx-2:idx+1]) - min(l[idx-2:idx+1]) <= 60) \
                or (idx - 1 >= 0 and idx + 1 < len(l) and max(l[idx-1:idx+2]) - min(l[idx-1:idx+2]) <= 60) \
                or (idx + 2 < len(l) and max(l[idx:idx+3]) - min(l[idx:idx+3]) <= 60):
                res.add(keyName[i])
        return sorted(res)
        
        


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((["alice","alice","alice","bob","bob","bob","bob"], ["12:01","12:00","18:00","21:00","21:20","21:30","23:00"],),["bob"]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().alertNames(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()