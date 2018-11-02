'''

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
Seen this question in a real interview before?

'''
import unittest


class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # m = x ^ y
        # count = 0
        # while m > 0:
        #     if m & 1:
        #         count += 1
        #     m = m >> 1
        # return count
        # ------------------------
        x_list = bin(x)[2:]
        y_list = bin(y)[2:]
        count = 0

        delta = len(x_list) - len(y_list)
        if delta > 0:
            y_list = '0' * delta + y_list
        else:
            x_list = '0' * (-delta) + x_list
        for x,y in zip(x_list, y_list):
            if x != y:
                count += 1
        return count


class TestSolution(unittest.TestCase):

    def test_hammingDistance(self):
        examples = (
            ((1, 4), 2),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().hammingDistance(*first), second, msg="first: {}; second: {}".format(first, second))

unittest.main()