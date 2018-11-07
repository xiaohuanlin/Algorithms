'''

Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Example 1:
Input:
    2
   / \
  2   5
     / \
    5   7

Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.
Example 2:
Input:
    2
   / \
  2   2

Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.

'''
import unittest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # if root is None:
        #     return -1
        # old_queue = [root]
        # new_queue = []
        # min_list = []
        # while old_queue:
        #     for node in old_queue:
        #         if node.left is not None:
        #             new_queue.append(node.left)
        #         if node.right is not None:
        #             new_queue.append(node.right)
        #     min_list.extend([node.val for node in new_queue if node.val > root.val])
        #     old_queue = new_queue
        #     new_queue = []
        # if min_list:
        #     return min(min_list)
        # return -1
        # ---------------------------------------------------
        def get_answer(root):
            if root is None:
                return []
            result = set(get_answer(root.left)+[root.val]+get_answer(root.right))
            return sorted(result)[:2]
        answer = get_answer(root)
        # print(answer)
        if len(answer) < 2:
            return -1
        return answer[1]
