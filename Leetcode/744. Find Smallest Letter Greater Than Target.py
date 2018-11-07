'''

Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.

Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

Examples:
Input:
letters = ["c", "f", "j"]
target = "a"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "c"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "d"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "g"
Output: "j"

Input:
letters = ["c", "f", "j"]
target = "j"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "k"
Output: "c"
Note:
letters has a length in range [2, 10000].
letters consists of lowercase letters, and contains at least 2 unique letters.
target is a lowercase letter.

'''
import unittest


class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        # for letter in letters:
        #     if ord(letter) > ord(target):
        #         return letter
        # return letters[0]
        # --------------------------------------
        import bisect
        pos = bisect.bisect_right(letters, target)
        return letters[0] if pos == len(letters) else letters[pos]

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((["c", "f", "j"], 'a'), 'c'),
            ((["c", "f", "j"], 'c'), 'f'),
            ((["c", "f", "j"], 'd'), 'f'),
            ((["c", "f", "j"], 'g'), 'j'),
            ((["c", "f", "j"], 'j'), 'c'),
            ((["c", "f", "j"], 'k'), 'c'),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().nextGreatestLetter(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
