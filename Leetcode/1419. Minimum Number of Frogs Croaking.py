'''
You are given the string croakOfFrogs, which represents a combination of the string "croak" from different frogs, that is, multiple frogs can croak at the same time, so multiple "croak" are mixed.

Return the minimum number of different frogs to finish all the croaks in the given string.

A valid "croak" means a frog is printing five letters 'c', 'r', 'o', 'a', and 'k' sequentially. The frogs have to print all five letters to finish a croak. If the given string is not a combination of a valid "croak" return -1.

 

Example 1:

Input: croakOfFrogs = "croakcroak"
Output: 1 
Explanation: One frog yelling "croak" twice.
Example 2:

Input: croakOfFrogs = "crcoakroak"
Output: 2 
Explanation: The minimum number of frogs is two. 
The first frog could yell "crcoakroak".
The second frog could yell later "crcoakroak".
Example 3:

Input: croakOfFrogs = "croakcrook"
Output: -1
Explanation: The given string is an invalid combination of "croak" from different frogs.
 

Constraints:

1 <= croakOfFrogs.length <= 105
croakOfFrogs is either 'c', 'r', 'o', 'a', or 'k'.
'''

from typing import *

import unittest

class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        s = "croak"
        counts = [0 for _ in range(len(s))]
        counts[0] = 1
        res = 1
        
        for c in croakOfFrogs:
            if c not in s:
                return -1
            i = s.index(c)
            counts[i] -= 1
            counts[(i+1) % len(s)] += 1
            
            if counts[i] < 0:
                if i != 0:
                    return -1
                else:
                    counts[i] = 0
        return counts[0] if counts[0] == sum(counts) else -1
        
class TestSolution(unittest.TestCase):
    def test_case(self):
        examples = (
            (("croakcroak",),1),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().minNumberOfFrogs(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

