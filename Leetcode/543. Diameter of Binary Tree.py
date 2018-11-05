'''

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.

'''
import unittest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
    #     if root is None:
    #         return 0
    #
    #     return max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right),
    #             self.get_max_h(root.left) + self.get_max_h(root.right) + 2)
    #
    # def get_max_h(self, root):
    #     if root is None:
    #         return -1
    #     if root.left is None and root.right is None:
    #         return 0
    #     return max(self.get_max_h(root.left), self.get_max_h(root.right)) + 1
    #     ------------------------------------------------------------------------
        self.answer = 1

        def dfs(root):
            if root is None:
                return 0

            l_max_node = dfs(root.left)
            r_max_node = dfs(root.right)
            self.answer = max(self.answer, l_max_node + r_max_node + 1)
            return max(l_max_node, r_max_node) + 1

        dfs(root)
        return self.answer - 1