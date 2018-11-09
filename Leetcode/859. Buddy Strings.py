'''

Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.



Example 1:

Input: A = "ab", B = "ba"
Output: true
Example 2:

Input: A = "ab", B = "ab"
Output: false
Example 3:

Input: A = "aa", B = "aa"
Output: true
Example 4:

Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true
Example 5:

Input: A = "", B = "aa"
Output: false


Note:

0 <= A.length <= 20000
0 <= B.length <= 20000
A and B consist only of lowercase letters.

'''
import unittest


class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        from collections import Counter

        if len(A) != len(B):
            return False

        result_list = []
        for a, b in zip(A, B):
            if a != b:
                result_list.append((a, b))
        # print(result_list)
        if result_list == []:
            return max(Counter(A).values(), default=0) > 1
        if len(result_list) > 2:
            return False

        return all((b, a) in result_list for a, b in result_list)



class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("abcd", "badc"), False),
            (('', ''), False),
            (('ab', 'ba'), True),
            (('ab', 'ab'), False),
            (('aa', 'aa'), True),
            (('aaaaaaabc', 'aaaaaaacb'), True),
            (('', 'aa'), False)
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().buddyStrings(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
