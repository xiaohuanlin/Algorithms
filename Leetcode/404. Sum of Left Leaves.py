'''

Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

'''
import unittest


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        value = 0
        if root is None:
            return 0
        if root.left is not None and root.left.left is None and root.left.right is None:
            value = root.left.val
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right) + value
