'''

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

'''
import unittest


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
    #     i = 0
    #     max_len = 0
    #     max_sub = ''
    #     while i < len(s):
    #         j = len(s) - 1
    #         while i <= j:
    #             # print(i, j)
    #             if s[i] == s[j]:
    #                 if self.judgepalindrome(s[i:j+1]):
    #                     if j-i+1 > max_len:
    #                         max_len = j-i+1
    #                         max_sub = s[i:j+1]
    #                     break
    #             j -= 1
    #         i += 1
    #     return max_sub
    #
    # def judgepalindrome(self, s):
    #     i = 0
    #     j = len(s) - 1
    #     while i < j:
    #         if s[i] != s[j]:
    #             return False
    #         i += 1
    #         j -= 1
    #     return True
    # ---------------------------------------------
    #     two points from i, walk to two side
    #     max_sub = ''
    #     for i in range(len(s)):
    #         tmp = self.get_answer(s, i, i+1)
    #         if len(tmp) > len(max_sub):
    #             max_sub = tmp
    #
    #         tmp = self.get_answer(s, i, i)
    #         if len(tmp) > len(max_sub):
    #             max_sub = tmp
    #     return max_sub
    #
    # def get_answer(self, s, i, j):
    #     # print(i, j)
    #     while i >= 0 and j < len(s) and s[i] == s[j]:
    #         i -= 1
    #         j += 1
    #     return s[i+1: j]
    # ------------------------------------------------
    # there will have 3 case for this problem, when add a char to a string
    # 'daba' + 'd': 3 --> 5
    # 'daaa' + 'a': 3 --> 4
    # 'daba' + 'e': 3 --> 3
    # the first and second case means if it become longer than before, it will attach the tail.
        if len(s) == 0:
            return ''
        max_len = 1
        start = 0
        for i in range(len(s)):
            # for length + 2
            if i >= max_len + 1 and s[i-max_len-1:i+1] == s[i-max_len-1:i+1][::-1]:
                start = i-max_len-1
                max_len += 2
                continue
            # for length + 1
            if i >= max_len and s[i-max_len:i+1] == s[i-max_len:i+1][::-1]:
                start = i-max_len
                max_len += 1
        return s[start:start+max_len]




class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ('babad', 'bab'),
            ('cbbd', 'bb'),
            ('aaa', 'aaa'),
            ('bcada', 'ada'),
            ('eweasdsae', 'easdsae'),
            ('a', 'a')
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().longestPalindrome(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
