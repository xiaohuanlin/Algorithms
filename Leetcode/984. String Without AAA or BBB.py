'''
Given two integers a and b, return any string s such that:

s has length a + b and contains exactly a 'a' letters, and exactly b 'b' letters,
The substring 'aaa' does not occur in s, and
The substring 'bbb' does not occur in s.
 

Example 1:

Input: a = 1, b = 2
Output: "abb"
Explanation: "abb", "bab" and "bba" are all correct answers.
Example 2:

Input: a = 4, b = 1
Output: "aabaa"
 

Constraints:

0 <= a, b <= 100
It is guaranteed such an s exists for the given a and b.
'''

from typing import *

import unittest


class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        change = False
        if a < b:
            a, b = b, a
            change = True
        two_numbers = min(abs(a - b), b)
        res = ["aab" for _ in range(two_numbers)]
        
        a -= 2 * two_numbers
        b -= two_numbers
        
        for _ in range(b):
            res.append("ab")
            
        a -= b
        
        for _ in range(a):
            res.append("a")
            
        ans = "".join(res)
        if change:
            ans = "".join('a' if c == 'b' else 'b' for c in ans)
        return ans

        
class TestSolution(unittest.TestCase):
    def test_case(self):
        examples = (
            ((4,1),"aabaa"),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().strWithout3a3b(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

