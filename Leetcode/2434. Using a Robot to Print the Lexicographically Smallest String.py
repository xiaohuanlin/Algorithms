'''
You are given a string s and a robot that currently holds an empty string t. Apply one of the following operations until s and t are both empty:

Remove the first character of a string s and give it to the robot. The robot will append this character to the string t.
Remove the last character of a string t and give it to the robot. The robot will write this character on paper.
Return the lexicographically smallest string that can be written on the paper.

 

Example 1:

Input: s = "zza"
Output: "azz"
Explanation: Let p denote the written string.
Initially p="", s="zza", t="".
Perform first operation three times p="", s="", t="zza".
Perform second operation three times p="azz", s="", t="".
Example 2:

Input: s = "bac"
Output: "abc"
Explanation: Let p denote the written string.
Perform first operation twice p="", s="c", t="ba". 
Perform second operation twice p="ab", s="c", t="". 
Perform first operation p="ab", s="", t="c". 
Perform second operation p="abc", s="", t="".
Example 3:

Input: s = "bdda"
Output: "addb"
Explanation: Let p denote the written string.
Initially p="", s="bdda", t="".
Perform first operation four times p="", s="", t="bdda".
Perform second operation four times p="addb", s="", t="".
 

Constraints:

1 <= s.length <= 105
s consists of only English lowercase letters.
'''
import unittest

from typing import *


class Solution:
    def robotWithString(self, s: str) -> str:
        sufmin = ["zz" for _ in range(len(s) +1)]       
        for i in range(len(s))[::-1]:
            sufmin[i] = min(sufmin[i+1], s[i])
        stack = []
        res = []
        for i in range(len(s)):
            stack.append(s[i])
            while stack and stack[-1] <= sufmin[i+1]:
                res.append(stack.pop())

        return ''.join(res)
        
        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("zza",), "azz"),
            (("bac",), "abc"),
            (("bdda",), "addb"),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().robotWithString(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
