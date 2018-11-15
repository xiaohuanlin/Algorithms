'''

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.

'''
import unittest


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        num_letter_dict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        result = ['']
        for digit in digits:
            tmp = []
            for res in result:
                for letter in num_letter_dict[digit]:
                    tmp.append(res + letter)
            result = tmp
        return result


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ('23', ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
            ('', [])
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().letterCombinations(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
