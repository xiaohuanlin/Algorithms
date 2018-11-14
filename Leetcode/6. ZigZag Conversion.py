'''

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I

'''
import unittest


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        from collections import OrderedDict
        str_dict = OrderedDict({i: [] for i in range(numRows)})
        direct = -1
        pre_i = 1
        for j in range(len(s)):
            pre_i = pre_i + direct
            # print(pre_i)
            str_dict[pre_i].append(s[j])
            if j % (numRows-1) == 0:
                direct *= -1
        return ''.join([''.join(value) for value in str_dict.values()])


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (('PAYPALISHIRING', 3), 'PAHNAPLSIIGYIR'),
            (('PAYPALISHIRING', 4), 'PINALSIGYAHRPI'),
            (('A', 1), 'A'),
            (('AB', 2), 'AB'),
            ((' ', 2), ' '),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().convert(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
