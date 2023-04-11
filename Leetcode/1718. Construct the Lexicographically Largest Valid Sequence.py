'''
Given an integer n, find a sequence that satisfies all of the following:

The integer 1 occurs once in the sequence.
Each integer between 2 and n occurs twice in the sequence.
For every integer i between 2 and n, the distance between the two occurrences of i is exactly i.
The distance between two numbers on the sequence, a[i] and a[j], is the absolute difference of their indices, |j - i|.

Return the lexicographically largest sequence. It is guaranteed that under the given constraints, there is always a solution.

A sequence a is lexicographically larger than a sequence b (of the same length) if in the first position where a and b differ, sequence a has a number greater than the corresponding number in b. For example, [0,1,9,0] is lexicographically larger than [0,1,5,6] because the first position they differ is at the third number, and 9 is greater than 5.



Example 1:

Input: n = 3
Output: [3,1,2,3,2]
Explanation: [2,3,2,1,3] is also a valid sequence, but [3,1,2,3,2] is the lexicographically largest valid sequence.
Example 2:

Input: n = 5
Output: [5,3,1,4,3,5,2,4,2]


Constraints:

1 <= n <= 20
'''
import unittest

from typing import *

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        def dfs(index, array, remain):
            if index == len(array):
                return True
            if array[index] != 0:
                return dfs(index + 1, array, remain)

            for i in sorted(remain, reverse=True):
                if i > 1 and i + index >= len(array):
                    continue
                if array[index] != 0 or (i > 1 and index + i < len(array) and array[index + i]) != 0:
                    continue
                array[index] = i
                if i > 1:
                    array[i + index] = i
                remain.remove(i)
                if dfs(index + 1, array, {x for x in remain}):
                    return True
                remain.add(i)
                array[index] = 0
                if i > 1:
                    array[i + index] = 0
            return False

        arr = [0 for _ in range(2 * n - 1)]
        remain = set(i for i in range(1, n + 1))
        dfs(0, arr, remain)
        return arr


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((2,), [2,1,2]),
            # ((5,), [5,3,1,4,3,5,2,4,2]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().constructDistancedSequence(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
