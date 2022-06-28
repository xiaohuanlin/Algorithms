'''
A string s is called good if there are no two different characters in s that have the same frequency.

Given a string s, return the minimum number of characters you need to delete to make s good.

The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

 

Example 1:

Input: s = "aab"
Output: 0
Explanation: s is already good.
Example 2:

Input: s = "aaabbbcc"
Output: 2
Explanation: You can delete two 'b's resulting in the good string "aaabcc".
Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".
Example 3:

Input: s = "ceabaacb"
Output: 2
Explanation: You can delete both 'c's resulting in the good string "eabaab".
Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).
 

Constraints:

1 <= s.length <= 105
s contains only lowercase English letters.
'''
import unittest
from typing import *

class Solution:
    def minDeletions(self, s: str) -> int:
        c = Counter(s)        
        l = sorted(c.values())
        res = 0
        target = float('inf')
        for i in range(len(l))[::-1]:
            target = max(0, min(l[i], target - 1))
            diff = l[i] - target
            res += diff
        return res

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("aaabbbcc",),2),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().minDeletions(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()