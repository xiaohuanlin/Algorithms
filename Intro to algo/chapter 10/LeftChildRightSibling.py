import unittest
import unittest.mock
import io
from pprint import pprint


class Node:
    def __init__(self, name, value, parent=None, left_child=None, right_sibling=None):
        self.value = value
        self.name = name
        self.parent = parent
        self.left_child = left_child
        self.right_sibling = right_sibling

    def __repr__(self):
        return 'Node({}, {}, {}, {}, {})'.format(self.name, self.value, getattr(self.parent, 'name', None),
                                                 getattr(self.left_child, 'name', None),
                                                 getattr(self.right_sibling, 'name', None))

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.name == other.name and self.left_child == other.left_child and self.right_sibling == other.right_sibling


class LCRST:
    def __init__(self, data=None, root=None):
        if data is not None:
            values = data[0]
            self.root = Node(*values)
            self.list_to_tree(data[1:])
        else:
            self.root = root

    def list_to_tree(self, value_list):
        for values in value_list:
            self.insert(Node(*values), values[-1])

    def get_valid_tree(self):
        if self.root is None:
            return
        result = []
        if self.root.left_child is not None:
            result.extend(LCRST(root=self.root.left_child).get_valid_tree())
        result.append(self.root)
        if self.root.right_sibling is not None:
            result.extend(LCRST(root=self.root.right_sibling).get_valid_tree())
        return result

    def search(self, k):
        # complexity: O(lgn)
        if self.root is None or k == self.root.name:
            return self.root

        left_tree = LCRST(root=self.root.left_child)
        value = left_tree.search(k)
        if value is not None:
            return value

        right_tree = LCRST(root=self.root.right_sibling)
        value = right_tree.search(k)
        if value is not None:
            return value

    def insert(self, node: Node, parent):
        parent_node = self.search(parent)
        if parent_node is None:
            raise ValueError
        if parent_node.left_child is None:
            parent_node.left_child = node
        else:
            insert_node = parent_node.right_sibling
            left_insert_node = parent_node.left_child
            while insert_node:
                # insert node until None
                left_insert_node = insert_node
                insert_node = insert_node.right_sibling
            left_insert_node.right_sibling = node

        node.parent = parent_node


class TestSolution(unittest.TestCase):

    def test_LCRST(self):
        examples = (
            ((['derek', 0.1, None],
              ['ann', 0.5, 'derek'],
              ['nancy', 0.6, 'derek'],
              ['wayne', 0.25, 'nancy'],
              ['jamie', 0.4, 'nancy'],
              ),
             '[Node(ann, 0.5, derek, None, nancy),\n Node(wayne, 0.25, nancy, None, jamie),\n Node(jamie, 0.4, nancy, None, None),\n Node(nancy, 0.6, derek, wayne, None),\n Node(derek, 0.1, None, ann, None)]\n'
             ),
        )
        for first, second in examples:
            self.assert_LCRST(first, second)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_LCRST(self, first, second, mock_stdout=None):
        lcrst = LCRST(first)
        pprint(lcrst.get_valid_tree())
        self.assertEqual(mock_stdout.getvalue(), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
