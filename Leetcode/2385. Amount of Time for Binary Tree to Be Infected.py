'''
You are given the root of a binary tree with unique values, and an integer start. At minute 0, an infection starts from the node with value start.

Each minute, a node becomes infected if:

The node is currently uninfected.
The node is adjacent to an infected node.
Return the number of minutes needed for the entire tree to be infected.

 

Example 1:


Input: root = [1,5,3,null,4,10,6,9,2], start = 3
Output: 4
Explanation: The following nodes are infected during:
- Minute 0: Node 3
- Minute 1: Nodes 1, 10 and 6
- Minute 2: Node 5
- Minute 3: Node 4
- Minute 4: Nodes 9 and 2
It takes 4 minutes for the whole tree to be infected so we return 4.
Example 2:


Input: root = [1], start = 1
Output: 0
Explanation: At minute 0, the only node in the tree is infected so we return 0.
 

Constraints:

The number of nodes in the tree is in the range [1, 105].
1 <= Node.val <= 105
Each node has a unique value.
A node with a value of start exists in the tree.
'''

from typing import *

import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def dfs(node):
            if node is None:
                return 0, float('inf')
            
            left_time, left_dis = dfs(node.left)
            right_time, right_dis = dfs(node.right)
            
            if node.val == start:
                return max(left_time, right_time), 0
            if left_dis != float('inf'):
                # exist in the left tree
                return max(left_time, right_time + left_dis + 1), left_dis + 1
            if right_dis != float('inf'):
                # exist in the right tree
                return max(right_time, left_time + right_dis + 1), right_dis + 1
            return max(left_time, right_time) + 1, float('inf')
        return dfs(root)[0]


