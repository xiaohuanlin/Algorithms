'''
You are given a 2D string array responses where each responses[i] is an array of strings representing survey responses from the ith day.

Return the most common response across all days after removing duplicate responses within each responses[i]. If there is a tie, return the lexicographically smallest response.

 

Example 1:

Input: responses = [["good","ok","good","ok"],["ok","bad","good","ok","ok"],["good"],["bad"]]

Output: "good"

Explanation:

After removing duplicates within each list, responses = [["good", "ok"], ["ok", "bad", "good"], ["good"], ["bad"]].
"good" appears 3 times, "ok" appears 2 times, and "bad" appears 2 times.
Return "good" because it has the highest frequency.
Example 2:

Input: responses = [["good","ok","good"],["ok","bad"],["bad","notsure"],["great","good"]]

Output: "bad"

Explanation:

After removing duplicates within each list we have responses = [["good", "ok"], ["ok", "bad"], ["bad", "notsure"], ["great", "good"]].
"bad", "good", and "ok" each occur 2 times.
The output is "bad" because it is the lexicographically smallest amongst the words with the highest frequency.
 

Constraints:

1 <= responses.length <= 1000
1 <= responses[i].length <= 1000
1 <= responses[i][j].length <= 10
responses[i][j] consists of only lowercase English letters
'''
import unittest

from typing import *

from collections import defaultdict


class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        m = defaultdict(int)
        max_v = float('-inf')
        max_l = []
        for r in responses:
            for s in set(r):
                m[s] += 1
                if m[s] > max_v:
                    max_v = m[s]
                    max_l = [s]
                elif m[s] == max_v:
                    max_l.append(s)
        return sorted(max_l)[0]


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([
                ["good", "ok", "good", "ok"],
                ["ok", "bad", "good", "ok", "ok"],
                ["good"],
                ["bad"]
            ],), "good"),
            (([
                ["good", "ok", "good"],
                ["ok", "bad"],
                ["bad", "notsure"],
                ["great", "good"]
            ],), "bad")
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().findCommonResponse(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

