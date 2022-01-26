'''
You are given two strings a and b of the same length. Choose an index and split both strings at the same index, splitting a into two strings: aprefix and asuffix where a = aprefix + asuffix, and splitting b into two strings: bprefix and bsuffix where b = bprefix + bsuffix. Check if aprefix + bsuffix or bprefix + asuffix forms a palindrome.

When you split a string s into sprefix and ssuffix, either ssuffix or sprefix is allowed to be empty. For example, if s = "abc", then "" + "abc", "a" + "bc", "ab" + "c" , and "abc" + "" are valid splits.

Return true if it is possible to form a palindrome string, otherwise return false.

Notice that x + y denotes the concatenation of strings x and y.

 

Example 1:

Input: a = "x", b = "y"
Output: true
Explaination: If either a or b are palindromes the answer is true since you can split in the following way:
aprefix = "", asuffix = "x"
bprefix = "", bsuffix = "y"
Then, aprefix + bsuffix = "" + "y" = "y", which is a palindrome.
Example 2:

Input: a = "xbdef", b = "xecab"
Output: false
Example 3:

Input: a = "ulacfd", b = "jizalu"
Output: true
Explaination: Split them at index 3:
aprefix = "ula", asuffix = "cfd"
bprefix = "jiz", bsuffix = "alu"
Then, aprefix + bsuffix = "ula" + "alu" = "ulaalu", which is a palindrome.
 

Constraints:

1 <= a.length, b.length <= 105
a.length == b.length
a and b consist of lowercase English letters
'''
from typing import *

import unittest


class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        return self.check(a, b) or self.check(b, a)
        
    def check(self, a, b):
        left = 0
        right = len(a) - 1
        while left < right:
            if a[left] != b[right]:
                return self.checkPalindrome(a, left, right) or self.checkPalindrome(b, left, right)
            left += 1
            right -= 1
        return True

    
    def checkPalindrome(self, a, a_start, a_end):
        while a_start < a_end and a[a_start] == a[a_end]:
            a_start += 1
            a_end -= 1

        return a_start >= a_end


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (('x', 'y'), True),
            (('xbdef', 'xecab'), False),
            (('ulacfd', 'jizalu'), True),
            (('abdef', 'fecab'), True),
            (('abcdcbf', 'fecabaa'), True),
            (('pvhmupgqeltozftlmfjjde', 'yjgpzbezspnnpszebzmhvp'), True),
            (('abmsbz', 'wyzzka'), False),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().checkPalindromeFormation(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
