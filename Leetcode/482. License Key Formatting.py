'''

You are given a license key represented as a string S which consists only alphanumeric character and dashes. The string is separated into N+1 groups by N dashes.

Given a number K, we would want to reformat the strings such that each group contains exactly K characters, except for the first group which could be shorter than K, but still must contain at least one character. Furthermore, there must be a dash inserted between two groups and all lowercase letters should be converted to uppercase.

Given a non-empty string S and a number K, format the string according to the rules described above.

Example 1:
Input: S = "5F3Z-2e-9-w", K = 4

Output: "5F3Z-2E9W"

Explanation: The string S has been split into two parts, each part has 4 characters.
Note that the two extra dashes are not needed and can be removed.
Example 2:
Input: S = "2-5g-3-J", K = 2

Output: "2-5G-3J"

Explanation: The string S has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.
Note:
The length of string S will not exceed 12,000, and K is a positive integer.
String S consists only of alphanumerical characters (a-z and/or A-Z and/or 0-9) and dashes(-).
String S is non-empty.

'''
import unittest


class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        s_list = [w.upper() for w in S if w != '-']
        start_num = len(s_list) % K
        group_list = [s_list[:start_num]] if start_num > 0 else []
        while start_num < len(s_list):
            group_list.append(s_list[start_num: start_num+K])
            start_num += K
            # print(group_list)
        return '-'.join((''.join(group) for group in group_list))


class TestSolution(unittest.TestCase):

    def test_licenseKeyFormatting(self):
        examples = (
            (("5F3Z-2e-9-w", 4), "5F3Z-2E9W"),
            (("2-5g-3-J", 2), "2-5G-3J"),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().licenseKeyFormatting(*first), second, msg="first: {}; second: {}".format(first, second))

unittest.main()