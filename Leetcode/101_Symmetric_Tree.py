'''

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.

'''

import unittest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def pair_match(contray_x, contray_y):

            if contray_x is None and contray_y is None:
                # if the pair are both None, we think it is true
                return True
                
            elif contray_x is not None and contray_y is not None:
                if contray_x.val != contray_y.val:
                    # we need check the value of both
                    return False

                else:
                    return pair_match(contray_x.left, contray_y.right) and pair_match(contray_x.right, contray_y.left)

            return False
        
        if root is None:
            return True
        
        return pair_match(root.left, root.right)


class TestSolution(unittest.TestCase):

    def test_isSymmetric(self):
        examples = (

        )
        for first,second in examples:
            self.assert_function(first, second)
        
    def assert_function(self, first, second):
        self.assertEqual(Solution().isSymmetric(*first), second)

unittest.main()