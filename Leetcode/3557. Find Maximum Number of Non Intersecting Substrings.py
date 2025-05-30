'''
You are given a string word.

Return the maximum number of non-intersecting substrings of word that are at least four characters long and start and end with the same letter.

 

Example 1:

Input: word = "abcdeafdef"

Output: 2

Explanation:

The two substrings are "abcdea" and "fdef".

Example 2:

Input: word = "bcdaaaab"

Output: 1

Explanation:

The only substring is "aaaa". Note that we cannot also choose "bcdaaaab" since it intersects with the other substring.

 

Constraints:

1 <= word.length <= 2 * 105
word consists only of lowercase English letters.
'''
import unittest
from typing import *
from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    def maxSubstrings(self, word: str) -> int:
        dp = [0 for _ in range(len(word) + 1)]
        maps = defaultdict(list)
        for i in range(1, len(word) + 1):
            dp[i] = dp[i-1]
            l = maps[word[i-1]]
            heappush(l, i-1)
            if len(l) > 5:
                heappop(l)
            for j in sorted(maps[word[i-1]], reverse=True):
                if i - j >= 4:
                    dp[i] = max(dp[i], dp[j] + 1)
                    break
        return dp[-1]
        

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ("abcdeafdef", 2),
            ("bcdaaaab", 1),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maxSubstrings(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

