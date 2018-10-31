'''

Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:

Input:
3

Output:
3
Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.

'''
import unittest


class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        num, length, size = 1, 1, 9
        while n > length*size:
            n -= length*size
            num += size
            length += 1
            size *= 10

        return int(str(num+((n-1)//length))[(n-1) % length])


class TestSolution(unittest.TestCase):

    def test_findNthDigit(self):
        examples = (
            (1, 1),
            (3, 3),
            (10, 1),
            (11, 0),
            (1000, 3),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().findNthDigit(first), second, msg="first: {}; second: {}".format(first, second))


unittest.main()