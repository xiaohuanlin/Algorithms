'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
'''
import unittest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # if root is None:
        #     return 0

        # node = root
        # depth = node.depth = 1

        # while True:
        #     if node.left is not None and not hasattr(node.left, 'parent'):
        #         new_node = node.left
        #         new_node.parent = node
        #         new_node.depth = node.depth + 1
        #         node = new_node
        #     elif node.right is not None and not hasattr(node.right, 'parent'):
        #         new_node = node.right
        #         new_node.parent = node
        #         new_node.depth = node.depth + 1
        #         node = new_node
        #     else:
        #         if node.depth > depth:
        #             depth = node.depth
        #         if hasattr(node, 'parent'):
        #             node = node.parent
        #         else:
        #             break
        # return depth
        # --------------------------------------------
        def max_depth(node, depth):
            if node is None:
                return depth

            return max(max_depth(node.left, depth + 1), max_depth(node.right, depth + 1))
        
        return max_depth(root, 1)
        # --------------------------------------------

        


class TestSolution(unittest.TestCase):

    def test_maxDepth(self):
        examples = (

        )
        for first,second in examples:
            self.assert_function(first, second)
        
    def assert_function(self, first, second):
        self.assertEqual(Solution().maxDepth(*first), second)

unittest.main()