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


class Interval:
    def __init__(self, min_v, max_v):
        self.low = min_v
        self.high = max_v

    def __lt__(self, other):
        if isinstance(other, Interval):
            return self.low < other.low
        return False

    def __eq__(self, other):
        if isinstance(other, Interval):
            return self.low == other.low and self.high == other.high
        return False

    def __repr__(self):
        return '{}({}, {})'.format(self.__class__.__name__, self.low, self.high)

    def is_overlap(self, other):
        if isinstance(other, Interval):
            return not (self.low > other.high or self.high < other.low)
        raise NotImplemented

    def exactly_same(self, other):
        if isinstance(other, Interval):
            return self.low == other.low and self.high == other.high
        raise NotImplemented


class NilInterval(Interval, Nil):
    def __init__(self):
        self.low = float('-inf')
        self.high = float('-inf')


class IntervalNode(RBNode):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.max = self.key.high

    def __repr__(self):
        return 'IntervalNode({}, {}, {}, {}, {}, {})'.format(self.key, self.color, self.max, getattr(self.parent, 'key', None),
                                                getattr(self.left, 'key', None), getattr(self.right, 'key', None))


class IntervalTree(RedBlackTree):

    def __init__(self, data=None, root=None):
        if not hasattr(self, 'nil_node'):
            nil_node = IntervalNode(NilInterval(), color=Color.BLACK)
            self.nil_node = nil_node
        if data is not None:
            interval = Interval(*data[0])
            self.root = IntervalNode(interval, color=Color.BLACK, parent=self.nil_node, left=self.nil_node, right=self.nil_node)
            self.list_to_tree(data[1:])
        else:
            self.root = root

    def list_to_tree(self, key_list):
        for num in key_list:
            interval = Interval(*num)
            node = IntervalNode(interval, color=Color.RED, left=self.nil_node, right=self.nil_node)
            self.insert(node)

    def search(self, i: Interval):
        node = self.root
        while node != self.nil_node and not node.key.is_overlap(i):
            # print(node, i, node.left.max, i.low)
            if node.left != self.nil_node and node.left.max >= i.low:
                # in this case, we will find the smallest value of overlap node
                node = node.left
            else:
                node = node.right
        return node

    def exactly_search(self, i: Interval):
        node = self.root
        while node != self.nil_node and not node.key.exactly_same(i):
            # print(node, i, node.left.max, i.low)
            if node.left != self.nil_node and node.left.max >= i.low:
                # in this case, we will find the smallest value of overlap node
                node = node.left
            else:
                node = node.right
        return node

    def get_valid_tree(self, detail=False):
        if self.root == self.nil_node:
            return
        result = []
        if self.root.left != self.nil_node:
            result.extend(self.__class__(root=self.root.left).get_valid_tree(detail=detail))

        if detail:
            result.append((self.root.key, self.root.color, self.root.max, self.root.parent))
        else:
            result.append((self.root.key, self.root.color, self.root.max))
        if self.root.right != self.nil_node:
            result.extend(self.__class__(root=self.root.right).get_valid_tree(detail=detail))
        return result

    def left_rotate(self, node: IntervalNode):
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

        # update the max value
        rotate_node.max = node.max
        node.max = max(node.left.max, node.right.max, node.key.high)
        return

    def right_rotate(self, node: IntervalNode):
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

        # update the max value
        rotate_node.max = node.max
        node.max = max(node.left.max, node.right.max, node.key.high)
        return

    def insert(self, node: IntervalNode):
        root = self.root
        last_node = self.nil_node
        while root != self.nil_node:
            # because after node has been substituted by its child, we can't know the origin root
            last_node = root
            # maintain the feature
            root.max = max(node.max, root.max)
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


def transplant(tree: IntervalTree, old_node: IntervalNode, new_node: IntervalNode):
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

    # fix the max until root
    fix_node = old_node.parent
    while fix_node != tree.root:
        fix_node.max = max(fix_node.left.max, fix_node.right.max, fix_node.max)
        fix_node = fix_node.parent


class TestSolution(unittest.TestCase):

    def test_RedBlackTree(self):
        examples = (
            (([[6, 9], [3, 10], [8, 8], [1, 2], [5, 7], [9, 20], [23, 38], [56, 59], [33, 50], [46, 50], [77, 80], [88, 90]],
              ('search', [2, 5]),
              ('insert', [15, 23]),
              ('delete', [23, 38]),
              ),
             ([3, 10],
              [(Interval(1, 2), Color.RED, 2), (Interval(3, 10), Color.BLACK, 10),
               (Interval(5, 7), Color.RED, 7), (Interval(6, 9), Color.BLACK, 10), (Interval(8, 8), Color.BLACK, 8),
               (Interval(9, 20), Color.BLACK, 90), (Interval(15, 23), Color.RED, 23),
               (Interval(23, 38), Color.BLACK, 38), (Interval(33, 50), Color.BLACK, 90),
               (Interval(46, 50), Color.BLACK, 50), (Interval(56, 59), Color.RED, 90),
               (Interval(77, 80), Color.BLACK, 90), (Interval(88, 90), Color.RED, 90)],
              [(Interval(1, 2), Color.RED, 2), (Interval(3, 10), Color.BLACK, 10),
               (Interval(5, 7), Color.RED, 7), (Interval(6, 9), Color.BLACK, 10), (Interval(8, 8), Color.BLACK, 8),
               (Interval(9, 20), Color.BLACK, 90), (Interval(15, 23), Color.BLACK, 23),
               (Interval(33, 50), Color.BLACK, 90), (Interval(46, 50), Color.BLACK, 50),
               (Interval(56, 59), Color.RED, 90), (Interval(77, 80), Color.BLACK, 90),
               (Interval(88, 90), Color.RED, 90)],
              )),
        )
        for first, second in examples:
            self.assert_RedBlackTree(first, second)

    def assert_RedBlackTree(self, first, second):
        data, *action = first
        it = IntervalTree(data)
        nil_node = IntervalNode(NilInterval(), color=Color.BLACK)
        for act, res in zip(action, second):
            func, *para = act
            if func == 'delete':
                inter = Interval(*para[0])
                node = it.exactly_search(inter)
                getattr(it, func)(node)
                self.assertEqual(it.get_valid_tree(), res,
                                 msg="first: {}; second: {}".format(first, second))
            elif func == 'search':
                inter = Interval(*para[0])
                result = getattr(it, func)(inter)
                self.assertEqual(result.key, Interval(*res),
                                 msg="first: {}; second: {}".format(first, second))
            else:
                inter = Interval(*para[0])
                node = IntervalNode(inter, left=nil_node, right=nil_node)
                getattr(it, func)(node)
                self.assertEqual(it.get_valid_tree(), res,
                                 msg="first: {}; second: {}".format(first, second))


unittest.main()
