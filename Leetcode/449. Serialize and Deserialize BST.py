'''
Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You need to ensure that a binary search tree can be serialized to a string, and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

 

Example 1:

Input: root = [2,1,3]
Output: [2,1,3]
Example 2:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
0 <= Node.val <= 104
The input tree is guaranteed to be a binary search tree.
'''
from typing import *

import unittest
    
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if root is None:
            return ""
        return f"{root.val},{self.serialize(root.left)}{self.serialize(root.right)}"


    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        def insert(node, val):
            if node is None:
                return TreeNode(val)
            if val < node.val:
                node.left = insert(node.left, val)
            else:
                node.right = insert(node.right, val)
            return node

        i = 0
        n = 0
        root = TreeNode(float('inf'))
        while i < len(data):
            if data[i] == ',':
                insert(root, n)
                n = 0
            else:
                n = 10 * n + int(data[i])
            i += 1
        return root.left


