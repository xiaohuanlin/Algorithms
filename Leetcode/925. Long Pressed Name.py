'''

Your friend is typing his name into a keyboard.  Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard.  Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.



Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
Example 2:

Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.
Example 3:

Input: name = "leelee", typed = "lleeelee"
Output: true
Example 4:

Input: name = "laiden", typed = "laiden"
Output: true
Explanation: It's not necessary to long press any character.


Note:

name.length <= 1000
typed.length <= 1000
The characters of name and typed are lowercase letters.

'''
import unittest


class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        i = j = 0

        while i < len(name) and j < len(typed):
            while name[i] != typed[j]:
                if typed[j] == name[i-1]:
                    if j == len(typed) - 1:
                        return False
                    j += 1
                else:
                    return False
            i += 1
            j += 1
        if i == len(name) and j != len(typed):
            return all(name[i-1] == typed[k] for k in range(j, len(typed)))
        if i != len(name) and j == len(typed):
            return False
        return True





class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("pyplrz", "ppyypllr"), False),
            (("kikcxmvzi", "kiikcxxmmvvzz"), False),
            (('alex', 'aaleex'), True),
            (('saeed', 'ssaaedd'), False),
            (('leelee', 'lleeelee'), True),
            (('laiden', 'laiden'), True),
            (('la', 'laxz'), False)
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().isLongPressedName(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
