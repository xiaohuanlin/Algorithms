'''

Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.

'''
import unittest


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if root is None:
            return []
        old_level_list = [root]
        new_level_list = []
        value_list = []
        result = [float(root.val)]
        while old_level_list:
            for node in old_level_list:
                if node is None:
                    continue
                if node.left is not None:
                    new_level_list.append(node.left)
                    value_list.append(getattr(node.left, 'val', 0))
                if node.right is not None:
                    new_level_list.append(node.right)
                    value_list.append(getattr(node.right, 'val', 0))

            if len(value_list):
                result.append(sum(value for value in value_list)/len(value_list))
            old_level_list = new_level_list
            new_level_list = []
            value_list = []
        return result

