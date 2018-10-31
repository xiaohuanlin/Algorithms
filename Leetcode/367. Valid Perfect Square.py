'''

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false

'''
import unittest


class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # if num == 1:
        #     return True
        # start = 0
        # end = num
        #
        # while end - start > 1:
        #     guess = int((start + end) / 2)
        #     value = guess ** 2
        #     if value > num:
        #         end = guess
        #     elif value < num:
        #         start = guess
        #     else:
        #         return True
        # return False
# for newton method
        guess = num

        while True:
            print(guess)
            if guess ** 2 == num:
                return True
            if guess ** 2 < num:
                return False
            guess = int((guess ** 2 + num) / (2 * guess))


class TestSolution(unittest.TestCase):

    def test_isPerfectSquare(self):
        examples = (
            (16, True),
            (1, True),
            (5, False),
            (14, False)
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().isPerfectSquare(first), second, msg="first: {}; second: {}".format(first, second))


unittest.main()