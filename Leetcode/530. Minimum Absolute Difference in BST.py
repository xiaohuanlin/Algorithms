'''

Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).


Note: There are at least two nodes in this BST.

'''
import unittest


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root):
        L = []
        def dfs(node):
            # keep in order
            if node.left:
                dfs(node.left)
            L.append(node.val)
            if node.right:
                dfs(node.right)
        dfs(root)
        return min(abs(a - b) for a, b in zip(L, L[1:]))
