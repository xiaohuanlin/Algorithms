'''
You are given a 0-indexed array nums consisting of n positive integers.

The array nums is called alternating if:

nums[i - 2] == nums[i], where 2 <= i <= n - 1.
nums[i - 1] != nums[i], where 1 <= i <= n - 1.
In one operation, you can choose an index i and change nums[i] into any positive integer.

Return the minimum number of operations required to make the array alternating.

 

Example 1:

Input: nums = [3,1,3,2,4,3]
Output: 3
Explanation:
One way to make the array alternating is by converting it to [3,1,3,1,3,1].
The number of operations required in this case is 3.
It can be proven that it is not possible to make the array alternating in less than 3 operations. 
Example 2:

Input: nums = [1,2,2,2,2]
Output: 2
Explanation:
One way to make the array alternating is by converting it to [1,2,1,2,1].
The number of operations required in this case is 2.
Note that the array cannot be converted to [2,2,2,2,2] because in this case nums[0] == nums[1] which violates the conditions of an alternating array.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105
'''
from typing import *
import unittest

from collections import Counter
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        odd = Counter()
        even = Counter()
        for i in range(len(nums)):
            if i % 2 == 0:
                even[nums[i]] += 1
            else:
                odd[nums[i]] += 1

        most_odd_v = 0
        most_odd = set()
        second_odd_v = 0
        second_odd = set()
        for k, v in odd.items():
            if v > most_odd_v:
                second_odd = most_odd
                second_odd_v = most_odd_v
                most_odd = set([k])
                most_odd_v = v
            elif v == most_odd_v:
                most_odd.add(k)
            elif v > second_odd_v:
                second_odd = set([k])
                second_odd_v = v
            elif v == second_odd_v:
                second_odd.add(k)

        most_even_v = 0
        most_even = set()
        second_even_v = 0
        second_even = set()
        for k, v in even.items():
            if v > most_even_v:
                second_even = most_even
                second_even_v = most_even_v
                most_even = set([k])
                most_even_v = v
            elif v == most_even_v:
                most_even.add(k)
            elif v > second_even_v:
                second_even = set([k])
                second_even_v = v
            elif v == second_even_v:
                second_even.add(k)

        if most_odd != most_even or len(most_odd) > 1:
            return len(nums) - most_odd_v - most_even_v
        if not second_odd and not second_even:
            return len(nums) - max(most_odd_v, most_even_v)
        if second_odd and second_even:
            return len(nums) - max(second_even_v + most_odd_v, second_odd_v + most_even_v)
        if second_odd:
            return len(nums) - max(most_odd_v, second_odd_v + most_even_v)
        return len(nums) - max(most_even_v, second_even_v + most_odd_v)
                    

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([1,2,2,2,2],),2),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().minimumOperations(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
