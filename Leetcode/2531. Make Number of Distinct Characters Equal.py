'''
You are given two 0-indexed strings word1 and word2.

A move consists of choosing two indices i and j such that 0 <= i < word1.length and 0 <= j < word2.length and swapping word1[i] with word2[j].

Return true if it is possible to get the number of distinct characters in word1 and word2 to be equal with exactly one move. Return false otherwise.

 

Example 1:

Input: word1 = "ac", word2 = "b"
Output: false
Explanation: Any pair of swaps would yield two distinct characters in the first string, and one in the second string.
Example 2:

Input: word1 = "abcc", word2 = "aab"
Output: true
Explanation: We swap index 2 of the first string with index 0 of the second string. The resulting strings are word1 = "abac" and word2 = "cab", which both have 3 distinct characters.
Example 3:

Input: word1 = "abcde", word2 = "fghij"
Output: true
Explanation: Both resulting strings will have 5 distinct characters, regardless of which indices we swap.
 

Constraints:

1 <= word1.length, word2.length <= 105
word1 and word2 consist of only lowercase English letters.
'''

from typing import *
import unittest

from collections import Counter

class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        a_c = Counter(word1)
        b_c = Counter(word2)
        same_key = set(b_c.keys()) & set(a_c.keys())

        if len(a_c) == len(b_c):
            for k, v in b_c.items():
                for a_k, a_v in a_c.items():
                    if (v == 1 and a_v == 1) or (v > 1 and a_v > 1):
                        return True
            return bool(same_key)
        elif len(a_c) > len(b_c):
            a_c, b_c = b_c, a_c

        if len(b_c) - len(a_c) == 1:
            for k, v in b_c.items():
                if v == 1 and k in a_c:
                    # minus 1 and keep the same
                    for another_k in same_key:
                        if another_k != k and a_c[another_k] > 1:
                            return True
                if v == 1 and k not in a_c:
                    # minus 2 and add 1
                    for a_k, a_v in a_c.items():
                        if a_v == 1 and a_k in b_c:
                            return True
                if v > 1 and k not in a_c:
                    # add 1 and keep the same
                    for another_k in same_key:
                        if another_k != k and a_c[another_k] > 1:
                            return True
        elif len(b_c) - len(a_c) == 2:
            for k, v in b_c.items():
                if v == 1 and k not in a_c:
                    # minus 2 and keep the same
                    for another_k in same_key:
                        if another_k != k and a_c[another_k] > 1:
                            return True
        return False


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("abcc", "aab"), True),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().isItPossible(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()