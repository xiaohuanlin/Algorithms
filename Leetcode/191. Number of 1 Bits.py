'''
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Example 1:

Input: 11
Output: 3
Explanation: Integer 11 has binary representation 00000000000000000000000000001011 
Example 2:

Input: 128
Output: 1
Explanation: Integer 128 has binary representation 00000000000000000000000010000000
'''
import unittest

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        # count = 0

        # for _ in range(32):
        #     n, rem = divmod(n, 2)
        #     if rem == 1:
        #         count += 1
        # return count
        # ---------------------------
        count = 0

        while n > 0:
            if n & 1:
                count += 1
            n >>= 1

        return count


class TestSolution(unittest.TestCase):

    def test_hammingWeight(self):
        examples = (
            (11, 3),
        )
        for first,second in examples:
            self.assert_function(first, second)
        
    def assert_function(self, first, second):
        self.assertEqual(Solution().hammingWeight(first), second)

unittest.main()