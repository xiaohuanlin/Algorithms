import unittest
import unittest.mock
from enum import Enum, auto
from typing import Optional


class Color(Enum):
    RED = auto()
    BLACK = auto()


class RBNode:

    def __init__(self, key, color=None, parent=None, left=None, right=None):
        self.key = key
        self.color = color
        self.parent = parent if parent is not None else None
        self.left = RBNode(left) if left is not None else None
        self.right = RBNode(right) if right is not None else None

    def __repr__(self):
        return 'RBNode({}, {}, {}, {}, {})'.format(self.key, self.color, getattr(self.parent, 'key', None),
                                                getattr(self.left, 'key', None), getattr(self.right, 'key', None))

    def __eq__(self, other):
        if isinstance(other, RBNode):
            return self.key == other.key and self.color == other.color and self.left == other.left and self.right == other.right


class RedBlackTree:
    def __init__(self, data=None, root=None):
        if data is not None:
            key = data[0]
            self.root = RBNode(key, color=Color.BLACK)
            self.list_to_tree(data[1:])
        else:
            self.root = root

    def list_to_tree(self, key_list):
        for num in key_list:
            node = RBNode(num, color=Color.RED)
            self.insert(node)

    def get_valid_tree(self):
        if self.root is None:
            return
        result = []
        if self.root.left is not None:
            result.extend(RedBlackTree(root=self.root.left).get_valid_tree())
        # result.append((self.root.key, self.root.color))
        result.append((self.root.key, self.root.color, self.root.parent))
        if self.root.right is not None:
            result.extend(RedBlackTree(root=self.root.right).get_valid_tree())
        return result

    def search(self, k):
        # complexity: O(lgn)
        if self.root is None or k == self.root.key:
            return self.root

        if k < self.root.key:
            tree = RedBlackTree(root=self.root.left)
            return tree.search(k)
        else:
            tree = RedBlackTree(root=self.root.right)
            return tree.search(k)

    def left_rotate(self, node: RBNode):
        rotate_node = node.right

        # connect the left child of rotate node with node
        node.right = rotate_node.left
        if rotate_node.left is not None:
            rotate_node.left.parent = node

        # connect the node parent with rotate node
        rotate_node.parent = node.parent
        if node.parent is None:
            # empty tree
            self.root = rotate_node
        elif node.parent.left == node:
            # node is left child of node parent
            node.parent.left = rotate_node
        else:
            # node is right child of node parent
            node.parent.right = rotate_node

        # connect node and rotate node
        rotate_node.left = node
        node.parent = rotate_node
        return

    def right_rotate(self, node: RBNode):
        rotate_node = node.left

        # connect the right child of rotate node with node
        node.left = rotate_node.right
        if rotate_node.right is not None:
            rotate_node.right.parent = node

        # connect the node parent with rotate node
        rotate_node.parent = node.parent
        if node.parent is None:
            # empty tree
            self.root = rotate_node
        elif node.parent.left == node:
            # node is left child of node parent
            node.parent.left = rotate_node
        else:
            # node is right child of node parent
            node.parent.right = rotate_node

        # connect node and rotate node
        rotate_node.right = node
        node.parent = rotate_node
        return

    def insert(self, node: RBNode):
        root = self.root
        if root is None:
            # empty tree
            self.root = node
            return

        root_copy = root
        while root:
            # because after node has been substituted by its child, we can't know the origin root
            root_copy = root
            if node.key < root.key:
                root = root.left
            else:
                root = root.right

        node.parent = root_copy

        # revise the parent node information
        if node.key < root_copy.key:
            root_copy.left = node
        else:
            root_copy.right = node
        # ---------------------------------------------------
        # that is the additional code
        node.color = Color.RED
        self.insert_fix_up(node)

    def insert_fix_up(self, node: RBNode):
        # complexity: O(lgn)
        while getattr(node.parent, 'color', Color.BLACK) == Color.RED:
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if getattr(uncle, 'color', Color.BLACK) == Color.RED:
                    # when uncle color is red, we need change those into black to satisfy the feature 4
                    node.parent.color = Color.BLACK
                    uncle.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    # NOTICE: keep all features and reduce the scalar of problem by 2
                    node = node.parent.parent
                else:
                    # NOTICE: after this action, the color of node parent is black, so program end
                    if node == node.parent.right:
                        # so we can left rotate and make it to next situation
                        node = node.parent
                        self.left_rotate(node)

                    node.parent.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    self.right_rotate(node.parent.parent)
            else:
                # same as before except the direction. We should put all data to right, and left rotate
                uncle = node.parent.parent.left
                if getattr(uncle, 'color', Color.BLACK) == Color.RED:
                    # when uncle color is red, we need change those into black to satisfy the feature 4
                    node.parent.color = Color.BLACK
                    uncle.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    # NOTICE: keep all features and reduce the scalar of problem by 2
                    node = node.parent.parent
                else:
                    # NOTICE: after this action, the color of node parent is black, so program end
                    if node == node.parent.left:
                        # so we can left rotate and make it to next situation
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    self.left_rotate(node.parent.parent)

        # make sure feature 2 can't be violated
        self.root.color = Color.BLACK

    def minimum(self):
        # complexity: O(lgn)
        node = self.root
        while node.left is not None:
            node = node.left
        return node

    def delete(self, node: RBNode):
        # complexity: O(lgn)
        new_node_color = node.color

        if node.left is None:
            # left is None or left and right both are None
            fix_up_node = node.right
            transplant(self, node, fix_up_node)
        elif node.right is None:
            # only right is None
            fix_up_node = node.left
            transplant(self, node, fix_up_node)
        else:
            # both are not None
            # get the right child tree minimum
            new_node_tree = RedBlackTree(root=node.right)
            new_node = new_node_tree.minimum()
            new_node_color = new_node.color
            fix_up_node = new_node.right

            if new_node.parent == node:
                # todo: it seems don't have any work
                fix_up_node.parent = new_node
            else:
                # this means the new node have left child, because if it has, the minimum won't be it
                # all we need to do is to transplant the node.right to its parent
                transplant(self, new_node, new_node.right)
                # attach the right child of old node to new node
                new_node.right = node.right
                new_node.right.parent = new_node

            # new_node substitute the old node
            transplant(self, node, new_node)
            # attach the left child of old node to new node
            new_node.left = node.left
            new_node.left.parent = new_node
            new_node.color = node.color

        if new_node_color == Color.BLACK:
            # deal with the core node, which will be the child of node parent
            print(self.get_valid_tree())
            self.delete_fix_up(fix_up_node)

    def delete_fix_up(self, node: RBNode):
        # todo: add null node to update this method
        while node != self.root and getattr(node, 'color', Color.BLACK) == Color.BLACK:
            if node == node.parent.left:
                brother = node.parent.right
                if getattr(brother, 'color', Color.BLACK) == Color.RED:
                    # to make the brother color to be black
                    brother.color = Color.BLACK
                    node.parent.color = Color.RED
                    self.left_rotate(node.parent)
                    # update brother node
                    brother = node.parent.right
                if brother.left.color == Color.BLACK and brother.right.color == Color.BLACK:
                    # every child have black color, we change it and make node.parent become new node
                    # so that its parent will have a extra black color, which was absorbed from its children
                    # NOTICE: reduce the scale of the problem
                    brother.color = Color.RED
                    node = node.parent
                else:
                    if brother.right.color == Color.BLACK:
                        # to make the brother right child become red
                        brother.left.color = Color.BLACK
                        brother.color = Color.RED
                        self.right_rotate(brother)
                        # update brother node
                        brother = node.parent.right
                    # in this case, we need cancel the extra color of node, so we change color and end loop
                    brother.color = node.parent.color
                    node.parent.color = Color.BLACK
                    brother.right.color = Color.BLACK
                    self.left_rotate(node.parent)
                    # end the loop
                    node = self.root
            else:
                brother = node.parent.left
                if getattr(brother, 'color', Color.BLACK) == Color.RED:
                    brother.color = Color.BLACK
                    node.parent.color = Color.RED
                    self.right_rotate(node.parent)
                    brother = node.parent.left
                if brother.left.color == Color.BLACK and brother.right.color == Color.BLACK:
                    brother.color = Color.RED
                    node = node.parent
                else:
                    if brother.left.color == Color.BLACK:
                        brother.right.color = Color.BLACK
                        brother.color = Color.RED
                        self.left_rotate(brother)
                        brother = node.parent.left
                    brother.color = node.parent.color
                    node.parent.color = Color.BLACK
                    brother.right.color = Color.BLACK
                    self.right_rotate(node.parent)
                    node = self.root
        node.color = Color.BLACK


