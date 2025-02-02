'''
Given a string s, find any 
substring
 of length 2 which is also present in the reverse of s.

Return true if such a substring exists, and false otherwise.

 

Example 1:

Input: s = "leetcode"

Output: true

Explanation: Substring "ee" is of length 2 which is also present in reverse(s) == "edocteel".

Example 2:

Input: s = "abcba"

Output: true

Explanation: All of the substrings of length 2 "ab", "bc", "cb", "ba" are also present in reverse(s) == "abcba".

Example 3:

Input: s = "abcd"

Output: false

Explanation: There is no substring of length 2 in s, which is also present in the reverse of s.

 

Constraints:

1 <= s.length <= 100
s consists only of lowercase English letters.
'''
import unittest

from typing import *


class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        all_set = set()
        for i in range(len(s)-1):
            all_set.add(s[i:i+2])
        for i in range(len(s)-1):
            if s[i:i+2][::-1] in all_set:
                return True
        return False

    
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("abcba",),True),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().isSubstringPresent(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
