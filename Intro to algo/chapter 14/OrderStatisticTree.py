import unittest
from enum import Enum, auto


class Nil:

    def __eq__(self, other):
        if isinstance(other, Nil):
            return True
        return False

    def __repr__(self):
        return 'nil({})'.format(None)


class Color(Enum):
    RED = auto()
    BLACK = auto()


class RBNode:

    def __init__(self, key, color=None, parent=None, left=None, right=None):
        self.key = key
        self.color = color
        self.parent = parent if parent is not None else None
        self.left = left if left is not None else None
        self.right = right if right is not None else None

    def __repr__(self):
        return 'RBNode({}, {}, {}, {}, {})'.format(self.key, self.color, getattr(self.parent, 'key', None),
                                                getattr(self.left, 'key', None), getattr(self.right, 'key', None))

    def __eq__(self, other):
        if isinstance(other, RBNode):
            if self.key != Nil() and other.key != Nil():
                return self.key == other.key and self.color == other.color and self.left == other.left and self.right == other.right
            else:
                return self.key == other.key and self.color == other.color
        return False


class RedBlackTree:
    def __init__(self, data=None, root=None):
        if not hasattr(self, 'nil_node'):
            nil_node = RBNode(Nil(), color=Color.BLACK)
            self.nil_node = nil_node
        if data is not None:
            key = data[0]
            self.root = RBNode(key, color=Color.BLACK, parent=self.nil_node, left=self.nil_node, right=self.nil_node)
            self.list_to_tree(data[1:])
        else:
            self.root = root

    def list_to_tree(self, key_list):
        for num in key_list:
            node = RBNode(num, color=Color.RED, left=self.nil_node, right=self.nil_node)
            self.insert(node)

    def get_valid_tree(self, detail=False):
        if self.root == self.nil_node:
            return
        result = []
        if self.root.left != self.nil_node:
            result.extend(self.__class__(root=self.root.left).get_valid_tree(detail=detail))

        if detail:
            result.append((self.root.key, self.root.color, self.root.parent))
        else:
            result.append((self.root.key, self.root.color))
        if self.root.right != self.nil_node:
            result.extend(self.__class__(root=self.root.right).get_valid_tree(detail=detail))
        return result

    def search(self,  k):
        # complexity: O(lgn)
        if self.root == self.nil_node or k == self.root.key:
            return self.root

        if k < self.root.key:
            tree = self.__class__(root=self.root.left)
            return tree.search(k)
        else:
            tree = self.__class__(root=self.root.right)
            return tree.search(k)

    def left_rotate(self, node: RBNode):
        rotate_node = node.right

        # connect the left child of rotate node with node
        node.right = rotate_node.left
        if rotate_node.left != self.nil_node:
            rotate_node.left.parent = node

        # connect the node parent with rotate node
        rotate_node.parent = node.parent
        if node.parent == self.nil_node:
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
        if rotate_node.right != self.nil_node:
            rotate_node.right.parent = node

        # connect the node parent with rotate node
        rotate_node.parent = node.parent
        if node.parent == self.nil_node:
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
        last_node = self.nil_node
        while root != self.nil_node:
            # because after node has been substituted by its child, we can't know the origin root
            last_node = root
            if node.key < root.key:
                root = root.left
            else:
                root = root.right

        node.parent = last_node

        if last_node == self.nil_node:
            # empty tree
            self.root = node
        # revise the parent node information
        elif node.key < last_node.key:
            last_node.left = node
        else:
            last_node.right = node
        # ---------------------------------------------------
        # that is the additional code
        node.color = Color.RED
        self.insert_fix_up(node)

    def insert_fix_up(self, node: RBNode):
        # complexity: O(lgn)
        while node.parent.color == Color.RED:
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == Color.RED:
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
                if uncle.color == Color.RED:
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
        if node == self.nil_node:
            return node
        while node.left != self.nil_node:
            node = node.left
        return node

    def delete(self, node: RBNode):
        # complexity: O(lgn)
        new_node_color = node.color

        if node.left == self.nil_node:
            # left is None or left and right both are None
            fix_up_node = node.right
            transplant(self, node, fix_up_node)
        elif node.right == self.nil_node:
            # only right is None
            fix_up_node = node.left
            transplant(self, node, fix_up_node)
        else:
            # both are not None
            # get the right child tree minimum
            new_node_tree = self.__class__(root=node.right)
            new_node = new_node_tree.minimum()
            new_node_color = new_node.color
            fix_up_node = new_node.right

            if new_node.parent == node:
                # it can change the nil node parent and let the next stage of deleting work well
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
            self.delete_fix_up(fix_up_node)

    def delete_fix_up(self, node: RBNode):

        while node != self.root and node.color == Color.BLACK:
            if node == node.parent.left:
                brother = node.parent.right
                if node.color == Color.RED:
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
                if node.color == Color.RED:
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


