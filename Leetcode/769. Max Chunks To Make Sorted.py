'''
You are given an integer array arr of length n that represents a permutation of the integers in the range [0, n - 1].

We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.

Return the largest number of chunks we can make to sort the array.

 

Example 1:

Input: arr = [4,3,2,1,0]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.
Example 2:

Input: arr = [1,0,2,3,4]
Output: 4
Explanation:
We can split into two chunks, such as [1, 0], [2, 3, 4].
However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.
 

Constraints:

n == arr.length
1 <= n <= 10
0 <= arr[i] < n
All the elements of arr are unique.
'''
from typing import *

import unittest
from pprint import pprint


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        min_v = float('+inf')
        max_v = float('-inf')
        sum_v = 0
        start = 0
        count = 0
        for i in range(len(arr)):
            sum_v += arr[i]
            min_v = min(min_v, arr[i])
            max_v = max(max_v, arr[i])
            if sum_v == (start + i) * (i - start + 1) / 2 and min_v == start and max_v == i:
                count += 1
                start = i + 1
                min_v = float('+inf')
                max_v = float('-inf')
                sum_v = 0
        return count

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([4,3,2,1,0],), 1),
            (([1,0,2,3,4],), 4),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maxChunksToSorted(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
