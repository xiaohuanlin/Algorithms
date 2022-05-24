'''
You are given a string of digits num, such as "123456579". We can split it into a Fibonacci-like sequence [123, 456, 579].

Formally, a Fibonacci-like sequence is a list f of non-negative integers such that:

0 <= f[i] < 231, (that is, each integer fits in a 32-bit signed integer type),
f.length >= 3, and
f[i] + f[i + 1] == f[i + 2] for all 0 <= i < f.length - 2.
Note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number 0 itself.

Return any Fibonacci-like sequence split from num, or return [] if it cannot be done.

 

Example 1:

Input: num = "1101111"
Output: [11,0,11,11]
Explanation: The output [110, 1, 111] would also be accepted.
Example 2:

Input: num = "112358130"
Output: []
Explanation: The task is impossible.
Example 3:

Input: num = "0123"
Output: []
Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.
 

Constraints:

1 <= num.length <= 200
num contains only digits.
'''
import unittest

from typing import *

class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        selected = []

        def dfs(index):
            if index == len(num):
                if len(selected) > 2:
                    return True
                return False
            
            for i in range(index+1, len(num)+1):
                v = int(num[index:i])
                if len(selected) > 1 and selected[-2] + selected[-1] != v:
                    continue
                if str(v) != num[index:i]:
                    continue
                if v >= (1 << 31):
                    continue
                    
                selected.append(v)
                if dfs(i):
                    return True
                selected.pop()
        
        dfs(0)
        return selected

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("1101111",), [11,0,11,11]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().splitIntoFibonacci(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()