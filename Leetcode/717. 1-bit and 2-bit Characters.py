'''

We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11).

Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.

Example 1:
Input:
bits = [1, 0, 0]
Output: True
Explanation:
The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.
Example 2:
Input:
bits = [1, 1, 1, 0]
Output: False
Explanation:
The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.
Note:

1 <= len(bits) <= 1000.
bits[i] is always 0 or 1.

'''
import unittest


class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        # def get_answer(bits):
        #     # print(bits, bits[:-1], bits[:-2], bits[-2:] in ([0, 0], [1, 0], [1, 1]))
        #     if bits == [0] or bits == []:
        #         return True
        #
        #     result_1 = get_answer(bits[:-1]) if len(bits) > 0 and bits[-1] == 0 else False
        #     result_2 = get_answer(bits[:-2]) if len(bits) > 1 and bits[-2:] in ([0, 0], [1, 0], [1, 1]) else False
        #
        #     return result_1 or result_2
        # return get_answer(bits[:-1])
        # -----------------------------------------
        if not bits:
            return False
        n = len(bits)

        index = 0
        while index < n:
            if index == n - 1:
                # the last element
                return True
            if bits[index] == 1:
                index += 2
            else:
                index += 1
        return False


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ([1, 0, 0], True),
            ([1, 1, 1, 0], False),
            ([0, 1, 0], False),
            ([1,0,0,0], True),
            ([0], True),
            ([1, 1, 0], True)
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().isOneBitCharacter(first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
