'''
Given two strings: s1 and s2 with the same size, check if some permutation of string s1 can break some permutation of string s2 or vice-versa. In other words s2 can break s1 or vice-versa.

A string x can break string y (both of size n) if x[i] >= y[i] (in alphabetical order) for all i between 0 and n-1.

 

Example 1:

Input: s1 = "abc", s2 = "xya"
Output: true
Explanation: "ayx" is a permutation of s2="xya" which can break to string "abc" which is a permutation of s1="abc".
Example 2:

Input: s1 = "abe", s2 = "acd"
Output: false 
Explanation: All permutations for s1="abe" are: "abe", "aeb", "bae", "bea", "eab" and "eba" and all permutation for s2="acd" are: "acd", "adc", "cad", "cda", "dac" and "dca". However, there is not any permutation from s1 which can break some permutation from s2 and vice-versa.
Example 3:

Input: s1 = "leetcodee", s2 = "interview"
Output: true
 

Constraints:

s1.length == n
s2.length == n
1 <= n <= 10^5
All strings consist of lowercase English letters.
'''
import unittest
from typing import *

class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1_count = [0 for _ in range(26)]
        s2_count = [0 for _ in range(26)]
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
            
        i = 0
        j = 0
        left_bigger = True
        right_bigger = True
        while i < 26 and j < 26:
            while i < 26 and s1_count[i] == 0:
                i += 1
            while j < 26 and s2_count[j] == 0:
                j += 1
            if i >= 26 or j >= 26:
                break
            left_bigger = left_bigger and (i >= j)
            right_bigger = right_bigger and (i <= j)
            delta = min(s1_count[i], s2_count[j])
            s1_count[i] -= delta
            s2_count[j] -= delta
        return left_bigger or right_bigger

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("abc", "xya"), True),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().checkIfCanBreak(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()