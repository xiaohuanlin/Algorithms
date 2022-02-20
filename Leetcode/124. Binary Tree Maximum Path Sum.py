'''
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

 

Example 1:


Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
Example 2:


Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
 

Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000
'''

from re import I
from typing import *
from pprint import pprint

import unittest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        _, res = self.helper(root)
        return res

    def helper(self, node: TreeNode) -> Tuple[int, int]:
        max_from_root = node.val
        max_path = node.val
        if node.left:
            max_sum_from_left, max_sum_path_left = self.helper(node.left)
            max_from_root = max(max_sum_from_left + node.val, max_from_root)
            max_path = max(max_path, max_sum_path_left, max_from_root)
        
        if node.right:
            max_sum_from_right, max_sum_path_right = self.helper(node.right)
            max_from_root = max(max_sum_from_right + node.val, max_from_root)
            max_path = max(max_path, max_sum_path_right, max_from_root)

        if node.left and node.right:
            max_path = max(max_path, max_sum_from_left + max_sum_from_right + node.val)

        return max_from_root, max_path

