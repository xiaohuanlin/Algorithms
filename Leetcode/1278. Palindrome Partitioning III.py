'''
You are given a string s containing lowercase letters and an integer k. You need to :

First, change some characters of s to other lowercase English letters.
Then divide s into k non-empty disjoint substrings such that each substring is a palindrome.
Return the minimal number of characters that you need to change to divide the string.

 

Example 1:

Input: s = "abc", k = 2
Output: 1
Explanation: You can split the string into "ab" and "c", and change 1 character in "ab" to make it palindrome.
Example 2:

Input: s = "aabbc", k = 3
Output: 0
Explanation: You can split the string into "aa", "bb" and "c", all of them are palindrome.
Example 3:

Input: s = "leetcode", k = 8
Output: 0
 

Constraints:

1 <= k <= s.length <= 100.
s only contains lowercase English letters.
'''
from typing import *

import unittest
    
from functools import lru_cache
class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        dp = [[0 for _ in range(len(s) + 1)] for _ in range(len(s))]
        for size in range(1, len(s) + 1):
            for i in range(len(s)):
                if i + size > len(s):
                    continue
                dp[i][i+size] = (dp[i+1][i+size-1] if i + 1 <= i + size - 1 else 0) + int((s[i] != s[i+size-1]))
        global res
        res = len(s)
        
        @lru_cache(None)
        def dfs(start, target, cost):
            global res
            if cost > res:
                return
            if target == 0 and start == len(s):
                res = min(res, cost)
                return
            if target < 0:
                return
            
            for end in range(start + 1, len(s) + 1):
                dfs(end, target - 1, cost + dp[start][end])
                
        
        dfs(0, k, 0)
        return res
        
        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("abc", 2), 1),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().palindromePartition(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
