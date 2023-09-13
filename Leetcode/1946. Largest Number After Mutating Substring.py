'''
You are given a string num, which represents a large integer. You are also given a 0-indexed integer array change of length 10 that maps each digit 0-9 to another digit. More formally, digit d maps to digit change[d].

You may choose to mutate a single substring of num. To mutate a substring, replace each digit num[i] with the digit it maps to in change (i.e. replace num[i] with change[num[i]]).

Return a string representing the largest possible integer after mutating (or choosing not to) a single substring of num.

A substring is a contiguous sequence of characters within the string.



Example 1:

Input: num = "132", change = [9,8,5,0,3,6,4,2,6,8]
Output: "832"
Explanation: Replace the substring "1":
- 1 maps to change[1] = 8.
Thus, "132" becomes "832".
"832" is the largest number that can be created, so return it.
Example 2:

Input: num = "021", change = [9,4,3,5,7,2,1,9,0,6]
Output: "934"
Explanation: Replace the substring "021":
- 0 maps to change[0] = 9.
- 2 maps to change[2] = 3.
- 1 maps to change[1] = 4.
Thus, "021" becomes "934".
"934" is the largest number that can be created, so return it.
Example 3:

Input: num = "5", change = [1,4,7,5,3,2,5,6,9,4]
Output: "5"
Explanation: "5" is already the largest number that can be created, so return it.


Constraints:

1 <= num.length <= 105
num consists of only digits 0-9.
change.length == 10
0 <= change[d] <= 9
'''

from typing import *

import unittest


class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        s = []
        i = 0
        first = True
        while i < len(num):
            map_i = int(num[i])
            if first:
                delta = 0
                while i < len(num) and change[map_i] >= int(num[i]):
                    delta += (change[map_i] - int(num[i]))
                    s.append(str(change[map_i]))
                    i += 1
                    if i >= len(num):
                        break
                    map_i = int(num[i])
                    first = False

                if delta == 0:
                    # all are same num
                    first = True

            if i >= len(num):
                break
            s.append(num[i])
            i += 1
        return "".join(s)


class TestSolution(unittest.TestCase):
    def test_case(self):
        examples = (
            (("334111", [0,9,2,3,3,2,5,5,5,5]), "334999"),
            (("214010", [6,7,9,7,4,0,3,4,4,7]), "974676"),
            (("330", [9,3,6,3,7,3,1,4,5,8]), "339"),
            (("021", [9,4,3,5,7,2,1,9,0,6]), "934"),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maximumNumber(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

