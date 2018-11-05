'''

Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Restrictions:
The string consists of lower English letters only.
Length of the given string and k will in the range [1, 10000]

'''
import unittest


class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        stack = []
        queue = []
        result = []
        max_len = k
        for index, word in enumerate(s):
            if len(stack) < max_len:
                stack.append(word)
            elif len(queue) < max_len:
                queue.append(word)
            # print(word, stack, queue)
            if index == len(s)-1 or len(stack) == max_len and len(queue) == max_len:
                while stack:
                    result.append(stack.pop())
                while queue:
                    result.append(queue.pop(0))
        return ''.join(result)




class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (('abcdefg', 2), 'bacdfeg'),
            (('a', 2), 'a'),
            (('abc', 5), 'cba')
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().reverseStr(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
