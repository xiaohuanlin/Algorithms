'''

Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital if it has more than one letter, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
Example 1:
Input: "USA"
Output: True
Example 2:
Input: "FlaG"
Output: False
Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.

'''
import unittest


class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
    #     word_list = list(word)
    #     upper = True if word[0].isupper() else False
    #     if upper:
    #         return self.upper(word_list[1:]) or self.lower(word_list[1:])
    #     else:
    #         return self.lower(word_list[1:])
    #
    # def upper(self, word_list):
    #     if not word_list:
    #         return True
    #     return word_list[0].isupper() and self.upper(word_list[1:])
    #
    # def lower(self, word_list):
    #     if not word_list:
    #         return True
    #     return word_list[0].islower() and self.lower(word_list[1:])
    # ---------------------------------
        return (word[0].isupper() and (word[1:].isupper() or word[1:].islower() or not word[1:])) or word.islower()


class TestSolution(unittest.TestCase):

    def test_detectCapitalUse(self):
        examples = (
            ('USA', True),
            ('FlaG', False),
            ('leetcode', True),
            ('Google', True),
            ('a', True),
            ('G', True)
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().detectCapitalUse(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()