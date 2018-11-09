'''

In a string S of lowercase letters, these letters form consecutive groups of the same character.

For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".

Call a group large if it has 3 or more characters.  We would like the starting and ending positions of every large group.

The final answer should be in lexicographic order.



Example 1:

Input: "abbxxxxzzy"
Output: [[3,6]]
Explanation: "xxxx" is the single large group with starting  3 and ending positions 6.
Example 2:

Input: "abc"
Output: []
Explanation: We have "a","b" and "c" but no large group.
Example 3:

Input: "abcdddeeeeaabbbcd"
Output: [[3,5],[6,9],[12,14]]


Note:  1 <= S.length <= 1000

'''
import unittest


class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        count = 0
        pre = ''
        result = []
        for i in range(len(S)):
            if S[i] == pre:
                count += 1
            else:
                if count >= 3:
                    result.append([i-count, i-1])
                pre = S[i]
                count = 1
        else:
            if count >= 3:
                if i - count >= 0:
                    result.append([i-count+1, i])
                else:
                    result.append([0, i])
        return result


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ('abbxxxxzzy', [[3,6]]),
            ('abc', []),
            ('abcdddeeeeaabbbcd', [[3,5],[6,9],[12,14]]),
            ('aaa', [[0,2]]),
            ('baaa', [[1, 3]])
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().largeGroupPositions(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
