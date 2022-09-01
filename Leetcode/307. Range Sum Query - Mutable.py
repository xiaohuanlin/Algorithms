'''
Given an integer array nums, handle multiple queries of the following types:

Update the value of an element in nums.
Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
void update(int index, int val) Updates the value of nums[index] to be val.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
 

Example 1:

Input
["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
Output
[null, 9, null, 8]

Explanation
NumArray numArray = new NumArray([1, 3, 5]);
numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
numArray.update(1, 2);   // nums = [1, 2, 5]
numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8
 

Constraints:

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
0 <= index < nums.length
-100 <= val <= 100
0 <= left <= right < nums.length
At most 3 * 104 calls will be made to update and sumRange.
'''

from typing import *

import unittest


class SegmentTree:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.sum = 0
        self.left = None
        self.right = None


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.root = self.build(0, len(nums)-1)
        
    def build(self, start, end):
        node = SegmentTree(start, end)
        if start == end:
            node.sum = self.nums[start]
            return node
        mid = start + (end - start) // 2
        node.left = self.build(start, mid)
        node.right = self.build(mid + 1, end)
        node.sum = node.left.sum + node.right.sum
        return node
    
    def _update(self, root, index, val):
        if root.start == index and root.end == index:
            root.sum = val
            return
        mid = root.start + (root.end - root.start) // 2
        if index > mid:
            self._update(root.right, index, val)
        else:
            self._update(root.left, index, val)
        root.sum = root.left.sum + root.right.sum

    def update(self, index: int, val: int) -> None:
        self._update(self.root, index, val)
    
    def _sumRange(self, root, left, right):
        if root.start == left and root.end == right:
            return root.sum
        mid = root.start + (root.end - root.start) // 2
        
        if mid >= right:
            return self._sumRange(root.left, left, right)
        elif mid < left:
            return self._sumRange(root.right, left, right)
        else:
            return self._sumRange(root.left, left, mid) + self._sumRange(root.right, mid+1, right)
        
    def sumRange(self, left: int, right: int) -> int:
        return self._sumRange(self.root, left, right)