class OrderNode(RBNode):
    def __init__(self, *args, **kwargs):
        self.size = kwargs.pop('size')
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return 'OrderNode({}, {}, {}, {}, {}, {})'.format(self.key, self.color, self.size, getattr(self.parent, 'key', None),
                                                getattr(self.left, 'key', None), getattr(self.right, 'key', None))


class OrderStaticTree(RedBlackTree):

    def __init__(self, data=None, root=None):
        if not hasattr(self, 'nil_node'):
            nil_node = OrderNode(Nil(), color=Color.BLACK, size=0)
            self.nil_node = nil_node
        if data is not None:
            key = data[0]
            self.root = OrderNode(key, color=Color.BLACK, size=1, parent=self.nil_node, left=self.nil_node, right=self.nil_node)
            self.list_to_tree(data[1:])
        else:
            self.root = root

    def list_to_tree(self, key_list):
        for num in key_list:
            node = OrderNode(num, color=Color.RED, size=1, left=self.nil_node, right=self.nil_node)
            self.insert(node)

    def select(self, i):
        """
        :param self: the root of a tree
        :param i: the i-th min node
        :return: OrderNode
        """
        r = self.root.left.size + 1
        if i == r:
            return self.root
        elif i < r:
            return self.__class__(root=self.root.left).select(i)
        else:
            return self.__class__(root=self.root.right).select(i - r)

    def loop_select(self, i):
        root = self.root
        r = root.left.size + 1
        while i != r:
            if i < r:
                root = root.left
            else:
                i = i - (root.left.size + 1)
                root = root.right

            r = root.left.size + 1
        return root

    def rank(self, node: OrderNode):
        r = node.left.size + 1
        test_node = node
        while test_node != self.root:
            if test_node == test_node.parent.right:
                # if node locates in the right side of parent node, then we need add the size_sum of left part.
                r = r + test_node.parent.left.size + 1
            test_node = test_node.parent
        return r

    def get_valid_tree(self, detail=False):
        if self.root == self.nil_node:
            return
        result = []
        if self.root.left != self.nil_node:
            result.extend(self.__class__(root=self.root.left).get_valid_tree(detail=detail))

        if detail:
            result.append((self.root.key, self.root.color, self.root.size, self.root.parent))
        else:
            result.append((self.root.key, self.root.color, self.root.size))
        if self.root.right != self.nil_node:
            result.extend(self.__class__(root=self.root.right).get_valid_tree(detail=detail))
        return result

    def left_rotate(self, node: OrderNode):
        rotate_node = node.right

        # connect the left child of rotate node with node
        node.right = rotate_node.left
        if rotate_node.left != self.nil_node:
            rotate_node.left.parent = node

        # connect the node parent with rotate node
        rotate_node.parent = node.parent
        if node.parent == self.nil_node:
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

        # update the size value
        rotate_node.size = node.size
        node.size = node.left.size + node.right.size + 1
        return

    def right_rotate(self, node: OrderNode):
        rotate_node = node.left

        # connect the right child of rotate node with node
        node.left = rotate_node.right
        if rotate_node.right != self.nil_node:
            rotate_node.right.parent = node

        # connect the node parent with rotate node
        rotate_node.parent = node.parent
        if node.parent == self.nil_node:
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

        # update the size value
        rotate_node.size = node.size
        node.size = node.left.size + node.right.size + 1
        return

    def insert(self, node: RBNode):
        root = self.root
        last_node = self.nil_node
        while root != self.nil_node:
            # because after node has been substituted by its child, we can't know the origin root
            last_node = root
            # change the size information
            root.size += 1
            if node.key < root.key:
                root = root.left
            else:
                root = root.right

        node.parent = last_node

        if last_node == self.nil_node:
            # empty tree
            self.root = node
        # revise the parent node information
        elif node.key < last_node.key:
            last_node.left = node
        else:
            last_node.right = node
        # ---------------------------------------------------
        # that is the additional code
        node.color = Color.RED
        self.insert_fix_up(node)


