'''

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

'''
import unittest


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # from collections import Counter
        # i = len(s)
        # max_len = 0
        # while i >= 1:
        #     for j in range(len(s)-i+1):
        #         test_dict = Counter(s[j:j+i])
        #
        #         fre = max(test_dict.values())
        #         if fre >= 2:
        #             continue
        #         if len(test_dict) > max_len:
        #             # print(len(test_dict), test_dict)
        #             max_len = len(test_dict)
        #     i -= 1
        # return max_len
        # ---------------------------------------------------
        i = j = 0
        chars = []
        max_len = 0
        while j < len(s):
            if s[j] in chars:
                max_len = max(max_len, j - i)
                i += 1
                chars.pop(0)
            else:
                chars.append(s[j])
                j += 1
            # print(i, j, chars)

        return max(max_len, j - i)



class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            # ('a', 1),
            # ('abcabcbb', 3),
            # ('bbbbb', 1),
            ('pwwkew', 3),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().lengthOfLongestSubstring(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
