'''
You are given a binary string s. In one second, all occurrences of "01" are simultaneously replaced with "10". This process repeats until no occurrences of "01" exist.

Return the number of seconds needed to complete this process.



Example 1:

Input: s = "0110101"
Output: 4
Explanation:
After one second, s becomes "1011010".
After another second, s becomes "1101100".
After the third second, s becomes "1110100".
After the fourth second, s becomes "1111000".
No occurrence of "01" exists any longer, and the process needed 4 seconds to complete,
so we return 4.
Example 2:

Input: s = "11100"
Output: 0
Explanation:
No occurrence of "01" exists in s, and the processes needed 0 seconds to complete,
so we return 0.


Constraints:

1 <= s.length <= 1000
s[i] is either '0' or '1'.


Follow up:

Can you solve this problem in O(n) time complexity?
'''
import unittest

from typing import *
class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        arr = [-1] + [i for i in range(len(s)) if s[i] == '1']

        total = (len(arr) - 3) * len(arr) // 2
        cnt = 0
        while sum(arr) != total:
            for i in range(1, len(arr))[::-1]:
                if arr[i-1] != arr[i] - 1:
                    arr[i] -= 1
            cnt += 1
        return cnt




class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("0110101",),4),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().secondsToRemoveOccurrences(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
