'''
You are given an integer array arr. You can choose a set of integers and remove all the occurrences of these integers in the array.

Return the minimum size of the set so that at least half of the integers of the array are removed.

 

Example 1:

Input: arr = [3,3,3,3,5,5,5,2,2,7]
Output: 2
Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
Possible sets of size 2 are {3,5},{3,2},{5,2}.
Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has a size greater than half of the size of the old array.
Example 2:

Input: arr = [7,7,7,7,7,7]
Output: 1
Explanation: The only possible set you can choose is {7}. This will make the new array empty.
 

Constraints:

2 <= arr.length <= 105
arr.length is even.
1 <= arr[i] <= 105
'''
from typing import *

import unittest
from collections import Counter


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = Counter(arr)
        items = counter.items()
        items = sorted(items, key = lambda x: -x[1])
        target = len(arr) // 2
        count = 0
        for _, v in items:
            if target <= 0:
                return count
            target -= v
            count += 1
        return count


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([9,77,63,22,92,9,14,54,8,38,18,19,38,68,58,19],), 5),
            (([3,3,3,3,5,5,5,2,2,7],), 2),
            (([7,7,7,7,7,7],), 1),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().minSetSize(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
