'''

Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Note:
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.
Example 1:
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
Example 2:
Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.

'''
import unittest


class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        # new_num = 0
        # num_list = []
        # while num > 0:
        #     num, dig = num >> 1, num & 1
        #     num_list.append(dig)
        # while num_list:
        #     dig = num_list.pop()
        #     new_num = new_num * 2 + int(dig != 1)
        # return new_num
        # --------------
        count = 0
        ori_num = num
        while num > 0:
            num = num >> 1
            count += 1
        return 2**count - 1 - ori_num



class TestSolution(unittest.TestCase):

    def test_findComplement(self):
        examples = (
            (5, 2),
            (1, 0),
            (2, 1),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().findComplement(first), second, msg="first: {}; second: {}".format(first, second))

unittest.main()