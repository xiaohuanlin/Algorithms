'''
Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.

A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.

 

Example 1:

Input: n = 1
Output: 5
Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].
Example 2:

Input: n = 2
Output: 15
Explanation: The 15 sorted strings that consist of vowels only are
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.
Example 3:

Input: n = 33
Output: 66045
 

Constraints:

1 <= n <= 50 
'''
import unittest
from typing import *


class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [1 for _ in range(5)]
        
        for _ in range(n-1):
            dp[4] = dp[0] + dp[1] + dp[2] + dp[3] + dp[4]
            dp[3] = dp[0] + dp[1] + dp[2] + dp[3]
            dp[2] = dp[0] + dp[1] + dp[2]
            dp[1] = dp[0] + dp[1]
        return sum(dp)

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((2,),15),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().countVowelStrings(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()