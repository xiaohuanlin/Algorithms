'''

Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]


Note:

S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase.

'''
import unittest


class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        # from bisect import bisect
        # c_list = [i for i, s in enumerate(S) if s == C]
        # result = []
        # print(c_list)
        # for i, s in enumerate(S):
        #     index = bisect(c_list, i)
        #     print(index)
        #     if index == len(c_list):
        #         left = i - c_list[index - 1]
        #         result.append(left)
        #         continue
        #     right = c_list[index] - i
        #     if index == 0:
        #         result.append(right)
        #         continue
        #     left = i - c_list[index-1]
        #     result.append(min(left, right))
        # return result
        from bisect import bisect
        c_list = [float('-inf')] + [i for i, s in enumerate(S) if s == C] + [float('+inf')]
        result = []
        # print(c_list)
        for i, s in enumerate(S):
            index = bisect(c_list, i)
            right = c_list[index] - i
            left = i - c_list[index-1]
            result.append(min(left, right))
        return result


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (('loveleetcode', 'e'), [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().shortestToChar(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
