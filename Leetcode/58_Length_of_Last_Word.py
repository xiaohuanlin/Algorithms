'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
'''

import unittest

class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # return len(s.rstrip(' ').split(' ')[-1])
        start = float('+inf')
        
        for i in range(len(s)-1, -1, -1):
            if s[i] != ' ':
                if start == float('+inf'):
                    start = i
            else:
                if start < float('+inf'):
                    return start - i
        else:
            if start < float('+inf'):
                return start + 1
        return 0



class TestSolution(unittest.TestCase):

    def test_lengthOfLastWord(self):
        examples = (("Hello World", 5),
                    ("a ", 1),
                    ("", 0)
        )
        for first,second in examples:
            self.assert_function(first, second)
        
    def assert_function(self, first, second):
        self.assertEqual(Solution().lengthOfLastWord(first), second)

unittest.main()