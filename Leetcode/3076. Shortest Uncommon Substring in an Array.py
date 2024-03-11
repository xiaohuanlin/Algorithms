'''
You are given an array arr of size n consisting of non-empty strings.

Find a string array answer of size n such that:

answer[i] is the shortest 
substring
 of arr[i] that does not occur as a substring in any other string in arr. If multiple such substrings exist, answer[i] should be the 
lexicographically smallest
. And if no such substring exists, answer[i] should be an empty string.
Return the array answer.

 

Example 1:

Input: arr = ["cab","ad","bad","c"]
Output: ["ab","","ba",""]
Explanation: We have the following:
- For the string "cab", the shortest substring that does not occur in any other string is either "ca" or "ab", we choose the lexicographically smaller substring, which is "ab".
- For the string "ad", there is no substring that does not occur in any other string.
- For the string "bad", the shortest substring that does not occur in any other string is "ba".
- For the string "c", there is no substring that does not occur in any other string.
Example 2:

Input: arr = ["abc","bcd","abcd"]
Output: ["","","abcd"]
Explanation: We have the following:
- For the string "abc", there is no substring that does not occur in any other string.
- For the string "bcd", there is no substring that does not occur in any other string.
- For the string "abcd", the shortest substring that does not occur in any other string is "abcd".
 

Constraints:

n == arr.length
2 <= n <= 100
1 <= arr[i].length <= 20
arr[i] consists only of lowercase English letters.
'''
import unittest

from typing import *


from collections import defaultdict

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        total = defaultdict(set)
        for i, s in enumerate(arr):
            for j in range(len(s)):
                for k in range(j, len(s)):
                    total[s[j:k+1]].add(i)

        res = []
        for i, s in enumerate(arr):
            for z in range(1, len(s)+1):
                current = None
                for j in range(len(s)):
                    if j + z > len(s):
                        continue
                    if len(total[s[j:j+z]]) == 1:
                        if current:
                            current = min(current, s[j:j+z])
                        else:
                            current = s[j:j+z]
                if current:
                    break
            res.append(current or "")
            current = None
        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((["cab","ad","bad","c"],),["ab","","ba",""]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().shortestSubstrings(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
