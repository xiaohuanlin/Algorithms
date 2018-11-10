'''

Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.



Example 1:

Input: "ab-cd"
Output: "dc-ba"
Example 2:

Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"


Note:

S.length <= 100
33 <= S[i].ASCIIcode <= 122
S doesn't contain \ or "

'''
import unittest


class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        S = list(S)
        i = 0
        j = len(S) - 1
        while i < j:
            if S[i].isalpha() and S[j].isalpha():
                S[i], S[j] = S[j], S[i]
                i += 1
                j -= 1
            elif not S[j].isalpha() and not S[i].isalpha():
                i += 1
                j -= 1
            elif not S[i].isalpha():
                i += 1
            else:
                j -= 1
        return ''.join(S)


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ("7_28]", "7_28]"),
            ('ab-cd', "dc-ba"),
            ("a-bC-dEf-ghIj", "j-Ih-gfE-dCba"),
            ("Test1ng-Leet=code-Q!", "Qedo1ct-eeLg=ntse-T!")
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().reverseOnlyLetters(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
