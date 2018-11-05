'''

Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13

'''
import unittest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # node_list = []
        # def dsf(root):
        #     if root is None:
        #         return None
        #     dsf(root.left)
        #     node_list.append(root)
        #     dsf(root.right)
        #
        # dsf(root)
        # for i in range(2, len(node_list) + 1):
        #     node_list[-i].val += node_list[-i+1].val
        # return root
        # -------------------------
        self.acc = 0
        self.get_answer(root)
        return root

    def get_answer(self, root):
        if root is None:
            return None
        self.get_answer(root.right)
        root.val += self.acc
        self.acc = root.val
        self.get_answer(root.left)
