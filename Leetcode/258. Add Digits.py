'''
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2.
             Since 2 has only one digit, return it.
Follow up:
Could you do it without any loop/recursion in O(1) runtime?
'''
import unittest


class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # if num < 10:
        #     return num
        # num_sum = 0
        # while num != 0:
        #     num_sum += num % 10
        #     num /= 10
        # return self.addDigits(num_sum)
        if num == 0:
            return 0
        return num % 9 if num % 9 != 0 else 9


class TestSolution(unittest.TestCase):

    def test_addDigits(self):
        examples = (
            (38, 2),
            (11, 2),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().addDigits(first), second)


unittest.main()