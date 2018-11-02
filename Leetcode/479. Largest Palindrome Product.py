'''

Find the largest palindrome made from the product of two n-digit numbers.

Since the result could be very large, you should return the largest palindrome mod 1337.

Example:

Input: 2

Output: 987

Explanation: 99 x 91 = 9009, 9009 % 1337 = 987

Note:

The range of n is [1,8].

'''
import unittest


class Solution:
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
    #     max_value = 10 ** n - 1
    #     min_value = 10 ** (n-1)
    #     for num in range(max_value ** 2, 0, -1):
    #         if self.is_pa(num):
    #             for i in range(max_value, min_value-1, -1):
    #                 j = num / i
    #                 if min_value <= j <= max_value and j == int(j):
    #                     return num % 1337
    #
    # def is_pa(self, num):
    #     return str(num) == str(num)[::-1]
    # --------------------
    # https://leetcode.com/problems/largest-palindrome-product/discuss/96305/Python-Solution-Using-Math-In-48ms
    # pa = a * 10**n + b
    # a = b[::-1]
    # pa = (10**n -i)(10**n-j)
    # so get:
    #     a = 10**n - sum_num
    #     b = sum_num*i - i**2
    # because i should be a inter, so (sum_num**2 - 4b)**0.5 also is a inter

        if n == 1:
            return 9
        if n == 2:
            return 987
        for sum_num in range(2, 9*10**(n-1)):
            a = (10**n)-sum_num
            b = int(str(a)[::-1])
            if sum_num**2-4*b < 0:
                continue
            if (sum_num**2-4*b)**.5 == int((sum_num**2-4*b)**.5):
                return (b+10**n*(10**n-sum_num)) % 1337


class TestSolution(unittest.TestCase):

    def test_largestPalindrome(self):
        examples = (
            (1, 9),
            (2, 987),
            (3, 123),
            (4, 597),
            (5, 677),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().largestPalindrome(first), second, msg="first: {}; second: {}".format(first, second))

unittest.main()