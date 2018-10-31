'''

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.

'''
import unittest


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # from collections import OrderedDict
        # word_dict = OrderedDict()
        # for i, word in enumerate(s):
        #     if word not in word_dict:
        #         word_dict[word] = [i, 1]
        #     else:
        #         word_dict[word][1] = word_dict[word][1] + 1
        # # print(word_dict)
        #
        # for record in word_dict.items():
        #     if record[1][1] == 1:
        #         return record[1][0]
        # return -1
        # ------------------------------------
        standand_s = [chr(i) for i in range(ord('a'), ord('{'))]

        word_index = [s.index(word) for word in standand_s if s.count(word) == 1]

        return min(word_index) if word_index else -1


class TestSolution(unittest.TestCase):

    def test_firstUniqChar(self):
        examples = (
            ('leetcode', 0),
            ('loveleetcode', 2),
            ("dddccdbba", 8),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().firstUniqChar(first), second, msg="first: {}; second: {}".format(first, second))


unittest.main()