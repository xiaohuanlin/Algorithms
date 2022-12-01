'''
You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i], return true if and only if all the given nodes form exactly one valid binary tree.

If node i has no left child then leftChild[i] will equal -1, similarly for the right child.

Note that the nodes have no values and that we only use the node numbers in this problem.

 

Example 1:


Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
Output: true
Example 2:


Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
Output: false
Example 3:


Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
Output: false
 

Constraints:

n == leftChild.length == rightChild.length
1 <= n <= 104
-1 <= leftChild[i], rightChild[i] <= n - 1
'''
from typing import *

import unittest

from collections import defaultdict
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        graph = defaultdict(list)
        in_degrees = [0 for _ in range(n)]
        for i in range(n):
            if leftChild[i] != -1:
                graph[i].append(leftChild[i])
                in_degrees[leftChild[i]] += 1
            if rightChild[i] != -1:
                graph[i].append(rightChild[i])
                in_degrees[rightChild[i]] += 1
            
        root = None
        for i in range(n):
            if in_degrees[i] == 0:
                if root is None:
                    root = i    
                else:
                    return False
            elif in_degrees[i] == 2:
                return False
        if root is None:
            return False

        visited = [0 for _ in range(n)]        
        def dfs(node):
            if visited[node] == 1:
                return False
            visited[node] = 1
            for next_node in graph[node]:
                if not dfs(next_node):
                    return False
            visited[node] = 2
            return True
        
        if not dfs(root):
            return False
        
        for i in visited:
            if i == 0:
                return False
        return True

        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            ((4, [1,-1,3,-1], [2,-1,-1,-1]), True),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().validateBinaryTreeNodes(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()


