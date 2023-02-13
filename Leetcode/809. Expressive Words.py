'''
Sometimes people repeat letters to represent extra feeling. For example:

"hello" -> "heeellooo"
"hi" -> "hiiii"
In these strings like "heeellooo", we have groups of adjacent letters that are all the same: "h", "eee", "ll", "ooo".

You are given a string s and an array of query strings words. A query word is stretchy if it can be made to be equal to s by any number of applications of the following extension operation: choose a group consisting of characters c, and add some number of characters c to the group so that the size of the group is three or more.

For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get "helloo" since the group "oo" has a size less than three. Also, we could do another extension like "ll" -> "lllll" to get "helllllooo". If s = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = s.
Return the number of query strings that are stretchy.

 

Example 1:

Input: s = "heeellooo", words = ["hello", "hi", "helo"]
Output: 1
Explanation: 
We can extend "e" and "o" in the word "hello" to get "heeellooo".
We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.
Example 2:

Input: s = "zzzzzyyyyy", words = ["zzyy","zy","zyy"]
Output: 3
'''

from typing import *
import unittest


class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        res = 0
        for word in words:
            i = 0
            j = 0
            while i < len(s) or j < len(word):
                i_start = i
                while i + 1 < len(s) and s[i] == s[i+1]:
                    i += 1
                i_count = i - i_start + 1

                j_start = j
                while j + 1 < len(word) and word[j] == word[j+1]:
                    j += 1
                j_count = j - j_start + 1
                if (i >= len(s) and j < len(word)) or (i < len(s) and j >= len(word)):
                    break
                if (s[i] != word[j]) or (i_count < 3 and i_count != j_count) or (i_count >= 3 and i_count < j_count):
                    break
                i += 1
                j += 1
            else:
                res += 1
        return res
        

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("heeellooo", ["hello", "hi", "helo"]), 1),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().expressiveWords(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()