'''
Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

Return all the possible results. You may return the answer in any order.

 

Example 1:

Input: s = "()())()"
Output: ["(())()","()()()"]
Example 2:

Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]
Example 3:

Input: s = ")("
Output: [""]
 

Constraints:

1 <= s.length <= 25
s consists of lowercase English letters and parentheses '(' and ')'.
There will be at most 20 parentheses in s.
'''
from typing import *

import unittest
from pprint import pprint


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = set()
        global min_length
        min_length = len(s)

        def form_str(selected):
            ans = ""
            for k in range(len(s)):
                if k in selected:
                    continue
                ans += s[k]
            res.add(ans)

        def get_result(selected, i, count):
            global min_length
            if count < 0:
                return
            if i == len(s):
                if count == 0:
                    if len(selected) < min_length:
                        min_length = len(selected)
                        res.clear()
                    if len(selected) <= min_length:
                        form_str(selected)
                return
            if len(s) - i < count:
                return
            
            if s[i] == '(':
                get_result(selected, i + 1, count + 1)
            elif s[i] == ')':
                get_result(selected, i + 1, count - 1)
            else:
                get_result(selected, i + 1, count)

            selected.add(i)
            get_result(selected, i + 1, count)
            selected.remove(i)
        get_result(set(), 0, 0)
        return list(res)

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("()())()",), ["()()()", "(())()",]),
            (("(a)())()",), ["(a)()()", "(a())()",]),
            ((")(",), [""]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().removeInvalidParentheses(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
