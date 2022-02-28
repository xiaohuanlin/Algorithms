'''
Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values and postorder is the postorder traversal of the same tree, reconstruct and return the binary tree.

If there exist multiple answers, you can return any of them.

 

Example 1:


Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]
Example 2:

Input: preorder = [1], postorder = [1]
Output: [1]
 

Constraints:

1 <= preorder.length <= 30
1 <= preorder[i] <= preorder.length
All the values of preorder are unique.
postorder.length == preorder.length
1 <= postorder[i] <= postorder.length
All the values of postorder are unique.
It is guaranteed that preorder and postorder are the preorder traversal and postorder traversal of the same binary tree.
'''
from typing import *

import unittest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        pre_map = {}
        post_map = {}
        for i, num in enumerate(preorder):
            pre_map[num] = i
        for i, num in enumerate(postorder):
            post_map[num] = i
        return self.iter_fun(preorder, 0, len(preorder), pre_map, postorder, 0, len(postorder), post_map)

    def iter_fun(self, preorder, pre_start, pre_end, pre_map, postorder, post_start, post_end, post_map):
        length = pre_end - pre_start
        if length == 0:
            return None
        elif length == 1:
            return TreeNode(preorder[pre_start])
        elif length == 2:
            return TreeNode(preorder[pre_start], TreeNode(preorder[pre_start + 1]))

        root = TreeNode(preorder[pre_start])
        left_v = preorder[pre_start + 1]
        right_v = postorder[post_end - 2]
        left = self.iter_fun(preorder, pre_start + 1, pre_map[right_v], pre_map, postorder, post_start, post_map[left_v] + 1, post_map)
        right = self.iter_fun(preorder, pre_map[right_v], pre_end, pre_map, postorder, post_map[left_v] + 1, post_end - 1, post_map)
        root.left = left
        root.right = right
        return root

