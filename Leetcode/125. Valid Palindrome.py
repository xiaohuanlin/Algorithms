'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
'''
import unittest

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_list = []
        for ele in s:
            if ele.isalpha() or ele.isnumeric():
                s_list.append(ele.lower())
        str_list = ''.join(s_list)
        if str_list[::-1] == str_list:
            return True
        return False


class TestSolution(unittest.TestCase):

    def test_isPalindrome(self):
        examples = (
            ("A man, a plan, a canal: Panama", True),
            ("race a car", False),
            ("", True)
        )
        for first,second in examples:
            self.assert_function(first, second)
        
    def assert_function(self, first, second):
        self.assertEqual(Solution().isPalindrome(first), second)

unittest.main()