'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.
'''
import unittest

class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        length = len(s)
        result_dict = {}
        result_dict_reverse = {}
        for i in range(length):
            if result_dict.setdefault(s[i],t[i]) != t[i]:
                break
            if result_dict_reverse.setdefault(t[i],s[i]) != s[i]:
                break
        else:
            return True
        return False
                


class TestSolution(unittest.TestCase):

    def test_isIsomorphic(self):
        examples = (
            (('ab', 'aa'), False),
            # (('egg', 'add'), True),
            # (('foo', 'bar'), False),
            # (('paper', 'title'), True),
        )
        for first,second in examples:
            self.assert_function(first, second)
        
    def assert_function(self, first, second):
        self.assertEqual(Solution().isIsomorphic(*first), second)

unittest.main()