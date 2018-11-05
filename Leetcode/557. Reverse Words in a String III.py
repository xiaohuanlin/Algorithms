'''

Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.

'''
import unittest


class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(w[::-1] for w in s.split(' '))


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ("Let's take LeetCode contest", "s'teL ekat edoCteeL tsetnoc"),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().reverseWords(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
