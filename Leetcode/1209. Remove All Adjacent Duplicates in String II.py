'''
You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

 

Example 1:

Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.
Example 2:

Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation: 
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"
Example 3:

Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"
 

Constraints:

1 <= s.length <= 105
2 <= k <= 104
s only contains lower case English letters.
'''
import unittest


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        counts = []
        for w in s:
            count = 1
            if stack and stack[-1] == w:
                count = counts[-1] + 1
            stack.append(w)
            counts.append(count)

            if counts[-1] == k:
                # pop k num
                for _ in range(k):
                    stack.pop()
                    counts.pop()
        return "".join(stack)


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("abcd", 2), "abcd"),
            (("deeedbbcccbdaa", 3), "aa"),
            (("pbbcggttciiippooaais", 2), "ps")
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().removeDuplicates(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
