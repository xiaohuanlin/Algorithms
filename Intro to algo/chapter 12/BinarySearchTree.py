import unittest
import unittest.mock
import io


class BSTNode:
    def __init__(self, key, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent if left is not None else None
        self.left = BSTNode(left) if left is not None else None
        self.right = BSTNode(right) if right is not None else None

    def __repr__(self):
        return 'BSTNode({}, {}, {})'.format(self.key, getattr(self.parent, 'key', None), getattr(self.left, 'key', None), getattr(self.right, 'key', None))

    def __eq__(self, other):
        if isinstance(other, BSTNode):
            return self.key == other.key and self.left == other.left and self.right == other.right


class BST:
    def __init__(self, data=None, root=None):
        if data is not None:
            self.root = self.list_to_tree(data)[0]
        else:
            self.root = root

    def list_to_tree(self, key_list):
        '''
        :param key_list: the key_list
        :return: transferred list
        '''
        for i in range(len(key_list)):
            if key_list[i] is None:
                continue
            if isinstance(key_list[i], BSTNode):
                node = key_list[i]
            else:
                node = BSTNode(key_list[i])
                key_list[i] = node

            left_index, right_index = 2 * i + 1, 2 * (i + 1)
            if left_index < len(key_list) and key_list[left_index] is not None:
                node.left = BSTNode(key_list[left_index])
                key_list[left_index] = node.left
            if left_index < len(key_list) and key_list[right_index] is not None:
                node.right = BSTNode(key_list[right_index])
                key_list[right_index] = node.right
        return key_list

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

    def successor(self):
        # there are two kind of condition:
        # 1. the node have right child, and we can find the successor in this tree
        # 2. don't have right child, so we need seek from bottom to top until find the first node,
        # which is regarded as a left child.
        if self.root.right is not None:
            return BST(root=self.root.right).minimum()
        while


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
            (BST([6, 3, 8, 1, 5, None, 9]), '1\n3\n5\n6\n8\n9\n'),
        )
        for first, second in examples:
            self.assert_inorder_tree_walk(first, second)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_inorder_tree_walk(self, first, second, mock_stdout=None):
        inorder_tree_walk(first.root)
        self.assertEqual(mock_stdout.getvalue(), second)

    def test_BST(self):
        examples = (
            (([6, 3, 8, 1, 5, None, 9], ('search', 8), ('minimum',), ('maximum',)),
             (BSTNode(8, None, 9),
              BSTNode(1),
              BSTNode(9)
              )),
        )
        for first, second in examples:
            self.assert_BST(first, second)

    def assert_BST(self, first, second):
        data, *action = first
        bst = BST(data)
        for act, res in zip(action, second):
            func, *para = act

            result = getattr(bst, func)(*para)

            if func in ('search', 'minimum', 'maximum'):
                self.assertEqual(result, res,
                                 msg="first: {}; second: {}".format(first, second))
            else:
                self.assertEqual(bst.get_valid_tree(), res,
                                 msg="first: {}; second: {}".format(first, second))



unittest.main()
