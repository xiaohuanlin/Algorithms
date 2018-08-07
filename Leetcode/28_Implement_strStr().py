'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
'''
import unittest

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0
        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                break
        else:
            return -1
        return i
        

class TestSolution(unittest.TestCase):

    def test_strStr(self):
        examples = ((("hello", "ll"), 2),
                    (("aaaaa", "bba"), -1),
                    (("aabaac", "aac"), 3),
                    (("sss", ""), 0),
        )
        for first,second in examples:
            self.assert_function(first, second)
        
    def assert_function(self, first, second):
        self.assertEqual(Solution().strStr(*first), second)

unittest.main()