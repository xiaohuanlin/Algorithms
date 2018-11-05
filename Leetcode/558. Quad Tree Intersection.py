'''

A quadtree is a tree data in which each internal node has exactly four children: topLeft, topRight, bottomLeft and bottomRight. Quad trees are often used to partition a two-dimensional space by recursively subdividing it into four quadrants or regions.

We want to store True/False information in our quad tree. The quad tree is used to represent a N * N boolean grid. For each node, it will be subdivided into four children nodes until the values in the region it represents are all the same. Each node has another two boolean attributes : isLeaf and val. isLeaf is true if and only if the node is a leaf node. The val attribute for a leaf node contains the value of the region it represents.

For example, below are two quad trees A and B:

A:
+-------+-------+   T: true
|       |       |   F: false
|   T   |   T   |
|       |       |
+-------+-------+
|       |       |
|   F   |   F   |
|       |       |
+-------+-------+
topLeft: T
topRight: T
bottomLeft: F
bottomRight: F

B:
+-------+---+---+
|       | F | F |
|   T   +---+---+
|       | T | T |
+-------+---+---+
|       |       |
|   T   |   F   |
|       |       |
+-------+-------+
topLeft: T
topRight:
     topLeft: F
     topRight: F
     bottomLeft: T
     bottomRight: T
bottomLeft: T
bottomRight: F


Your task is to implement a function that will take two quadtrees and return a quadtree that represents the logical OR (or union) of the two trees.

A:                 B:                 C (A or B):
+-------+-------+  +-------+---+---+  +-------+-------+
|       |       |  |       | F | F |  |       |       |
|   T   |   T   |  |   T   +---+---+  |   T   |   T   |
|       |       |  |       | T | T |  |       |       |
+-------+-------+  +-------+---+---+  +-------+-------+
|       |       |  |       |       |  |       |       |
|   F   |   F   |  |   T   |   F   |  |   T   |   F   |
|       |       |  |       |       |  |       |       |
+-------+-------+  +-------+-------+  +-------+-------+
Note:

Both A and B represent grids of size N * N.
N is guaranteed to be a power of 2.
If you want to know more about the quad tree, you can refer to its wiki.
The logic OR operation is defined as this: "A or B" is true if A is true, or if B is true, or if both A and B are true.

'''
import unittest


# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

    def __str__(self):
        return 'Node({}, {},\n\t {},\n\t {},\n\t {},\n\t {})'.format(self.val, self.isLeaf, self.topLeft, self.topRight, self.bottomLeft, self.bottomRight)


class Solution:
    def intersect(self, quadTree1, quadTree2):
        """
        :type quadTree1: Node
        :type quadTree2: Node
        :rtype: Node
        """
        if quadTree1.isLeaf and quadTree2.isLeaf:
            return Node(
                quadTree1.val or quadTree2.val,
                True,
                None,
                None,
                None,
                None
            )
        if quadTree1.isLeaf:
            if quadTree1.val:
                return quadTree1
            else:
                return quadTree2
        if quadTree2.isLeaf:
            return self.intersect(quadTree2, quadTree1)

        topLeft = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
        topRight = self.intersect(quadTree1.topRight, quadTree2.topRight)
        bottomLeft = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
        bottomRight = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)

        val = sum(node.val for node in (topLeft, topRight, bottomLeft, bottomRight))

        if topLeft.isLeaf and topRight.isLeaf and bottomLeft and bottomRight:
            if val == 0 or val == 4:
                return Node(
                    bool(val),
                    True,
                    None,
                    None,
                    None,
                    None
                )
        return Node(
            quadTree1.val or quadTree2.val,
            quadTree1.isLeaf and quadTree2.isLeaf,
            topLeft,
            topRight,
            bottomLeft,
            bottomRight
        )


a = Node(
    True,
    False,
    Node(
        True,
        True,
        None,
        None,
        None,
        None
    ),
    Node(
        True,
        True,
        None,
        None,
        None,
        None
    ),
    Node(
        False,
        True,
        None,
        None,
        None,
        None
    ),
    Node(
        False,
        True,
        None,
        None,
        None,
        None
    )
)

b = Node(
    True,
    False,
    Node(
        True,
        True,
        None,
        None,
        None,
        None
    ),
    Node(
        True,
        False,
        Node(
            False,
            True,
            None,
            None,
            None,
            None
        ),
        Node(
            False,
            True,
            None,
            None,
            None,
            None
        ),
        Node(
            True,
            True,
            None,
            None,
            None,
            None
        ),
        Node(
            True,
            True,
            None,
            None,
            None,
            None
        )
    ),
    Node(
        True,
        True,
        None,
        None,
        None,
        None
    ),
    Node(
        False,
        True,
        None,
        None,
        None,
        None
    )
)

c = Solution().intersect(a, b)
print(c)