'''
You are given a string s that consists of only digits.

Check if we can split s into two or more non-empty substrings such that the numerical values of the substrings are in descending order and the difference between numerical values of every two adjacent substrings is equal to 1.

For example, the string s = "0090089" can be split into ["0090", "089"] with numerical values [90,89]. The values are in descending order and adjacent values differ by 1, so this way is valid.
Another example, the string s = "001" can be split into ["0", "01"], ["00", "1"], or ["0", "0", "1"]. However all the ways are invalid because they have numerical values [0,1], [0,1], and [0,0,1] respectively, all of which are not in descending order.
Return true if it is possible to split s​​​​​​ as described above, or false otherwise.

A substring is a contiguous sequence of characters in a string.



Example 1:

Input: s = "1234"
Output: false
Explanation: There is no valid way to split s.
Example 2:

Input: s = "050043"
Output: true
Explanation: s can be split into ["05", "004", "3"] with numerical values [5,4,3].
The values are in descending order with adjacent values differing by 1.
Example 3:

Input: s = "9080701"
Output: false
Explanation: There is no valid way to split s.


Constraints:

1 <= s.length <= 20
s only consists of digits.
'''
import unittest

from typing import *

class Solution:
    def splitString(self, s: str) -> bool:
        def dfs(i, target):
            for j in range(i + 1, len(s) + 1):
                num = int(s[i:j])
                if num > target:
                    return False
                if num == target:
                    if j == len(s) or dfs(j, num - 1):
                        return True
            return False

        for i in range(1, len(s)):
            if dfs(i, int(s[:i]) - 1):
                return True
        return False


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("1234",),False),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().splitString(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
