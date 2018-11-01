'''

We want to use quad trees to store an N x N boolean grid. Each cell in the grid can only be true or false. The root node represents the whole grid. For each node, it will be subdivided into four children nodes until the values in the region it represents are all the same.

Each node has another two boolean attributes : isLeaf and val. isLeaf is true if and only if the node is a leaf node. The val attribute for a leaf node contains the value of the region it represents.

Your task is to use a quad tree to represent a given grid. The following example may help you understand the problem better:

Given the 8 x 8 grid below, we want to construct the corresponding quad tree:

The corresponding quad tree should be as following, where each node is represented as a (isLeaf, val) pair.

For the non-leaf nodes, val can be arbitrary, so it is represented as *.

'''
import unittest


# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        from operator import and_
        from functools import reduce
        n = len(grid)
        status = reduce(and_, (n for l in grid for n in l))
        if all(bool(n) == status for l in grid for n in l):
            return Node(bool(grid[0][0]), True, None, None, None, None)
        root = Node(
            '*',
            False,
            self.construct([row[:n // 2] for row in grid[:n // 2]]),
            self.construct([row[n // 2:] for row in grid[:n // 2]]),
            self.construct([row[:n // 2] for row in grid[n // 2:]]),
            self.construct([row[n // 2:] for row in grid[n // 2:]]),
        )
        return root


# class TestSolution(unittest.TestCase):
#
#     def test_construct(self):
#         examples = (
#             ([[1,1,1,1,0,0,0,0],
#               [1,1,1,1,0,0,0,0],
#               [1,1,1,1,1,1,1,1],
#               [1,1,1,1,1,1,1,1],
#               [1,1,1,1,0,0,0,0],
#               [1,1,1,1,0,0,0,0],
#               [1,1,1,1,0,0,0,0],
#               [1,1,1,1,0,0,0,0]], None),
#         )
#         for first, second in examples:
#             self.assert_function(first, second)
#
#     def assert_function(self, first, second):
#         self.assertEqual(Solution().construct(first), second, msg="first: {}; second: {}".format(first, second))
#
#
# unittest.main()