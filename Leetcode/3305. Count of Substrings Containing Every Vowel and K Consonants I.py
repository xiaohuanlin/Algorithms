'''
You are given a string word and a non-negative integer k.

Return the total number of 
substrings
 of word that contain every vowel ('a', 'e', 'i', 'o', and 'u') at least once and exactly k consonants.

 

Example 1:

Input: word = "aeioqq", k = 1

Output: 0

Explanation:

There is no substring with every vowel.

Example 2:

Input: word = "aeiou", k = 0

Output: 1

Explanation:

The only substring with every vowel and zero consonants is word[0..4], which is "aeiou".

Example 3:

Input: word = "ieaouqqieaouqq", k = 1

Output: 3

Explanation:

The substrings with every vowel and one consonant are:

word[0..5], which is "ieaouq".
word[6..11], which is "qieaou".
word[7..12], which is "ieaouq".
 

Constraints:

5 <= word.length <= 250
word consists only of lowercase English letters.
0 <= k <= word.length - 5
'''
import unittest

from typing import *

from collections import Counter

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        presum = [Counter() for _ in range(len(word) + 1)]
        for i in range(1, len(presum)):
            presum[i] = presum[i-1] + Counter(word[i-1])
        
        res = 0
        for i in range(len(word)):
            for j in range(i+1, len(word) + 1):
                c = presum[j] - presum[i]
                if all(c[w] > 0 for w in 'aeiou') and c.total() - sum(c[w] for w in 'aeiou') == k:
                    res += 1
        return res
        
    
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("ieaouqqieaouqq", 1), 3),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().countOfSubstrings(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
