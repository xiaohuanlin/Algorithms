'''
Reverse bits of a given 32 bits unsigned integer.

Example:

Input: 43261596
Output: 964176192
Explanation: 43261596 represented in binary as 00000010100101000001111010011100, 
             return 964176192 represented in binary as 00111001011110000010100101000000.
Follow up:
If this function is called many times, how would you optimize it?
'''
import unittest

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):

        sum_rem = 0

        for _ in range(32):
            n, rem = divmod(n, 2)
            sum_rem = sum_rem * 2 + rem
        return sum_rem
        

class TestSolution(unittest.TestCase):

    def test_reverseBits(self):
        examples = (
            (43261596, 964176192),
        )
        for first,second in examples:
            self.assert_function(first, second)
        
    def assert_function(self, first, second):
        self.assertEqual(Solution().reverseBits(first), second)

unittest.main()