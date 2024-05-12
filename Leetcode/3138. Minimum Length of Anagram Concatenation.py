'''
You are given a string s, which is known to be a concatenation of anagrams of some string t.

Return the minimum possible length of the string t.

An anagram is formed by rearranging the letters of a string. For example, "aab", "aba", and, "baa" are anagrams of "aab".

 

Example 1:

Input: s = "abba"

Output: 2

Explanation:

One possible string t could be "ba".

Example 2:

Input: s = "cdef"

Output: 4

Explanation:

One possible string t could be "cdef", notice that t can be equal to s.

 

Constraints:

1 <= s.length <= 105
s consist only of lowercase English letters.
'''
from typing import *
import unittest

from collections import Counter


class Solution:
    def minAnagramLength(self, s: str) -> int:
        pre_sum = [Counter() for _ in range(len(s)+1)]
        for i,w in enumerate(s):
            pre_sum[i+1] = Counter(pre_sum[i])
            if w not in pre_sum[i+1]:
                pre_sum[i+1][w] = 0
            pre_sum[i+1][w] += 1
        
        def check(start, length):
            if start > len(s) - length:
                return False
            while start < len(s):
                if pre_sum[start+length] - pre_sum[start] != pre_sum[start] - pre_sum[start-length]:
                    return False
                start += length
            return True

        for l in range(1, len(s)):
            if len(s) % l == 0 and check(l, l):
                return l
        return len(s)
        


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("abba",),2),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().minAnagramLength(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()