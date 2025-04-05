'''
You are given a 2D integer array properties having dimensions n x m and an integer k.

Define a function intersect(a, b) that returns the number of distinct integers common to both arrays a and b.

Construct an undirected graph where each index i corresponds to properties[i]. There is an edge between node i and node j if and only if intersect(properties[i], properties[j]) >= k, where i and j are in the range [0, n - 1] and i != j.

Return the number of connected components in the resulting graph.

 

Example 1:

Input: properties = [[1,2],[1,1],[3,4],[4,5],[5,6],[7,7]], k = 1

Output: 3

Explanation:

The graph formed has 3 connected components:



Example 2:

Input: properties = [[1,2,3],[2,3,4],[4,3,5]], k = 2

Output: 1

Explanation:

The graph formed has 1 connected component:



Example 3:

Input: properties = [[1,1],[1,1]], k = 2

Output: 2

Explanation:

intersect(properties[0], properties[1]) = 1, which is less than k. This means there is no edge between properties[0] and properties[1] in the graph.

 

Constraints:

1 <= n == properties.length <= 100
1 <= m == properties[i].length <= 100
1 <= properties[i][j] <= 100
1 <= k <= m
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
