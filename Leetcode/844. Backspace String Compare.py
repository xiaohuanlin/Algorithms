'''

Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?

'''
import unittest


class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        i = len(S) - 1
        j = len(T) - 1
        i_count = j_count = 0

        while i >= 0 or j >= 0:
            while i >= 0:
                if S[i] == '#':
                    i_count += 1
                elif i_count > 0:
                    i_count -= 1
                else:
                    break
                i -= 1
            while j >= 0:
                if T[j] == '#':
                    j_count += 1
                elif j_count > 0:
                    j_count -= 1
                else:
                    break
                j -= 1

            if (i < 0 and j >= 0) or (i >= 0 and j < 0):
                return False

            # print(i, j)
            if i >= 0 and j >= 0 and S[i] != T[j]:
                return False
            else:
                i -= 1
                j -= 1

        return True





class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (('ab#c', 'ad#c'), True),
            (('ab##', 'c#d#'), True),
            (('a##c', '#a#c'), True),
            (('a#c', 'b'), False),
            (('b#c', 'c'), True),
            (('a#', 'a'), False),
            (('abc##b', 'ab'), True),
            (('###', '##'), True),
            (("bxj##tw", "bxj###tw"), False),
            (("bbbextm", "bbb#extm"), False),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().backspaceCompare(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
