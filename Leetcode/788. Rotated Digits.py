'''

X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from X.  Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.

Now given a positive number N, how many numbers X from 1 to N are good?

Example:
Input: 10
Output: 4
Explanation:
There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
Note:

N  will be in range [1, 10000].

'''
import unittest


class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        # dp[i] = 0, invalid number
        # dp[i] = 1, valid and same number
        # dp[i] = 2, valid and different number
        dp = [0] * (N+1)
        count = 0
        for i in range(N+1):
            if i < 10:
                if i == 0 or i == 1 or i == 8:
                    dp[i] = 1
                elif i == 2 or i == 5 or i == 6 or i == 9:
                    dp[i] = 2
                    count += 1
            else:
                a, b = dp[i//10], dp[i % 10]
                if a == 1 and b == 1:
                    dp[i] = 1
                elif a >= 1 and b >= 1:
                    dp[i] = 2
                    count += 1
        return count


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (10, 4),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().rotatedDigits(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
