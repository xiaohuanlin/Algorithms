'''
You are given a 0-indexed string word of length n consisting of digits, and a positive integer m.

The divisibility array div of word is an integer array of length n such that:

div[i] = 1 if the numeric value of word[0,...,i] is divisible by m, or
div[i] = 0 otherwise.
Return the divisibility array of word.



Example 1:

Input: word = "998244353", m = 3
Output: [1,1,0,0,0,1,1,0,0]
Explanation: There are only 4 prefixes that are divisible by 3: "9", "99", "998244", and "9982443".
Example 2:

Input: word = "1010", m = 10
Output: [0,1,0,1]
Explanation: There are only 2 prefixes that are divisible by 10: "10", and "1010".


Constraints:

1 <= n <= 105
word.length == n
word consists of digits from 0 to 9
1 <= m <= 109
'''
import unittest

from typing import *

class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        res = []
        remain = 0
        for i in range(len(word)):
            remain = (remain * 10 + int(word[i]) % m) % m
            if remain % m == 0:
                remain = 0
                res.append(1)
            else:
                res.append(0)

        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("998244353", 3), [1,1,0,0,0,1,1,0,0]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().divisibilityArray(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
