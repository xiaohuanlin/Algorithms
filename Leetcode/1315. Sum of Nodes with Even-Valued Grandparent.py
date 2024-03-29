'''
Given the root of a binary tree, return the sum of values of nodes with an even-valued grandparent. If there are no nodes with an even-valued grandparent, return 0.

A grandparent of a node is the parent of its parent if it exists.

 

Example 1:


Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18
Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.
Example 2:


Input: root = [1]
Output: 0
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
1 <= Node.val <= 100
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
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        s = [(root, None)]
        res = 0
        while s:
            node, parent = s.pop()
            if node is None:
                continue
            if parent and parent.val % 2 == 0:
                if node.left:
                    res += node.left.val
                if node.right:
                    res += node.right.val 
            s.append((node.right, node))
            s.append((node.left, node))
        return res


