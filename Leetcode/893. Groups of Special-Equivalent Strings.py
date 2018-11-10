'''

You are given an array A of strings.

Two strings S and T are special-equivalent if after any number of moves, S == T.

A move consists of choosing two indices i and j with i % 2 == j % 2, and swapping S[i] with S[j].

Now, a group of special-equivalent strings from A is a non-empty subset S of A such that any string not in S is not special-equivalent with any string in S.

Return the number of groups of special-equivalent strings from A.



Example 1:

Input: ["a","b","c","a","c","c"]
Output: 3
Explanation: 3 groups ["a","a"], ["b"], ["c","c","c"]
Example 2:

Input: ["aa","bb","ab","ba"]
Output: 4
Explanation: 4 groups ["aa"], ["bb"], ["ab"], ["ba"]
Example 3:

Input: ["abc","acb","bac","bca","cab","cba"]
Output: 3
Explanation: 3 groups ["abc","cba"], ["acb","bca"], ["bac","cab"]
Example 4:

Input: ["abcd","cdab","adcb","cbad"]
Output: 1
Explanation: 1 group ["abcd","cdab","adcb","cbad"]

'''
import unittest


class Solution:
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        result_dict = {}
        for s in A:
            spec_s = self.spec_eq(s)
            # print(s, spec_s)
            if spec_s not in result_dict:
                result_dict[spec_s] = [s]
            else:
                result_dict[spec_s].append(s)
        # print(result_dict)
        return len(result_dict)

    def spec_eq(self, s):
        odd_sort = sorted(s[::2])
        even_sort = sorted(s[1::2])
        result = [0] * len(s)
        for i, number in enumerate(odd_sort):
            result[2*i] = odd_sort[i]
        for i, number in enumerate(even_sort):
            result[2 * i + 1] = even_sort[i]
        return tuple(result)


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (["a","b","c","a","c","c"], 3),
            (["aa","bb","ab","ba"], 4),
            (["abc","acb","bac","bca","cab","cba"], 3),
            (["abcd","cdab","adcb","cbad"], 1)
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().numSpecialEquivGroups(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
