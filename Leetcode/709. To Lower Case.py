'''

Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.



Example 1:

Input: "Hello"
Output: "hello"
Example 2:

Input: "here"
Output: "here"
Example 3:

Input: "LOVELY"
Output: "lovely"

'''
import unittest


class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return str.lower()


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ('here', 'here'),
            ('Hello', 'hello')
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().toLowerCase(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
