import unittest
import unittest.mock
import io


class BSTNode:
    def __init__(self, key, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent if parent is not None else None
        self.left = BSTNode(left) if left is not None else None
        self.right = BSTNode(right) if right is not None else None

    def __repr__(self):
        return 'BSTNode({}, {}, {}, {})'.format(self.key, getattr(self.parent, 'key', None),
                                                getattr(self.left, 'key', None), getattr(self.right, 'key', None))

    def __eq__(self, other):
        if isinstance(other, BSTNode):
            return self.key == other.key and self.left == other.left and self.right == other.right


class BST:
    def __init__(self, data=None, root=None):
        if data is not None:
            data = sorted(data)
            key = data[len(data) // 2]
            self.root = BSTNode(key)
            self.list_to_tree(self.root, 'left', data[:len(data) // 2])
            self.list_to_tree(self.root, 'right', data[len(data) // 2 + 1:])
        else:
            self.root = root

    def list_to_tree(self, root_node, direction, key_list):

        if root_node is None or not key_list:
            return
        key = key_list[len(key_list) // 2]
        node = BSTNode(key, root_node)
        setattr(root_node, direction, node)

        self.list_to_tree(node, 'left', key_list[:len(key_list) // 2])
        self.list_to_tree(node, 'right', key_list[len(key_list) // 2 + 1:])

    def get_valid_tree(self):
        if self.root is None:
            return
        result = []
        if self.root.left is not None:
            result.extend(BST(root=self.root.left).get_valid_tree())
        result.append(self.root.key)
        if self.root.right is not None:
            result.extend(BST(root=self.root.right).get_valid_tree())
        return result

    def search(self, k):
        # complexity: O(lgn)
        if self.root is None or k == self.root.key:
            return self.root

        if k < self.root.key:
            tree = BST(root=self.root.left)
            return tree.search(k)
        else:
            tree = BST(root=self.root.right)
            return tree.search(k)

    def minimum(self):
        # complexity: O(lgn)
        node = self.root
        while node.left is not None:
            node = node.left
        return node

    def maximum(self):
        # complexity: O(lgn)
        node = self.root
        while node.right is not None:
            node = node.right
        return node

    def successor(self, node):
        # complexity: O(lgn)
        # there are two kind of condition:
        # 1. the node have right child, and we can find the successor in this tree
        # 2. don't have right child, so we need seek from bottom to top until find the first node,
        # which is regarded as a left child.
        if node.right is not None:
            return BST(root=node.right).minimum()
        parent, root = node.parent, node
        while parent is not None and root == parent.right:
            root, parent = parent, root.parent
        return parent

    def predecessor(self, node):
        # complexity: O(lgn)
        if node.left is not None:
            return BST(root=node.left).maximum()
        parent, root = node.parent, node
        while parent is not None and root == parent.left:
            root, parent = parent, root.parent
        return parent

    def insert(self, node: BSTNode):
        # complexity: O(lgn)
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

    def delete(self, node: BSTNode):
        # complexity: O(lgn)
        if node.left is None:
            # left is None or left and right both are None
            transplant(self, node, node.right)
        elif node.right is None:
            # only right is None
            transplant(self, node, node.left)
        else:
            # both are not None
            # 1. get the right child tree minimum
            new_node_tree = BST(root=node.right)
            new_node = new_node_tree.minimum()

            if new_node.parent != node:
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

    def delete_with_pre(self, node: BSTNode):
        # complexity: O(lgn)
        if node.right is None:
            # right is None or left and right both are None
            transplant(self, node, node.left)
        elif node.left is None:
            # only left is None
            transplant(self, node, node.right)
        else:
            # both are not None
            new_node_tree = BST(root=node.left)
            new_node = new_node_tree.maximum()

            if new_node.parent != node:
                transplant(self, new_node, new_node.left)
                # attach the left child of old node to new node
                new_node.left = node.left
                new_node.left.parent = new_node

            # new_node substitute the old node
            transplant(self, node, new_node)
            # attach the right child of old node to new node
            new_node.right = node.right
            new_node.right.parent = new_node


def transplant(tree: BST, old_node: BSTNode, new_node: BSTNode):
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

# def is_BST(tree: BST):
#     stack = [tree.root]
#     while stack:
#         node = stack.pop()
#         if (node.left is not None and node.left.key > node.key) or \
#                 (node.right is not None and node.right.key < node.key):
#             return False
#         if node.left is not None:
#             stack.append(node.left)
#         if node.right is not None:
#             stack.append(node.right)
#     return True


def inorder_tree_walk(x: BSTNode):
    if x is None:
        return
    inorder_tree_walk(x.left)
    print(x.key)
    inorder_tree_walk(x.right)


class TestSolution(unittest.TestCase):

    def test_inorder_tree_walk(self):
        examples = (
            (BST([6, 3, 8, 1, 5, 9]), '1\n3\n5\n6\n8\n9\n'),
        )
        for first, second in examples:
            self.assert_inorder_tree_walk(first, second)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_inorder_tree_walk(self, first, second, mock_stdout=None):
        inorder_tree_walk(first.root)
        self.assertEqual(mock_stdout.getvalue(), second)

    def test_BST(self):
        examples = (
            (([6, 3, 8, 1, 5, 9],
              ('search', 8),
              ('minimum',),
              ('maximum',),
              ('successor', 3),
              ('predecessor', 3),
              ('insert', BSTNode(7)),
              ('delete', 3),
              ('delete_with_pre', 8),
              ),
             (8,
              1,
              9,
              5,
              1,
              [1, 3, 5, 6, 7, 8, 9],
              [1, 5, 6, 7, 8, 9],
              [1, 5, 6, 7, 9]
              )),
            (([6, 3, 8, 1, 5, 9, 23, 56, 33, 46, 77, 88],
              ('delete', 3),
              ('delete', 23),
              ('delete_with_pre', 77),
              ),
             ([1, 5, 6, 8, 9, 23, 33, 46, 56, 77, 88],
              [1, 5, 6, 8, 9, 33, 46, 56, 77, 88],
              [1, 5, 6, 8, 9, 33, 46, 56, 88],
              )),
        )
        for first, second in examples:
            self.assert_BST(first, second)

    def assert_BST(self, first, second):
        data, *action = first
        bst = BST(data)
        for act, res in zip(action, second):
            func, *para = act
            if func in ('successor', 'predecessor'):
                node = bst.search(*para)
                self.assertEqual(getattr(bst, func)(node).key, res,
                                 msg="first: {}; second: {}".format(first, second))
            elif func in ('insert',):
                getattr(bst, func)(*para)
                self.assertEqual(bst.get_valid_tree(), res,
                                 msg="first: {}; second: {}".format(first, second))
            elif func in ('delete', 'delete_with_pre'):
                node = bst.search(*para)
                getattr(bst, func)(node)
                self.assertEqual(bst.get_valid_tree(), res,
                                 msg="first: {}; second: {}".format(first, second))
            else:
                result = getattr(bst, func)(*para)
                self.assertEqual(result.key, res,
                                 msg="first: {}; second: {}".format(first, second))


unittest.main()
