'''

We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
Example:
Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14
Note: The input number n will not exceed 100,000,000. (1e8)

'''
import unittest


class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
        from math import sqrt
        find_num = int(sqrt(num))
        result = [1]
        while find_num > 1:
            pair_num = num / find_num
            print(pair_num, find_num)
            if int(pair_num) == pair_num:
                result.extend([find_num, pair_num])
            find_num -= 1
        return sum(result) == num


class TestSolution(unittest.TestCase):

    def test_checkPerfectNumber(self):
        examples = (
            # (28, True),
            # (6, True),
            (1, False),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().checkPerfectNumber(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()