def transplant(tree: RedBlackTree, old_node: RBNode, new_node: RBNode):
    # same with the BST
    # change the old node of a tree into new node
    if old_node.parent is None:
        # old node is the root of tree
        tree.root = new_node
    elif old_node == old_node.parent.left:
        old_node.parent.left = new_node
    else:
        old_node.parent.right = new_node

    if new_node is not None:
        new_node.parent = old_node.parent


class TestSolution(unittest.TestCase):

    def test_RedBlackTree(self):
        examples = (
            # (([6, 3, 8, 1, 5, 9, 23, 56, 33, 46, 77, 88],
            #   ('left_rotate', 3),
            #   ('insert', 100)
            #   ),
            #  ([(1, Color.RED), (3, Color.BLACK), (5, Color.RED), (6, Color.BLACK), (8, Color.BLACK),
            #    (9, Color.BLACK), (23, Color.BLACK), (33, Color.BLACK), (46, Color.BLACK),
            #    (56, Color.RED), (77, Color.BLACK), (88, Color.RED)],
            #   [(1, Color.RED), (3, Color.BLACK), (5, Color.RED), (6, Color.BLACK), (8, Color.BLACK),
            #    (9, Color.BLACK), (23, Color.BLACK), (33, Color.BLACK), (46, Color.BLACK),
            #    (56, Color.RED), (77, Color.RED), (88, Color.BLACK), (100, Color.RED)]
            #   )),
            (([41, 38, 31, 12, 19, 8],
              # ('insert', 8),
              ('delete', 8),
              ('delete', 12)),
             (
              # [(8, Color.RED), (12, Color.BLACK), (19, Color.RED), (31, Color.BLACK),
              #  (38, Color.BLACK), (41, Color.BLACK)],
              [(12, Color.BLACK), (19, Color.RED), (31, Color.BLACK),
               (38, Color.BLACK), (41, Color.BLACK)]
              )
             ),
        )
        for first, second in examples:
            self.assert_RedBlackTree(first, second)

    def assert_RedBlackTree(self, first, second):
        data, *action = first
        rbt = RedBlackTree(data)
        for act, res in zip(action, second):
            func, *para = act
            if func in ('delete', 'left_rotate'):
                node = rbt.search(*para)
                getattr(rbt, func)(node)
                # print(rbt.get_valid_tree())
                # self.assertEqual(rbt.get_valid_tree(), res,
                #                  msg="first: {}; second: {}".format(first, second))
            else:
                node = RBNode(*para)
                getattr(rbt, func)(node)
                # print(rbt.get_valid_tree())
                self.assertEqual(rbt.get_valid_tree(), res,
                                 msg="first: {}; second: {}".format(first, second))


unittest.main()
