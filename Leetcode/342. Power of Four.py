'''

Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?

'''
import unittest


class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        if num <= 0 or num & 3 != 0:
            return False
        return self.isPowerOfFour(num >> 2)


class TestSolution(unittest.TestCase):

    def test_isPowerOfFour(self):
        examples = (
            (16, True),
            (0, False),
            (1, True),
            (6, False),
            (-4, False)
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().isPowerOfFour(first), second, msg="first: {}; second: {}".format(first, second))


unittest.main()