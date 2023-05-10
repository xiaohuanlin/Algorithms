'''
Given an integer array queries and a positive integer intLength, return an array answer where answer[i] is either the queries[i]th smallest positive palindrome of length intLength or -1 if no such palindrome exists.

A palindrome is a number that reads the same backwards and forwards. Palindromes cannot have leading zeros.

 

Example 1:

Input: queries = [1,2,3,4,5,90], intLength = 3
Output: [101,111,121,131,141,999]
Explanation:
The first few palindromes of length 3 are:
101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 202, ...
The 90th palindrome of length 3 is 999.
Example 2:

Input: queries = [2,4,6], intLength = 4
Output: [1111,1331,1551]
Explanation:
The first six palindromes of length 4 are:
1001, 1111, 1221, 1331, 1441, and 1551.
 

Constraints:

1 <= queries.length <= 5 * 104
1 <= queries[i] <= 109
1 <= intLength <= 15
'''
import unittest

from typing import *

from math import ceil
class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        length = ceil(intLength / 2)
        start = 10 ** (length - 1)
        res = []
        for q in queries:
            if q + start > start * 10:
                res.append(-1)
                continue
            pre = str(q + start - 1)
            suf = pre[:intLength - len(pre)][::-1]
            res.append(int(pre + suf))
        return res

        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,2,3,4,5,90],3),[101,111,121,131,141,999]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().kthPalindrome(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
