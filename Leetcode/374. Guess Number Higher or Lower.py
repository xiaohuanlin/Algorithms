'''

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
Example :

Input: n = 10, pick = 6
Output: 6

'''
import unittest


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):
#     _guess = 6
#     if num < _guess:
#         return -1
#     elif num > _guess:
#         return 1
#     return 0


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
        while low <= high:
            mid = (low + high)//2
            res = guess(mid)
            if res == 0 :
                return mid
            elif res == -1:
                high = mid - 1
            else:
                low = mid + 1


# class TestSolution(unittest.TestCase):
#
#     def test_guessNumber(self):
#         examples = (
#             (10, 6),
#         )
#         for first, second in examples:
#             self.assert_function(first, second)
#
#     def assert_function(self, first, second):
#         self.assertEqual(Solution().guessNumber(first), second, msg="first: {}; second: {}".format(first, second))
#
#
# unittest.main()