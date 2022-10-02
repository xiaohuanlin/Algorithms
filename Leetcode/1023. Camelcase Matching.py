'''
Given an array of strings queries and a string pattern, return a boolean array answer where answer[i] is true if queries[i] matches pattern, and false otherwise.

A query word queries[i] matches pattern if you can insert lowercase English letters pattern so that it equals the query. You may insert each character at any position and you may not insert any characters.

 

Example 1:

Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"
Output: [true,false,true,true,false]
Explanation: "FooBar" can be generated like this "F" + "oo" + "B" + "ar".
"FootBall" can be generated like this "F" + "oot" + "B" + "all".
"FrameBuffer" can be generated like this "F" + "rame" + "B" + "uffer".
Example 2:

Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa"
Output: [true,false,true,false,false]
Explanation: "FooBar" can be generated like this "Fo" + "o" + "Ba" + "r".
"FootBall" can be generated like this "Fo" + "ot" + "Ba" + "ll".
Example 3:

Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBaT"
Output: [false,true,false,false,false]
Explanation: "FooBarTest" can be generated like this "Fo" + "o" + "Ba" + "r" + "T" + "est".
 

Constraints:

1 <= pattern.length, queries.length <= 100
1 <= queries[i].length <= 100
queries[i] and pattern consist of English letters.
'''
from typing import *

import unittest

from functools import lru_cache
class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        @lru_cache
        def check(q, q_start, p, p_start):
            if len(q) - q_start < len(p) - p_start:
                return False
            if q_start == len(q):
                return True
            if p_start == len(p):
                return not any(c.isupper() for c in q[q_start:])

            if q[q_start] == p[p_start]:
                return check(q, q_start+1, p, p_start+1)
            if q[q_start].isupper():
                return False
            return check(q, q_start+1, p, p_start)
            
        
        res = []
        for q in queries:
            res.append(check(q, 0, pattern, 0))
        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"],"FoBaT"),[False,True,False,False,False]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().camelMatch(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
