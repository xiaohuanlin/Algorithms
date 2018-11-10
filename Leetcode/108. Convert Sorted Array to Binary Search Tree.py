'''
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
'''

import unittest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums == []:
            return None

        node_index = len(nums)//2
        node = TreeNode(nums[node_index])
        node.left, node.right = self.sortedArrayToBST(nums[:node_index]), self.sortedArrayToBST(nums[node_index+1:])
        return node

class TestSolution(unittest.TestCase):

    def test_sortedArrayToBST(self):
        examples = (

        )
        for first,second in examples:
            self.assert_function(first, second)
        
    def assert_function(self, first, second):
        self.assertEqual(Solution().sortedArrayToBST(*first), second)

unittest.main()