'''
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
'''

import unittest

class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # keep the same length 
        length = max(len(a), len(b))
        a = '0' * (length- len(a)) + a
        b = '0' * (length- len(b)) + b
        # add the binary
        c = []
        tmp = 0
        for i in range(length-1, -1, -1):
            a_i = int(a[i])
            b_i = int(b[i])
            if a_i + b_i + tmp >= 2:
                c.insert(0,(a_i + b_i + tmp)%2)
                tmp = 1
            else:
                c.insert(0,a_i + b_i + tmp)
                tmp = 0
        else:
            if tmp == 1:
                c = [1] + c
        result = ''.join([ str(num) for num in c])
        return result


class TestSolution(unittest.TestCase):

    def test_addBinary(self):
        examples = ((('11','1'), '100'),
                    (('1010','1011'), '10101'),
                    (('1111','1111'), '11110'),
        )
        for first,second in examples:
            self.assert_function(first, second)
        
    def assert_function(self, first, second):
        self.assertEqual(Solution().addBinary(*first), second)

unittest.main()