'''

Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".

'''
import unittest


class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        VOWELS = ('a', 'e', 'i', 'o', 'u')
        vowel_list = []

        for i, s_word in enumerate(s):
            if s_word.lower() in VOWELS:
                vowel_list.append(i)

        str_list = [s for s in s]
        for index, i in enumerate(vowel_list):
            str_list[i] = s[vowel_list[-index - 1]]

        return ''.join(str_list)


class TestSolution(unittest.TestCase):

    def test_reverseVowels(self):
        examples = (
            ('hello', 'holle'),
            ("leetcode", "leotcede"),
            ("", ""),
            ("aA", "Aa")
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().reverseVowels(first), second, msg="first: {}; second: {}".format(first, second))


unittest.main()