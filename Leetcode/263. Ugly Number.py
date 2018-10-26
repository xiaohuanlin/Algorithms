'''
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example 1:

Input: 6
Output: true
Explanation: 6 = 2 × 3
Example 2:

Input: 8
Output: true
Explanation: 8 = 2 × 2 × 2
Example 3:

Input: 14
Output: false
Explanation: 14 is not ugly since it includes another prime factor 7.
Note:

1 is typically treated as an ugly number.
Input is within the 32-bit signed integer range: [−231,  231 − 1].
'''
import unittest


class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        for num_int in (5, 3, 2):
            while True:
                if num == 0:
                    break
                if num == 1:
                    return True
                res = num % num_int
                if res > 0:
                    break
                num = num / num_int
        return False


class TestSolution(unittest.TestCase):

    def test_isUgly(self):
        examples = (
            (6, True),
            (8, True),
            (14, False),
            (0, False),
            (1, True)
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().isUgly(first), second, msg="first: {}; second: {}".format(first, second))


unittest.main()