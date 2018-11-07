'''

Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

'''
import unittest


class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return self.get_answer(s, 0)

    def get_answer(self, s, wrong_count):
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                wrong_count += 1
                if wrong_count <= 1:
                    return self.get_answer(s[i+1:j+1], wrong_count) or self.get_answer(s[i:j], wrong_count)
                else:
                    return False
            i += 1
            j -= 1
        return True


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ('aba', True),
            ('abca', True),
            ('abc', False),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().validPalindrome(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
