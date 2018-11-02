'''

Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:

Input: "Hello, my name is John"
Output: 5

'''
import unittest


class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """

        section = []
        sections = []
        for word in s+' ':
            if word == ' ':
                if section:
                    sections.append(section)
                    section = []
            else:
                section.append(word)
        return len(sections)


class TestSolution(unittest.TestCase):

    def test_countSegments(self):
        examples = (
            ('Hello, my name is John', 5),
            ('s', 1),
            ('     ', 0)
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().countSegments(first), second, msg="first: {}; second: {}".format(first, second))


unittest.main()