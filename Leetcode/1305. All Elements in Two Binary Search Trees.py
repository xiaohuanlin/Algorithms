'''
Given two binary search trees root1 and root2, return a list containing all the integers from both trees sorted in ascending order.

 

Example 1:


Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]
Example 2:


Input: root1 = [1,null,8], root2 = [8,1]
Output: [1,1,8,8]
 

Constraints:

The number of nodes in each tree is in the range [0, 5000].
-105 <= Node.val <= 105
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
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:

        def to_list(root, l):
            if root is None:
                return
            to_list(root.left, l)
            l.append(root.val)
            to_list(root.right, l)
        
        list1 = []
        list2 = []
        to_list(root1, list1)
        to_list(root2, list2)
        res = []
        i = 0
        j = 0
        
        while i < len(list1) or j < len(list2):
            if i >= len(list1):
                res.append(list2[j])
                j += 1
            elif j >= len(list2):
                res.append(list1[i])
                i += 1
            else:
                if list1[i] < list2[j]:
                    res.append(list1[i])
                    i += 1
                else:
                    res.append(list2[j])
                    j += 1
        return res
        
