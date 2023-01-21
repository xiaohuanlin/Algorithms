'''
You are given a string s consisting of the characters 'a', 'b', and 'c' and a non-negative integer k. Each minute, you may take either the leftmost character of s, or the rightmost character of s.

Return the minimum number of minutes needed for you to take at least k of each character, or return -1 if it is not possible to take k of each character.

 

Example 1:

Input: s = "aabaaaacaabc", k = 2
Output: 8
Explanation: 
Take three characters from the left of s. You now have two 'a' characters, and one 'b' character.
Take five characters from the right of s. You now have four 'a' characters, two 'b' characters, and two 'c' characters.
A total of 3 + 5 = 8 minutes is needed.
It can be proven that 8 is the minimum number of minutes needed.
Example 2:

Input: s = "a", k = 1
Output: -1
Explanation: It is not possible to take one 'b' or 'c' so return -1.
 

Constraints:

1 <= s.length <= 105
s consists of only the letters 'a', 'b', and 'c'.
0 <= k <= s.length
'''

from typing import *
import unittest

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0

        def satisfied(win):
            return win[0] >= k and win[1] >= k and win[2] >= k

        l = len(s)
        windows = [0, 0, 0]
        s = s + s
        left = 0
        res = float('inf')

        for right in range(l-1):
            windows[ord(s[right]) - ord('a')] += 1
            if satisfied(windows):
                res = min(res, right - left + 1)

        for right in range(l-1, len(s)):
            windows[ord(s[right]) - ord('a')] += 1
            while left < l and satisfied(windows):
                res = min(res, right - left + 1)
                windows[ord(s[left]) - ord('a')] -= 1
                left += 1
                
        if res == float('inf') or res > len(s) // 2:
            return -1
        return res



class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("aabaaaacaabc",2),8),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().takeCharacters(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()