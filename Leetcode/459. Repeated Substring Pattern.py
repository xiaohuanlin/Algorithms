'''

Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.



Example 1:

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.
Example 2:

Input: "aba"
Output: False
Example 3:

Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

'''
import unittest


class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # from collections import Counter
        # word = Counter(s)
        # times = [1]
        #
        # for i in range(2, max(word.values()) + 1):
        #     # get the number that can divide all values
        #     if all(value % i == 0 for value in word.values()):
        #         times.append(i)
        # # calculate the period time and exclude T = len(s)
        # if times == [1]:
        #     return False
        # for t in times[1:]:
        #     T = len(s)//t
        #
        #     for i in range(len(s)-T):
        #         if s[i+T] != s[i]:
        #             print(s[i+T], s[i], i)
        #             break
        #     else:
        #         return True
        # else:
        #     return False
        # ---------------
        return s in s[1:] + s[:-1]



class TestSolution(unittest.TestCase):

    def test_repeatedSubstringPattern(self):
        examples = (
            ('abab', True),
            ('aba', False),
            ('abcabcabcabc', True),
            ('aaaa', True),
            ('a', False),
            ("abaababaab", True),
            ("babbaaabbbbabbaaabbbbabbaaabbbbabbaaabbbbabbaaabbbbabbaaabbbbabbaaabbbbabbaaabbbbabbaaabbbbabbaaabbb", True),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().repeatedSubstringPattern(first), second, msg="first: {}; second: {}".format(first, second))

unittest.main()