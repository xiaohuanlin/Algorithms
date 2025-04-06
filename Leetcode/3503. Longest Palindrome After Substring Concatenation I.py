'''
You are given two strings, s and t.

You can create a new string by selecting a substring from s (possibly empty) and a substring from t (possibly empty), then concatenating them in order.

Return the length of the longest palindrome that can be formed this way.

 

Example 1:

Input: s = "a", t = "a"

Output: 2

Explanation:

Concatenating "a" from s and "a" from t results in "aa", which is a palindrome of length 2.

Example 2:

Input: s = "abc", t = "def"

Output: 1

Explanation:

Since all characters are different, the longest palindrome is any single character, so the answer is 1.

Example 3:

Input: s = "b", t = "aaaa"

Output: 4

Explanation:

Selecting "aaaa" from t is the longest palindrome, so the answer is 4.

Example 4:

Input: s = "abcde", t = "ecdba"

Output: 5

Explanation:

Concatenating "abc" from s and "ba" from t results in "abcba", which is a palindrome of length 5.

 

Constraints:

1 <= s.length, t.length <= 30
s and t consist of lowercase English letters.
'''
from typing import *

import unittest


class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        t = t[::-1]
        def is_palindrome(x):
            for i in range(len(x) // 2):
                if x[i] != x[-i-1]:
                    return False
            return True
       
        max_pali_s = [1 for _ in range(len(s))]
        for i in range(0, len(s)):
            max_pali = 1
            for j in range(i, len(s)):
                if is_palindrome(s[i:j+1]):
                    max_pali = max(max_pali, j - i + 1)
            max_pali_s[i] = max_pali

        max_pali_t = [1 for _ in range(len(t))]
        for i in range(0, len(t)):
            max_pali = 1
            for j in range(i, len(t)):
                if is_palindrome(t[i:j+1]):
                    max_pali = max(max_pali, j - i + 1)
            max_pali_t[i] = max_pali

        # common substring
        res = max(max(max_pali_s), max(max_pali_t))
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = 0
                res = max(res, 2 * dp[i][j] + max(max_pali_s[i] if i < len(max_pali_s) else 0, max_pali_t[j] if j < len(max_pali_t) else 0))
        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("k", "uryuggfgkp"), 5),
            (("tqrkyvaknctsxieyobebofepsuu", "tghyrqlytksmzybnfz"), 7),
            (("gxutsdmdsg", "mqn"), 5),
            (("dfgimwcmrr", "bmh"), 4),
            (("hc", "jooh"), 4),
            (("n", "no"), 2),
            (("f", "zzvz"), 3),
            (("b", "aaaa"), 4),
            (("abc", "def"), 1),
            (("abcde", "ecdba"), 5),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().longestPalindrome(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
