'''

Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.


For example:
Given BST [1,null,2,2],

   1
    \
     2
    /
   2


return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).

'''
import unittest


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return None
        count = self.get_answer(root)
        max_value = max(count.values())
        return [key for key in count.keys() if count[key] == max_value]

    def get_answer(self, root):
        # return frequency_dict
        if root is None:
            return {}
        frequency_dict = {root.val: 1}
        for map in (self.get_answer(root.left), self.get_answer(root.right)):
            for key, value in map.items():
                frequency_dict[key] = frequency_dict.setdefault(key, 0) + value
        return frequency_dict