'''
You are given two arrays of integers, fruits and baskets, each of length n, where fruits[i] represents the quantity of the ith type of fruit, and baskets[j] represents the capacity of the jth basket.

From left to right, place the fruits according to these rules:

Each fruit type must be placed in the leftmost available basket with a capacity greater than or equal to the quantity of that fruit type.
Each basket can hold only one type of fruit.
If a fruit type cannot be placed in any basket, it remains unplaced.
Return the number of fruit types that remain unplaced after all possible allocations are made.

 

Example 1:

Input: fruits = [4,2,5], baskets = [3,5,4]

Output: 1

Explanation:

fruits[0] = 4 is placed in baskets[1] = 5.
fruits[1] = 2 is placed in baskets[0] = 3.
fruits[2] = 5 cannot be placed in baskets[2] = 4.
Since one fruit type remains unplaced, we return 1.

Example 2:

Input: fruits = [3,6,1], baskets = [6,4,7]

Output: 0

Explanation:

fruits[0] = 3 is placed in baskets[0] = 6.
fruits[1] = 6 cannot be placed in baskets[1] = 4 (insufficient capacity) but can be placed in the next available basket, baskets[2] = 7.
fruits[2] = 1 is placed in baskets[1] = 4.
Since all fruits are successfully placed, we return 0.

 

Constraints:

n == fruits.length == baskets.length
1 <= n <= 105
1 <= fruits[i], baskets[i] <= 109
'''
import unittest

from typing import *


class SegmentTree:
    def __init__(self, nums):
        n = len(nums)
        self.tree = [0] * 4 * n
        self.nums = nums
        self.build(0, 0, n - 1)

    def build(self, i, l, r):
        if l == r:
            self.tree[i] = self.nums[l]
            return
        m = (l + r) // 2
        self.build(2*i + 1, l, m)
        self.build(2*i + 2, m+1, r)
        self.tree[i] = max(self.tree[2*i+1], self.tree[2*i+2])
    
    def query(self, k, i, l, r):
        if self.tree[i] < k:
            return -1

        if l == r:
            self.tree[i] = -1
            return l

        m = (l + r) // 2
        if self.tree[2*i + 1] >= k:
            pos = self.query(k, 2*i + 1, l, m)
        else:
            pos = self.query(k, 2*i + 2, m+1, r)
        self.tree[i] = max(self.tree[2*i+1], self.tree[2*i+2])
        return pos

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        s = SegmentTree(baskets)

        res = 0
        for f in fruits:
            pos = s.query(f, 0, 0, len(baskets) - 1)
            if pos == -1:
                res += 1
        return res

            
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (([4, 2, 5], [3, 5, 4]), 1),
            (([3, 6, 1], [6, 4, 7]), 0),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().numOfUnplacedFruits(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
