'''
Given a string s, return true if s is a good string, or false otherwise.

A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).

 

Example 1:

Input: s = "abacbc"
Output: true
Explanation: The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.
Example 2:

Input: s = "aaabb"
Output: false
Explanation: The characters that appear in s are 'a' and 'b'.
'a' occurs 3 times while 'b' occurs 2 times, which is not the same number of times.
 

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.
'''
from typing import *

import unittest
    
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        all_c = [0 for _ in range(26)]
        for c in s:
            all_c[ord(c) - ord('a')] += 1
        set_c = set(all_c)
        return len(set_c) <= 1 or (len(set_c) == 2 and 0 in set_c)
        
        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("abacbc",),True),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().areOccurrencesEqual(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
