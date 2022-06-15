'''
A string s is called happy if it satisfies the following conditions:

s only contains the letters 'a', 'b', and 'c'.
s does not contain any of "aaa", "bbb", or "ccc" as a substring.
s contains at most a occurrences of the letter 'a'.
s contains at most b occurrences of the letter 'b'.
s contains at most c occurrences of the letter 'c'.
Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.
Example 2:

Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It is the only correct answer in this case.
 

Constraints:

0 <= a, b, c <= 100
a + b + c > 0
'''
import unittest
from typing import *

from heapq import heappush, heappop

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq = []
        if a > 0:
            heappush(pq, (-a, 'a'))
        if b > 0:
            heappush(pq, (-b, 'b'))
        if c > 0:
            heappush(pq, (-c, 'c'))
        
        count = 0
        res = ""
        while pq:
            num, sym = heappop(pq)
            num = -num
            if count == 2 and res[-1] == sym:
                if not pq:
                    break
                else:
                    new_num, new_sym = heappop(pq)
                    new_num = -new_num
                    res += new_sym
                    count = 0
                    if new_num - 1 > 0:
                        heappush(pq, (-(new_num - 1), new_sym))
                    if num > 0:
                        heappush(pq, (-num, sym))
            else:
                res += sym
                if res[-1] == sym:
                    count += 1
                else:
                    count = 0
                if num - 1 > 0:
                    heappush(pq, (-(num - 1), sym))
        return res

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((1,1,7), "ccaccbcc"),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().longestDiverseString(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()