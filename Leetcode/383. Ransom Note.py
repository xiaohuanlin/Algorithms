'''

Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true

'''
import unittest


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        from collections import Counter
        note = Counter(ransomNote)
        mag = Counter(magazine)
        for word, number in note.items():
            if mag.setdefault(word, 0) < number:
                return False
        return True

class TestSolution(unittest.TestCase):

    def test_canConstruct(self):
        examples = (
            (('a', 'b'), False),
            (('aa', 'ab'), False),
            (('aa', 'aab'), True),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().canConstruct(*first), second, msg="first: {}; second: {}".format(first, second))


unittest.main()