'''
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
 

Constraints:

1 <= s.length <= 105
s[i] is either'(' , ')', or lowercase English letter.
'''
import unittest


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for i, w in enumerate(s):
            if w.isalpha():
                continue
            elif w == ")":
                if stack and s[stack[-1]] == "(":
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
        
        res = []
        stack = set(stack)
        for i, w in enumerate(s):
            if i in stack:
                continue
            res.append(w)
        return "".join(res)
        


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("lee(t(c)o)de)",), "lee(t(c)o)de"),
            (("a)b(c)d",),"ab(c)d"),
            (("))((",),""),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().minRemoveToMakeValid(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
