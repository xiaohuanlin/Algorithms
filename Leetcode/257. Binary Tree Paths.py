'''
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []
        result = []
        self.dfs(root, "", result)
        return result

    def dfs(self, root, pre_str, result):
        if root.left is None and root.right is None:
            result.append(pre_str + str(root.val))
        if root.left:
            self.dfs(root.left, pre_str + str(root.val) + "->", result)
        if root.right:
            self.dfs(root.right, pre_str + str(root.val) + "->", result)
