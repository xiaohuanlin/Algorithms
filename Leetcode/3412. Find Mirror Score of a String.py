'''
You are given a string s.

We define the mirror of a letter in the English alphabet as its corresponding letter when the alphabet is reversed. For example, the mirror of 'a' is 'z', and the mirror of 'y' is 'b'.

Initially, all characters in the string s are unmarked.

You start with a score of 0, and you perform the following process on the string s:

Iterate through the string from left to right.
At each index i, find the closest unmarked index j such that j < i and s[j] is the mirror of s[i]. Then, mark both indices i and j, and add the value i - j to the total score.
If no such index j exists for the index i, move on to the next index without making any changes.
Return the total score at the end of the process.

 

Example 1:

Input: s = "aczzx"

Output: 5

Explanation:

i = 0. There is no index j that satisfies the conditions, so we skip.
i = 1. There is no index j that satisfies the conditions, so we skip.
i = 2. The closest index j that satisfies the conditions is j = 0, so we mark both indices 0 and 2, and then add 2 - 0 = 2 to the score.
i = 3. There is no index j that satisfies the conditions, so we skip.
i = 4. The closest index j that satisfies the conditions is j = 1, so we mark both indices 1 and 4, and then add 4 - 1 = 3 to the score.
Example 2:

Input: s = "abcdef"

Output: 0

Explanation:

For each index i, there is no index j that satisfies the conditions.

 

Constraints:

1 <= s.length <= 105
s consists only of lowercase English letters.
'''
import unittest

from typing import *

from bisect import bisect
from collections import defaultdict


class Solution:
    def calculateScore(self, s: str) -> int:
        index_map = defaultdict(list)
        for i in range(len(s)):
            index_map[s[i]].append(i)
        
        visited = set()
        res = 0
        for i in range(len(s)):
            if i in visited:
                continue
            mirror = chr(25 - (ord(s[i]) - ord('a')) + ord('a'))
            if not index_map[mirror]:
                continue
            j_index = bisect(index_map[mirror], i)
            if j_index == 0:
                continue
            j = index_map[mirror][j_index-1]
            index_map[mirror].pop(j_index-1)
            index_map[s[i]].remove(i)
            visited.add(j)
            visited.add(i)
            res += i - j
        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("eockppxdqclkhjgvnw",),50),
            # (("aczzx",),5),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().calculateScore(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
