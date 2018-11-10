'''

In a deck of cards, each card has an integer written on it.

Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:

Each group has exactly X cards.
All the cards in each group have the same integer.


Example 1:

Input: [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4]
Example 2:

Input: [1,1,1,2,2,2,3,3]
Output: false
Explanation: No possible partition.
Example 3:

Input: [1]
Output: false
Explanation: No possible partition.
Example 4:

Input: [1,1]
Output: true
Explanation: Possible partition [1,1]
Example 5:

Input: [1,1,2,2,2,2]
Output: true
Explanation: Possible partition [1,1],[2,2],[2,2]

Note:

1 <= deck.length <= 10000
0 <= deck[i] < 10000

'''
import unittest


class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        from collections import Counter
        word_dict = Counter(deck)
        i = 2
        while i <= max(word_dict.values()):
            if all(word % i == 0 for word in word_dict.values()):
                return True
            i += 1

        return False


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ([1,1,1,1,2,2,2,2,2,2], True),
            ([1,2,3,4,4,3,2,1], True),
            ([1,1,1,2,2,2,3,3], False),
            ([1], False),
            ([1,1], True),
            ([1,1,2,2,2,2], True)
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().hasGroupsSizeX(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
