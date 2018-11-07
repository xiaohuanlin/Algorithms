'''

A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example 1:
Input:
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
Note:

The boundaries of each input argument are 1 <= left <= right <= 10000.

'''
import unittest


class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        return [i for i in range(left, right+1) if self.is_divide(i)]


    def is_divide(self, num):
        try:
            if all(num % int(n) == 0 for n in str(num)):
                return True
        except ZeroDivisionError:
            return False


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((1,22), [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().selfDividingNumbers(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
