'''
You are given an array of strings message and an array of strings bannedWords.

An array of words is considered spam if there are at least two words in it that exactly match any word in bannedWords.

Return true if the array message is spam, and false otherwise.

 

Example 1:

Input: message = ["hello","world","leetcode"], bannedWords = ["world","hello"]

Output: true

Explanation:

The words "hello" and "world" from the message array both appear in the bannedWords array.

Example 2:

Input: message = ["hello","programming","fun"], bannedWords = ["world","programming","leetcode"]

Output: false

Explanation:

Only one word from the message array ("programming") appears in the bannedWords array.

 

Constraints:

1 <= message.length, bannedWords.length <= 105
1 <= message[i].length, bannedWords[i].length <= 15
message[i] and bannedWords[i] consist only of lowercase English letters.
'''
import unittest

from typing import *


class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        banned = set(bannedWords)
        c = 0
        for m in message:
            if m in banned:
                c += 1
                if c == 2:
                    break

        return c >= 2


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((["hello","world","leetcode"], ["world","hello"],), True),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().reportSpam(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
