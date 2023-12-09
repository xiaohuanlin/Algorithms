'''
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

 

Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
 

Constraints:

The given address is a valid IPv4 address.
'''

from typing import *
import unittest


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("255.100.50.0", ), "255[.]100[.]50[.]0"),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().defangIPaddr(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()