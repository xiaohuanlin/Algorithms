'''
Given two integers num and k, consider a set of positive integers with the following properties:

The units digit of each integer is k.
The sum of the integers is num.
Return the minimum possible size of such a set, or -1 if no such set exists.

Note:

The set can contain multiple instances of the same integer, and the sum of an empty set is considered 0.
The units digit of a number is the rightmost digit of the number.
 

Example 1:

Input: num = 58, k = 9
Output: 2
Explanation:
One valid set is [9,49], as the sum is 58 and each integer has a units digit of 9.
Another valid set is [19,39].
It can be shown that 2 is the minimum possible size of a valid set.
Example 2:

Input: num = 37, k = 2
Output: -1
Explanation: It is not possible to obtain a sum of 37 using only integers that have a units digit of 2.
Example 3:

Input: num = 0, k = 7
Output: 0
Explanation: The sum of an empty set is considered 0.
 

Constraints:

0 <= num <= 3000
0 <= k <= 9
'''
import unittest

from typing import *

class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        maps = {
            0: {
                0: 0
            },
            1: {
                0: 10,
                1: 1,
                2: 2,
                3: 3,
                4: 4,
                5: 5,
                6: 6,
                7: 7,
                8: 8,
                9: 9
            },
            2: {
                0: 10,
                2: 2,
                4: 4,
                6: 6,
                8: 8
            },
            3: {
                0: 30,
                1: 21,
                2: 12,
                3: 3,
                4: 24,
                5: 15,
                6: 6,
                7: 27,
                8: 18,
                9: 9
            },
            4: {
                0: 20,
                2: 12,
                4: 4,
                6: 16,
                8: 8,
            },
            5: {
                0: 10,
                5: 5,
            },
            6: {
                0: 30,
                2: 12,
                4: 24,
                6: 6,
                8: 18
            },
            7: {
                0: 70,
                1: 21,
                2: 42,
                3: 63,
                4: 14,
                5: 35,
                6: 56,
                7: 7,
                8: 28,
                9: 49
            },
            8: {
                0: 40,
                2: 32,
                4: 24,
                6: 16,
                8: 8
            },
            9: {
                0: 90,
                1: 81,
                2: 72,
                3: 63,
                4: 54,
                5: 45,
                6: 36,
                7: 27,
                8: 18,
                9: 9
            }
        }
        if num == 0:
            return 0
        if k == 0:
            if num % 10 == 0:
                return 1
            return -1

        target = maps[k].get(num % 10)
        if target is not None and num >= target:
            return target // k
        return -1


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((37, 2), -1),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().minimumNumbers(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
