'''
You are given a list of songs where the ith song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.

 

Example 1:

Input: time = [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
Example 2:

Input: time = [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.
 

Constraints:

1 <= time.length <= 6 * 104
1 <= time[i] <= 500
'''

from typing import *

import unittest

from collections import defaultdict
from bisect import bisect

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        maps = defaultdict(list)
        for i in range(len(time)):
            maps[time[i] % 60].append(i)
        
        res = 0
        for i in range(len(time)):
            k = time[i] % 60
            target_list = maps[(60-k) % 60]
            res += (len(target_list) - bisect(target_list, i))
        return res
        
class TestSolution(unittest.TestCase):
    def test_case(self):
        examples = (
            (([30,20,150,100,40],),3),
        )

        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().numPairsDivisibleBy60(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

