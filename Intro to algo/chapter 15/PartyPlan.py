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


def party_plan(root: Node):
    without_dict = {}
    with_dict = {}
    with_select = {}
    without_select = {}
    with_value, with_choice = get_max_without_root(with_select, without_select, with_dict, without_dict, root)
    without_value, without_choice = get_max_with_root(with_select, without_select, with_dict, without_dict, root)
    print(without_dict)
    print(without_select)
    print(with_dict)
    print(with_select)
    if with_value > without_value:
        max_value = with_value
        initial_choice = with_choice
    else:
        max_value = without_value
        initial_choice = without_choice
    return max_value, initial_choice


def get_max_without_root(with_select, without_select, with_dict, without_dict, root: Node):
    if root.name in without_dict:
        return without_dict[root.name], without_select[root.name]

    # calculate the sum of all child values
    with_value = 0
    child_node = root.left_child
    with_children_list = []
    while child_node is not None:
        value, node_list = get_max_with_root(with_select, without_select, with_dict, without_dict, child_node)
        with_value += value
        with_children_list.extend(node_list)
        child_node = child_node.right_sibling

    without_value = 0
    child_node = root.left_child
    without_children_list = []
    while child_node is not None:
        value, node_list = get_max_without_root(with_select, without_select, with_dict, without_dict, child_node)
        without_value += value
        without_children_list.extend(node_list)
        child_node = child_node.right_sibling

    if with_value > without_value:
        without_dict[root.name] = with_value
        without_select[root.name] = with_children_list
    else:
        without_dict[root.name] = without_value
        without_select[root.name] = without_children_list

    return without_dict[root.name], without_select[root.name]


def get_max_with_root(with_select, without_select, with_dict, without_dict, root: Node):
    if root.name in with_dict:
        return with_dict[root.name], with_select[root.name]

    without_value = root.value
    child_node = root.left_child
    children_list = [root.name]
    while child_node is not None:
        value, node_list = get_max_without_root(with_select, without_select, with_dict, without_dict, child_node)
        without_value += value
        children_list.extend(node_list)
        child_node = child_node.right_sibling

    with_dict[root.name] = without_value
    with_select[root.name] = children_list
    return with_dict[root.name], with_select[root.name]


class TestSolution(unittest.TestCase):

    def test_party_plan(self):
        examples = (
            ((['derek', 0.1, None],
              ['ann', 0.5, 'derek'],
              ['nancy', 0.6, 'derek'],
              ['wayne', 0.25, 'nancy'],
              ['jamie', 0.4, 'nancy'],
              ),
             (1.1,
              ['ann', 'nancy'])),
        )
        for first, second in examples:
            self.assert_party_plan(first, second)

    def assert_party_plan(self, first, second):
        lcrst = LCRST(first)
        self.assertEqual(party_plan(lcrst.root), second,
                         msg="first: {}; second: {}".format(first, second))


def print_list(l):
    from copy import deepcopy
    c_l = deepcopy(l)
    max_length = max(len(str(data)) for row in c_l for data in row)
    spe = '{:<' + str(max_length) + '}'
    for row in c_l:
        for i in range(len(row)):
            if row[i] is None:
                row[i] = 'None'
            row[i] = spe.format(row[i])
    pprint(c_l, width=(max_length + 5) * len(c_l[0]))


unittest.main()
