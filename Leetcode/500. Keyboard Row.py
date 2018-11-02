'''

Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.






Example:

Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]


Note:

You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.

'''
import unittest


class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        word_list = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        result = []
        for word in words:
            for pattern in word_list:
                if all(char.lower() in pattern for char in word):
                    result.append(word)
                    break
        return result


class TestSolution(unittest.TestCase):

    def test_findWords(self):
        examples = (
            (["Hello", "Alaska", "Dad", "Peace"], ["Alaska", "Dad"]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().findWords(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()