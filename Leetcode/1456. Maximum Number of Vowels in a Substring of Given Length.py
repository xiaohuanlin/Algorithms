'''
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length
'''
import unittest
from typing import *

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left = 0
        count = 0
        res = 0
        for i in range(len(s)):
            if s[i] in 'aeiou':
                count += 1
            if i - left == k:
                if s[left] in 'aeiou':
                    count -= 1
                left += 1
            res = max(res, count)
        return res

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("leetcode", 3), 2),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maxVowels(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()