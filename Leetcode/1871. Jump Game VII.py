'''
You are given a 0-indexed binary string s and two integers minJump and maxJump. In the beginning, you are standing at index 0, which is equal to '0'. You can move from index i to index j if the following conditions are fulfilled:

i + minJump <= j <= min(i + maxJump, s.length - 1), and
s[j] == '0'.
Return true if you can reach index s.length - 1 in s, or false otherwise.

 

Example 1:

Input: s = "011010", minJump = 2, maxJump = 3
Output: true
Explanation:
In the first step, move from index 0 to index 3. 
In the second step, move from index 3 to index 5.
Example 2:

Input: s = "01101110", minJump = 2, maxJump = 3
Output: false
 

Constraints:

2 <= s.length <= 105
s[i] is either '0' or '1'.
s[0] == '0'
1 <= minJump <= maxJump < s.length
'''
from typing import *

import unittest

from collections import deque

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q = deque()
        q.append(0)
        m = 0
        while q:
            start = q.popleft()
            for next_ in range(max(start + minJump, m + 1), min(start + maxJump + 1, len(s))):
                if s[next_] == "1":
                    continue
                if next_ == len(s) - 1:
                    return True
                q.append(next_)
            m = max(m, start + maxJump)
        return False



class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("011010", 2, 3), True),
            (("01101110", 2, 3), False),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().canReach(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
