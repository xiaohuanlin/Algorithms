'''
You are given two positive integers n and target.

An integer is considered beautiful if the sum of its digits is less than or equal to target.

Return the minimum non-negative integer x such that n + x is beautiful. The input will be generated such that it is always possible to make n beautiful.



Example 1:

Input: n = 16, target = 6
Output: 4
Explanation: Initially n is 16 and its digit sum is 1 + 6 = 7. After adding 4, n becomes 20 and digit sum becomes 2 + 0 = 2. It can be shown that we can not make n beautiful with adding non-negative integer less than 4.
Example 2:

Input: n = 467, target = 6
Output: 33
Explanation: Initially n is 467 and its digit sum is 4 + 6 + 7 = 17. After adding 33, n becomes 500 and digit sum becomes 5 + 0 + 0 = 5. It can be shown that we can not make n beautiful with adding non-negative integer less than 33.
Example 3:

Input: n = 1, target = 1
Output: 0
Explanation: Initially n is 1 and its digit sum is 1, which is already smaller than or equal to target.


Constraints:

1 <= n <= 1012
1 <= target <= 150
The input will be generated such that it is always possible to make n beautiful.
'''
import unittest

from typing import *
class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        def convert_to_arr(num):
            res = []
            while num:
                res.append(num % 10)
                num //= 10
            return res[::-1]

        def arr_to_num(arr):
            res = 0
            for i in arr:
                res = 10 * res + i
            return res

        res = 0
        arr = convert_to_arr(n)
        for i in range(len(arr)):
            res += arr[i]
            if res > target:
                # need stop
                return 10**(len(arr) - i) - arr_to_num(arr[i:])
            elif res == target:
                if all(j == 0 for j in arr[i+1:]):
                    return 0
                # need stop
                return 10**(len(arr) - i) - arr_to_num(arr[i:])
        return 0




class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            # ((16, 6), 4),
            ((467, 6), 33),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().makeIntegerBeautiful(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
