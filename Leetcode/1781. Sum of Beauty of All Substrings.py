'''
The beauty of a string is the difference in frequencies between the most frequent and least frequent characters.

For example, the beauty of "abaacc" is 3 - 1 = 2.
Given a string s, return the sum of beauty of all of its substrings.

 

Example 1:

Input: s = "aabcb"
Output: 5
Explanation: The substrings with non-zero beauty are ["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1.
Example 2:

Input: s = "aabcbaa"
Output: 17
 

Constraints:

1 <= s.length <= 500
s consists of only lowercase English letters.
'''
import unittest

class Solution:
    def beautySum(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            fre = [0 for _ in range(26)]
            for j in range(i, len(s)):
                fre[ord(s[j]) - ord('a')] += 1
                maxv = max(fre)
                minv = min(f for f in fre if f > 0)
                res += (maxv - minv)
        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("aabcb",),5),
            (("aabcbaa",),17),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().beautySum(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
