'''
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
'''
import unittest

class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        import collections
        s_counter = collections.Counter(s)
        t_counter = collections.Counter(t)
        return s_counter == t_counter     


class TestSolution(unittest.TestCase):
    
    def test_isAnagram(self):
        examples = (
            (('anagram', 'nagaram'), True),
            (('rat', 'car'), False),
        )
        for first,second in examples:
            self.assert_function(first, second)
        
    def assert_function(self, first, second):
        self.assertEqual(Solution().isAnagram(*first), second)

unittest.main()