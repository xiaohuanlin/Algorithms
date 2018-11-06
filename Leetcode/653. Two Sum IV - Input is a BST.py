'''

Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:
Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
Example 2:
Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False

'''
import unittest


class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        node_list = [root]
        node_value_list = []
        while node_list:
            node = node_list.pop()
            if node.left is not None:
                node_list.append(node.left)
            if node.right is not None:
                node_list.append(node.right)
            node_value_list.append(node.val)
        res_value_dict = {k-value: value for value in node_value_list}
        for value in node_value_list:
            if value in res_value_dict and value != res_value_dict[value]:
                return True
        return False

