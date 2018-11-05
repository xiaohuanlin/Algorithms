'''

You are given a string representing an attendance record for a student. The record only contains the following three characters:
'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

Example 1:
Input: "PPALLP"
Output: True
Example 2:
Input: "PPALLL"
Output: False

'''
import unittest


class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a_count = 0
        l_count = 0
        for word in s:
            if word == 'L':
                l_count += 1
            else:
                l_count = 0

            if l_count > 2:
                return False
            if word == 'A':
                a_count += 1
        return a_count <= 1







class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ('PPALLP', True),
            ('PPALLL', False),
            ("LALL", True),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().checkRecord(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
