'''

Given a Binary Search Tree (BST) with the root node root, return the minimum difference between the values of any two different nodes in the tree.

Example :

Input: root = [4,2,6,1,3,null,null]
Output: 1
Explanation:
Note that root is a TreeNode object, not an array.

The given tree [4,2,6,1,3,null,null] is represented by the following diagram:

          4
        /   \
      2      6
     / \
    1   3

while the minimum difference in this tree is 1, it occurs between node 1 and node 2, also between node 3 and node 2.
Note:

The size of the BST will be between 2 and 100.
The BST is always valid, each node's value is an integer, and each node's value is different.

'''
import unittest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # stack = [root]
        # val_list = []
        # while stack:
        #     node = stack.pop()
        #     if node is None:
        #         continue
        #     val_list.append(node.val)
        #     stack.extend([node.left, node.right])
        # val_list.sort()
        # return min(a-b for a, b in zip(val_list[1:], val_list))
        # --------------------------------------
        def get_answer(root):
            # return min_diff, min, max
            if root.left is None and root.right is None:
                return float('+inf'), root.val, root.val

            if root.left is not None and root.right is not None:
                min_diff_l, min_root_l, max_root_l = get_answer(root.left)
                min_diff_r, min_root_r, max_root_r = get_answer(root.right)
                min_diff = min(min_diff_l, min_diff_r, root.val-max_root_l, min_root_r-root.val)
                return min_diff, min_root_l, max_root_r

            if root.left is None:
                min_diff_r, min_root_r, max_root_r = get_answer(root.right)
                return min(min_diff_r, min_root_r-root.val), root.val, max_root_r
            if root.right is None:
                min_diff_l, min_root_l, max_root_l = get_answer(root.left)
                return min(min_diff_l, root.val-max_root_l), min_root_l, root.val

        if root is None:
            return 0
        return get_answer(root)[0]
