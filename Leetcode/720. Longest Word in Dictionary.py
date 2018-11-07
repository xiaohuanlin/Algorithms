'''

Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character at a time by other words in words. If there is more than one possible answer, return the longest word with the smallest lexicographical order.

If there is no answer, return the empty string.
Example 1:
Input:
words = ["w","wo","wor","worl", "world"]
Output: "world"
Explanation:
The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
Example 2:
Input:
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"
Explanation:
Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
Note:

All the strings in the input will only contain lowercase letters.
The length of words will be in the range [1, 1000].
The length of words[i] will be in the range [1, 30].

'''
import unittest


class Solution(object):
    def longestWord(self, words):
        words.sort()
        words_set, longest_word = set(['']), ''
        for word in words:
            # if there is construct number, there must have at least one one-char number
            # the answer like a tree
            if word[:-1] in words_set:
                # print(word[:-1], words_set)
                words_set.add(word)
                if len(word) > len(longest_word):
                    longest_word = word
        return longest_word



class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (["w","wo","wor","worl", "world"], 'world'),
            # (["a", "banana", "app", "appl", "ap", "apply", "apple"], 'apple'),
            # (["w", "wo", "wor", "a", "ab", 'abc'], 'abc'),
            # (["yo","ew","fc","zrc","yodn","fcm","qm","qmo","fcmz","z","ewq","yod","ewqz","y"], 'yodn'),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().longestWord(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
