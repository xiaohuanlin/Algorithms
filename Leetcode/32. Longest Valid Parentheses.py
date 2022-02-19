'''
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

 

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 3 * 104
s[i] is '(', or ')'.
'''

from typing import *

import unittest

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        return self.helper(s, 0, len(s))
        
    def helper(self, s: str, start, end):
        if start + 1 >= end:
            return 0

        max_v = 0
        length = 0
        stack = []
        for i in range(start, end):
            if s[i] == ')':
                if not stack:
                    length = 0
                else:
                    stack.pop()
                    length += 2
                    max_v = max(max_v, length)
            else:
                stack.append(i)
        if stack:
            last = stack[len(stack) // 2]
            return max(self.helper(s, start, last), self.helper(s, last + 1, end))
        return max_v
                

class TestSolution(unittest.TestCase):
    def test_case(self):
        examples = (
            ((")", ), 0),
            (("(", ), 0),
            (("())()(()", ), 2),
            (("(()", ), 2),
            ((")()())", ), 4),
            (("", ), 0),
            (("()(()", ), 2),
            (("(((((()()()", ), 6),
            (("()()()(((((", ), 6),
            (("(((()()()))", ), 10),
            (("))))()()()", ), 6),
            (("()()()))))", ), 6),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().longestValidParentheses(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

