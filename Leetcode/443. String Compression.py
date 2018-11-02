'''

Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.


Follow up:
Could you solve it using only O(1) extra space?


Example 1:

Input:
["a","a","b","b","c","c","c"]

Output:
Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".


Example 2:

Input:
["a"]

Output:
Return 1, and the first 1 characters of the input array should be: ["a"]

Explanation:
Nothing is replaced.


Example 3:

Input:
["a","b","b","b","b","b","b","b","b","b","b","b","b"]

Output:
Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

Explanation:
Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
Notice each digit has it's own entry in the array.


Note:

All characters have an ASCII value in [35, 126].
1 <= len(chars) <= 1000.

'''
import unittest


class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        last_c = None
        count = 1
        chars.append(None)

        for index in range(-len(chars), 0):
            if chars[index] == last_c:
                chars.pop(index)
                count += 1
            else:
                if count > 1:
                    chars[index:index] = list(str(count))
                    count = 1
                last_c = chars[index]

        chars.pop(-1)
        return len(chars)


class TestSolution(unittest.TestCase):

    def test_compress(self):
        examples = (
            # ["a","2","b","2","c","3"]
            (["a","a","b","b","c","c","c"], 6),
            # ["a"]
            (["a"], 1),
            # ["a","b","1","2"]
            (["a","b","b","b","b","b","b","b","b","b","b","b","b"], 4),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().compress(first), second, msg="first: {}; second: {}".format(first, second))


unittest.main()