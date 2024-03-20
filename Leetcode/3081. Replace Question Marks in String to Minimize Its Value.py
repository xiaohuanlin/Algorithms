'''
You are given a string s. s[i] is either a lowercase English letter or '?'.

For a string t having length m containing only lowercase English letters, we define the function cost(i) for an index i as the number of characters equal to t[i] that appeared before it, i.e. in the range [0, i - 1].

The value of t is the sum of cost(i) for all indices i.

For example, for the string t = "aab":

cost(0) = 0
cost(1) = 1
cost(2) = 0
Hence, the value of "aab" is 0 + 1 + 0 = 1.
Your task is to replace all occurrences of '?' in s with any lowercase English letter so that the value of s is minimized.

Return a string denoting the modified string with replaced occurrences of '?'. If there are multiple strings resulting in the minimum value, return the
lexicographically smallest
 one.



Example 1:

Input:  s = "???"

Output:  "abc"

Explanation: In this example, we can replace the occurrences of '?' to make s equal to "abc".

For "abc", cost(0) = 0, cost(1) = 0, and cost(2) = 0.

The value of "abc" is 0.

Some other modifications of s that have a value of 0 are "cba", "abz", and, "hey".

Among all of them, we choose the lexicographically smallest.

Example 2:

Input: s = "a?a?"

Output: "abac"

Explanation: In this example, the occurrences of '?' can be replaced to make s equal to "abac".

For "abac", cost(0) = 0, cost(1) = 0, cost(2) = 1, and cost(3) = 0.

The value of "abac" is 1.



Constraints:

1 <= s.length <= 105
s[i] is either a lowercase English letter or '?'.
'''
import unittest

from typing import *


class Solution:
    def minimizeStringValue(self, s: str) -> str:
        l = list(s)
        c = [0 for _ in range(26)]
        marks = []
        for i in range(len(l)):
            if l[i] == '?':
                marks.append(i)
            else:
                c[ord(l[i]) - ord('a')] += 1

        res = []
        for i in marks:
            minv = float('inf')
            mini = -1
            for j in range(len(c)):
                if c[j] < minv:
                    minv = c[j]
                    mini = j
            res.append(chr(ord('a') + mini))
            c[mini] += 1

        res.sort()
        for i in range(len(marks)):
            l[marks[i]] = res[i]
        return ''.join(l)



class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("abcdefghijklmnopqrstuvwxy??",), "abcdefghijklmnopqrstuvwxyaz"),
            # (("a?a?",), "abac"),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().minimizeStringValue(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
