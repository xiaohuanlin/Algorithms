'''

Given a positive integer N, find and return the longest distance between two consecutive 1's in the binary representation of N.

If there aren't two consecutive 1's, return 0.



Example 1:

Input: 22
Output: 2
Explanation:
22 in binary is 0b10110.
In the binary representation of 22, there are three ones, and two consecutive pairs of 1's.
The first consecutive pair of 1's have distance 2.
The second consecutive pair of 1's have distance 1.
The answer is the largest of these two distances, which is 2.
Example 2:

Input: 5
Output: 2
Explanation:
5 in binary is 0b101.
Example 3:

Input: 6
Output: 1
Explanation:
6 in binary is 0b110.
Example 4:

Input: 8
Output: 0
Explanation:
8 in binary is 0b1000.
There aren't any consecutive pairs of 1's in the binary representation of 8, so we return 0.


Note:

1 <= N <= 10^9

'''
import unittest


class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        i = 0
        max_dis = 0
        pre = 0
        count = 0
        # print(bin(N))
        while N > 0:
            N, res = N >> 1, N & 1
            if res == 1:
                dis = i - pre
                if dis > max_dis and count > 0:
                    max_dis = dis
                # print(i, pre, dis)
                pre = i
                count += 1
            i += 1
        return max_dis if count > 1 else 0


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (22, 2),
            (5, 2),
            (6, 1),
            (8, 0),
            (12, 1),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().binaryGap(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
