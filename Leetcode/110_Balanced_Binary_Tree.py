'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
'''
import unittest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def get_tree_hight(node):
            if node == None:
                return 0
            return max(get_tree_hight(node.left), get_tree_hight(node.right)) + 1
        
        if root == None:
            return True

        if self.isBalanced(root.left) and self.isBalanced(root.right):
            return abs(get_tree_hight(root.left)-get_tree_hight(root.right)) <= 1

        return False


class TestSolution(unittest.TestCase):

    def test_isBalanced(self):
        examples = (

        )
        for first,second in examples:
            self.assert_function(first, second)
        
    def assert_function(self, first, second):
        self.assertEqual(Solution().isBalanced(*first), second)

unittest.main()