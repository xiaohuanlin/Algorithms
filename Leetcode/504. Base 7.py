'''

Given an integer, return its base 7 string representation.

Example 1:
Input: 100
Output: "202"
Example 2:
Input: -7
Output: "-10"
Note: The input will be in range of [-1e7, 1e7].

'''
import unittest


class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        result = []
        flag = True if num > 0 else False
        num = abs(num)
        while num > 0:
            num, res = num // 7, num % 7
            result.append(str(res))
        if not flag:
            result.append('-')
        return ''.join(result[::-1])


class TestSolution(unittest.TestCase):

    def test_convertToBase7(self):
        examples = (
            (100, '202'),
            (-7, '-10'),
            (0, '0')
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().convertToBase7(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()