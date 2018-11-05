'''

Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.

'''
import unittest


class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
    #     if s is None and t is None:
    #         return True
    #     if s is None or t is None:
    #         return False
    #     return self.same(s, t) or \
    #            self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    #
    #
    # def same(self, s, t):
    #     if s is None and t is None:
    #         return True
    #
    #     if s is None or t is None:
    #         return False
    #
    #     if s.val != t.val:
    #         return False
    #
    #     return self.same(s.left, t.left) and self.same(s.right, t.right)
    # ----------------------------------------------------------
        return self.get_answer(s, t, False)

    def get_answer(self, s, t, same_status):
        if s is None and t is None:
            return True
        if s is None or t is None:
            return False
        if same_status and s.val != t.val:
            return False
        if s.val == t.val:
            if self.get_answer(s.left, t.left, True) and self.get_answer(s.right, t.right, True):
                return True
        return self.get_answer(s.left, t, False) or self.get_answer(s.right, t, False)