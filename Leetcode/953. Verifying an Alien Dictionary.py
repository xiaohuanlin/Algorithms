'''
In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

 

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.
'''

from typing import *
import unittest


from functools import cmp_to_key
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        def cmp(a, b):
            i = 0
            j = 0
            while i < len(a) and j < len(b):
                i_idx = order.find(a[i])
                j_idx = order.find(b[i])
                if i_idx < j_idx:
                    return -1
                elif i_idx > j_idx:
                    return 1
                i += 1
                j += 1
            
            if i == len(a) and j == len(b):
                return 0
            if i < len(a):
                return 1
            return -1
        
        return words == sorted(words, key=cmp_to_key(cmp))


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((["word","world","row"],"worldabcefghijkmnpqstuvxyz"),False),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().isAlienSorted(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()