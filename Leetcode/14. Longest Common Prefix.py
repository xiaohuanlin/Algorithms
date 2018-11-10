'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.

'''
import unittest

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # def get_common(str1, str2):
        #     if len(str1) > len(str2):
        #         str1, str2 = str2, str1
        #     common = ''
        #     for index,x in enumerate(str1):
        #         if x == str2[index]:
        #             common += x
        #         else:
        #             break
        #     return common
        
        # if len(strs) == 0:
        #     return ''

        # for i in range(len(strs)-1):
        #     strs[i+1] = get_common(strs[i], strs[i+1])
        
        # return strs[-1]
        if len(strs) == 0:
            return ''
        elif len(strs) == 1:
            return strs[0]

        left_long = self.longestCommonPrefix(strs[:len(strs)//2])
        right_long = self.longestCommonPrefix(strs[len(strs)//2:])

        if len(left_long) > len(right_long):
            left_long, right_long = right_long, left_long
        common = ''
        for index,x in enumerate(left_long):
            if x == right_long[index]:
                common += x
            else:
                break
        return common


class TestSolution(unittest.TestCase):

    def test_longest(self):
        examples = ((["flower","flow","flight"], 'fl'),
                    (["dog","racecar","car"], ''),
                    (["flow","flower","flight"], 'fl')
        )
        for first,second in examples:
            self.assert_function(first, second)
        
    def assert_function(self, first, second):
        self.assertEqual(Solution().longestCommonPrefix(first), second)
