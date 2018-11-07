'''

Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
Note:

S will be a string with length between 1 and 12.
S will consist only of letters or digits.

'''
import unittest


class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        def get_answer(i):
            if i == -1:
                return ['']
            if not S[i].isalpha():
                # print(S[i])
                return [word+S[i] for word in get_answer(i-1)]
            else:
                return [word+S[i].lower() for word in get_answer(i-1)] + [word+S[i].upper() for word in get_answer(i-1)]
        return get_answer(len(S)-1)


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ('a1b2', ["a1b2", "a1B2", "A1b2", "A1B2"]),
            ('3z4', ["3z4", "3Z4"]),
            ('12345', ['12345'])
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().letterCasePermutation(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
