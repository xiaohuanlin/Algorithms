'''
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
'''
import unittest


class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        from itertools import zip_longest
        word_dict = {}
        part_dict = {}
        for key, value in zip_longest(pattern, str.split(' ')):
            if key is None or value is None:
                return False
            if part_dict.setdefault(key, value) != value:
                return False
            if word_dict.setdefault(value, key) != key:
                return False
            if len(word_dict) != len(part_dict):
                return False
        return True


class TestSolution(unittest.TestCase):

    def test_wordPattern(self):
        examples = (
            (('abba', "dog cat cat dog"), True),
            (('abba', "dog cat cat fish"), False),
            (('aaaa', "dog cat cat dog"), False),
            (('abba', "dog dog dog dog"), False),
            (('abba', "dog cat cat"), False),
            (('aba', "dog cat cat"), False),
            (('', "beef"), False)
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().wordPattern(*first), second, msg="first: {}; second: {}".format(first, second))


unittest.main()