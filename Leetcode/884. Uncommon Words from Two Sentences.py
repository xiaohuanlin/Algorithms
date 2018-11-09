'''

We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words.

You may return the list in any order.



Example 1:

Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]
Example 2:

Input: A = "apple apple", B = "banana"
Output: ["banana"]


Note:

0 <= A.length <= 200
0 <= B.length <= 200
A and B both contain only spaces and lowercase letters.

'''
import unittest


class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        from collections import Counter
        #
        # A = Counter(A.split(' '))
        # B = Counter(B.split(' '))
        # A_set = set(key for key, value in A.items() if value == 1)
        # B_set = set(key for key, value in B.items() if value == 1)
        # A_list = [a for a in A_set if a not in B]
        # B_list = [b for b in B_set if b not in A]
        # return A_list + B_list
        # ---------------------------------
        return [key for key, value in Counter(A.split(' ') + B.split(' ')).items() if value == 1]


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (('this apple is sweet', 'this apple is sour'), ["sweet","sour"]),
            (('apple apple', 'banana'), ['banana']),
            (("s z z z s", "s z ejt"), ["ejt"]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().uncommonFromSentences(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
