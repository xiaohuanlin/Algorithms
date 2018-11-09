'''



Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.



For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.



Note:

Both of the given trees will have between 1 and 100 nodes.

'''
import unittest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.get_leaf(root1) == self.get_leaf(root2)

    def get_leaf(self, root):
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            if node.left is None and node.right is None:
                result.append(node.val)
            elif node.left is not None and node.right is not None:
                stack.extend([node.left, node.right])
            elif node.left is not None:
                stack.append(node.left)
            else:
                stack.append(node.right)

        return result