def transplant(tree: OrderStaticTree, old_node: OrderNode, new_node: OrderNode):
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

    # fix the size until root
    fix_node = old_node.parent
    while fix_node != tree.root:
        fix_node.size = fix_node.left.size + fix_node.right.size + 1
        fix_node = fix_node.parent


class TestSolution(unittest.TestCase):

    def test_RedBlackTree(self):
        examples = (
            (([6, 3, 8, 1, 5, 9, 23, 56, 33, 46, 77, 88],
              ('select', 3),
              ('loop_select', 3),
              ('rank', 9),
              ('insert', 44),
              ('rank', 44),
              ('delete', 23),
              ('rank', 44),
              ),
             (5,
              5,
              6,
              [(1, Color.RED, 1), (3, Color.BLACK, 3), (5, Color.RED, 1),
               (6, Color.BLACK, 5), (8, Color.BLACK, 1), (9, Color.BLACK, 13), (23, Color.BLACK, 1), (33, Color.BLACK, 7),
               (44, Color.RED, 1), (46, Color.BLACK, 2),
               (56, Color.RED, 5), (77, Color.BLACK, 2), (88, Color.RED, 1)],
              9,
              [(1, Color.RED, 1), (3, Color.BLACK, 3), (5, Color.RED, 1),
               (6, Color.RED, 5), (8, Color.BLACK, 1), (9, Color.BLACK, 13), (33, Color.BLACK, 6),
               (44, Color.RED, 1), (46, Color.BLACK, 2),
               (56, Color.RED, 5), (77, Color.BLACK, 2), (88, Color.RED, 1)]
              ,
              8
              )),
        )
        for first, second in examples:
            self.assert_RedBlackTree(first, second)

    def assert_RedBlackTree(self, first, second):
        data, *action = first
        ost = OrderStaticTree(data)
        nil_node = OrderNode(Nil(), color=Color.BLACK, size=0)
        for act, res in zip(action, second):
            func, *para = act
            if func in ('delete', 'left_rotate'):
                node = ost.search(*para)
                getattr(ost, func)(node)
                self.assertEqual(ost.get_valid_tree(), res,
                                 msg="first: {}; second: {}".format(first, second))
            elif func in ('select', 'loop_select'):
                result = getattr(ost, func)(*para)
                node = ost.search(res)
                self.assertEqual(result, node,
                                 msg="first: {}; second: {}".format(first, second))
            elif func == 'rank':
                node = ost.search(*para)
                result = getattr(ost, func)(node)
                self.assertEqual(result, res,
                                 msg="first: {}; second: {}".format(first, second))
            else:
                node = OrderNode(*para, size=1, left=nil_node, right=nil_node)
                getattr(ost, func)(node)
                print(ost.get_valid_tree())
                self.assertEqual(ost.get_valid_tree(), res,
                                 msg="first: {}; second: {}".format(first, second))


unittest.main()
