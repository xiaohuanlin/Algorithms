'''

Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.

'''
import unittest


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        alph_list = [chr(code) for code in range(ord('A'), ord('['))] + [chr(code) for code in range(ord('a'), ord('{'))]
        # print(alph_list)
        count_list = [s.count(word) for word in alph_list]
        # print(count_list)
        sum_count = 0
        for count in count_list:
            if count % 2 == 0:
                sum_count += count
            else:
                sum_count += count - 1
        return sum_count + 1 if any(count % 2 == 1 for count in count_list) else sum_count


class TestSolution(unittest.TestCase):

    def test_longestPalindrome(self):
        examples = (
            ('abccccdd', 7),
            ('abcd', 1),
            ('ccc', 3),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().longestPalindrome(first), second, msg="first: {}; second: {}".format(first, second))


unittest.main()