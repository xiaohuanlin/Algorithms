'''

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

'''
import unittest


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # get the counter information for p
        from collections import Counter
        p_dict = Counter(p)

        result = []
        s_list = list(s[:len(p)])
        s_dict = Counter(s_list)
        if s_dict == p_dict:
            result.append(0)

        for i, w in enumerate(s[len(p):]):
            # update word list
            s_list.append(s[i+len(p)])
            old_w = s_list.pop(0)
            # update dict
            s_dict[w] = s_dict.setdefault(w, 0) + 1
            if s_dict[old_w] == 1:
                del s_dict[old_w]
            else:
                s_dict[old_w] -= 1

            # print(s_list, s_dict)
            if s_dict == p_dict:
                result.append(i+1)

        return result


class TestSolution(unittest.TestCase):

    def test_findAnagrams(self):
        examples = (
            (('cbaebabacd', 'abc'), [0, 6]),
            (('abab', 'ab'), [0, 1, 2]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().findAnagrams(*first), second, msg="first: {}; second: {}".format(first, second))


unittest.main()