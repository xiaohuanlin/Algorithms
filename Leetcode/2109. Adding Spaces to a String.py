'''
You are given a 0-indexed string s and a 0-indexed integer array spaces that describes the indices in the original string where spaces will be added. Each space should be inserted before the character at the given index.

For example, given s = "EnjoyYourCoffee" and spaces = [5, 9], we place spaces before 'Y' and 'C', which are at indices 5 and 9 respectively. Thus, we obtain "Enjoy Your Coffee".
Return the modified string after the spaces have been added.

 

Example 1:

Input: s = "LeetcodeHelpsMeLearn", spaces = [8,13,15]
Output: "Leetcode Helps Me Learn"
Explanation: 
The indices 8, 13, and 15 correspond to the underlined characters in "LeetcodeHelpsMeLearn".
We then place spaces before those characters.
Example 2:

Input: s = "icodeinpython", spaces = [1,5,7,9]
Output: "i code in py thon"
Explanation:
The indices 1, 5, 7, and 9 correspond to the underlined characters in "icodeinpython".
We then place spaces before those characters.
Example 3:

Input: s = "spacing", spaces = [0,1,2,3,4,5,6]
Output: " s p a c i n g"
Explanation:
We are also able to place spaces before the first character of the string.
 

Constraints:

1 <= s.length <= 3 * 105
s consists only of lowercase and uppercase English letters.
1 <= spaces.length <= 3 * 105
0 <= spaces[i] <= s.length - 1
All the values of spaces are strictly increasing.
'''

from typing import *
import unittest

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ["" for _ in range(len(s) + len(spaces))]

        s_index = 0
        space_index = 0
        index = 0
        while index < len(res):
            if space_index >= len(spaces) or index != space_index + spaces[space_index]:
                # word
                res[index] = s[s_index]
                s_index += 1
            else:
                res[index] = " "
                space_index += 1
            index += 1
        return "".join(res)


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("LeetcodeHelpsMeLearn",[8,13,15]),"Leetcode Helps Me Learn"),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().addSpaces(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()