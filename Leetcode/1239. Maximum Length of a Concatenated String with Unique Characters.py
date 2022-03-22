'''
You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").
Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
Explanation: The only string in arr has all 26 characters.
 

Constraints:

1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lowercase English letters.
'''
from typing import *

import unittest


class Solution:
    max_length = 0

    def maxLength(self, arr: List[str]) -> int:

        def backtrace(index, choice, string_set):
            if len(arr[index]) != len(choice):
                return
            if choice & string_set:
                return

            string_set |= choice
            self.max_length = max(self.max_length, len(string_set))

            for i in range(index, len(arr)):
                backtrace(i, set(arr[i]), string_set)
            
            string_set -= choice

        for i in range(len(arr)):
            backtrace(i, set(arr[i]), set())
        return self.max_length


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((["aa","bb"],), 0),
            ((["un","iq","ue"],), 4),
            ((["cha","r","act","ers"],), 6),
            ((["abcdefghijklmnopqrstuvwxyz"],), 26),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maxLength(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
