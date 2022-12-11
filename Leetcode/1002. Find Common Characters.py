'''
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

 

Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.
'''
from typing import *

import unittest

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        chars = [float('inf') for _ in range(26)]
        current = [0 for _ in range(26)]
        
        for word in words:
            for s in word:
                current[ord(s) - ord('a')] += 1
            for i in range(26):
                chars[i] = min(chars[i], current[i])
            current = [0 for _ in range(26)]

        res = []
        for i in range(26):
            for _ in range(chars[i]):
                res.append(chr(ord('a') + i))
        return res
        

        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((["cool","lock","cook"],), ["c","o"]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().commonChars(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()


