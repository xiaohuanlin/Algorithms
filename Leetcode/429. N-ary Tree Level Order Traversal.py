'''

Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example, given a 3-ary tree:

We should return its level order traversal:

[
     [1],
     [3,2,4],
     [5,6]
]


Note:

The depth of the tree is at most 1000.
The total number of nodes is at most 5000.

'''
import unittest


# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        queue = [(root, 0)]
        result = [[root.val]]
        while queue:
            chi_list = []
            root, level = queue.pop(0)
            # you need connect with the list if level is same
            for chi in root.children:
                chi_list.append(chi.val)
                queue.append((chi, level+1))
            if chi_list:
                if len(result) <= level + 1:
                    result.append(chi_list)
                else:
                    result[level+1].extend(chi_list)
        return result
