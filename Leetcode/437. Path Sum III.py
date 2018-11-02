'''

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11

'''
import unittest


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # def pathSum(self, root, sum):
    #     """
    #     :type root: TreeNode
    #     :type sum: int
    #     :rtype: int
    #     """
    #     return self.get_answer(root, sum, False)
    #
    # def get_answer(self, root, sum, status):
    #     # if sum - root.val, then all descendants should keep sum-root.val.
    #     if root is None:
    #         return 0
    #     count = 0
    #     if root.val == sum:
    #         count += 1
    #     if status:
    #         return count + self.get_answer(root.left, sum - root.val, True) + self.get_answer(root.right, sum - root.val, True)
    #     return count + self.get_answer(root.left, sum, False) + self.get_answer(root.left, sum - root.val, True) \
    #            + self.get_answer(root.right, sum, False) + self.get_answer(root.right, sum - root.val, True)
    #     ---------------------------------------
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        return self.search(0, root, sum, {0: 1})

    def search(self, sum_value, root, sum, cache):
        if root is None:
            return 0
        # update cache value number
        root_val = sum_value + root.val
        # check if cache have the certain value
        value = root_val - sum
        count = cache.get(value, 0)

        cache[root_val] = cache.setdefault(root_val, 0) + 1
        return count + self.search(root_val, root.left, sum, cache.copy()) + self.search(root_val, root.right, sum, cache.copy())

