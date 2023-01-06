'''
You are given an array of strings words. Each element of words consists of two lowercase English letters.

Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.

Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

A palindrome is a string that reads the same forward and backward.

 

Example 1:

Input: words = ["lc","cl","gg"]
Output: 6
Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
Note that "clgglc" is another longest palindrome that can be created.
Example 2:

Input: words = ["ab","ty","yt","lc","cl","ab"]
Output: 8
Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
Note that "lcyttycl" is another longest palindrome that can be created.
Example 3:

Input: words = ["cc","ll","xx"]
Output: 2
Explanation: One longest palindrome is "cc", of length 2.
Note that "ll" is another longest palindrome that can be created, and so is "xx".
 

Constraints:

1 <= words.length <= 105
words[i].length == 2
words[i] consists of lowercase English letters.
'''

from typing import *
import unittest

from collections import defaultdict
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        maps = defaultdict(int)
        cnt = 0
        for w in words:
            reverse_w = w[::-1]
            if maps[reverse_w] == 0:
                maps[w] += 1
            else:
                maps[reverse_w] -= 1
                cnt += 4
        for k, v in maps.items():
            if k == k[::-1] and v > 0:
                cnt += 2
                break
        return cnt

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((["ab","ty","yt","lc","cl","ab"],),8),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().longestPalindrome(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()