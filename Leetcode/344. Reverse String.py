'''

Write a function that takes a string as input and returns the string reversed.

Example 1:

Input: "hello"
Output: "olleh"
Example 2:

Input: "A man, a plan, a canal: Panama"
Output: "amanaP :lanac a ,nalp a ,nam A"

'''
import unittest


class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        new_str = []
        for i in range(len(s)):
            index = len(s) - 1 - i
            new_str.append(s[index])
        return ''.join(new_str)


class TestSolution(unittest.TestCase):

    def test_reverseString(self):
        examples = (
            ("A man, a plan, a canal: Panama", "amanaP :lanac a ,nalp a ,nam A"),
            ("hello", "olleh"),
            ("", "")
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().reverseString(first), second, msg="first: {}; second: {}".format(first, second))


unittest.main()