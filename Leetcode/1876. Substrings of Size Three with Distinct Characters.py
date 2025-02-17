'''
A string is good if there are no repeated characters.

Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.

Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

A substring is a contiguous sequence of characters in a string.

 

Example 1:

Input: s = "xyzzaz"
Output: 1
Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
The only good substring of length 3 is "xyz".
Example 2:

Input: s = "aababcabc"
Output: 4
Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
The good substrings are "abc", "bca", "cab", and "abc".
 

Constraints:

1 <= s.length <= 100
s​​​​​​ consists of lowercase English letters.
'''
import unittest

from typing import *


class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += (len(set(s[i:i+3])) == 3)
        return res
        
    
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("aababcabc",),4),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().countGoodSubstrings(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
