'''
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"

'''

import unittest

class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        string = '1'
        i = 1
        while i < n:
            string = self.generate_str(string)
            i += 1
        return string
        
    def generate_str(self, string):
        start = 0
        group = []
        for i in range(len(string)-1):
            if string[i] != string[i+1]:
                group.extend((str(i+1-start), string[i]))
                start = i+1
        else:
            group.extend((str(len(string)-start), string[-1]))
        return ''.join(group)



class TestSolution(unittest.TestCase):

    def test_countAndSay(self):
        examples = ((1, "1"),
                    (4, "1211"),
                    (5, "111221"),
        )
        for first,second in examples:
            self.assert_function(first, second)
        
    def assert_function(self, first, second):
        self.assertEqual(Solution().countAndSay(first), second)

unittest.main()