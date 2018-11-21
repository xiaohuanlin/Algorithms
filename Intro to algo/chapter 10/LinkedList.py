import unittest


class Node:

    def __init__(self, key):
        self.key = key
        self.pre = None
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def search(self, k):
        # complexity: O(n), if we can't find k, it will return None as result
        x = self.head
        while x is not None and x.key != k:
            x = x.next
        return x

    def insert(self, x: Node):
        # complexity: O(1)
        # consider this kind of point have two direction
        x.next = self.head
        if self.head is not None:
            self.head.pre = x
        # revise the list head to x
        self.head = x
        x.pre = None

    def delete(self, x: Node):
        # complexity: O(1)
        if x.pre is not None:
            x.pre.next = x.next
        else:
            self.head = x.next

        if x.next is not None:
            x.next.pre = x.pre

    def get_valid_list(self):
        x = self.head
        result = []
        while x is not None:
            result.append(x.key)
            x = x.next
        return result


class StackList:
    def __init__(self, data):
        self.linked_list = LinkedList()
        for num in data:
            self.linked_list.insert(Node(num))

    def empty(self):
        return self.linked_list.head is None

    def push(self, x):
        self.linked_list.insert(Node(x))

    def pop(self):
        return self.linked_list.delete(self.linked_list.head)

    def get_valid_stack(self):
        return self.linked_list.get_valid_list()[::-1]


class QueueList:
    def __init__(self, data):
        self.linked_list = LinkedList()
        if data is not None and data != []:
            self.head = Node(data[0])
            self.linked_list.insert(self.head)
            for num in data[1:]:
                self.linked_list.insert(Node(num))
        else:
            self.head = None

    def enqueue(self, x):
        self.linked_list.insert(Node(x))

    def dequeue(self):
        old_head = self.head
        # it use the pre as the point, maybe we can use next realize this function
        self.head = self.head.pre
        self.linked_list.delete(old_head)
        return old_head.key

    def get_valid_queue(self):
        return self.linked_list.get_valid_list()[::-1]


def compactify_list(L:LinkedList, F:LinkedList, n):
    '''
    by swapping the element of L and F, get the compact list. In this case, it will make the key of
    element from 1 to m.

    :param L: the allocate list
    :param F: the free list
    :param n: amount of L
    :return: new L and F
    '''
    l_node, f_node = L.head, F.head
    while l_node is not None and f_node is not None:
        while l_node is not None and l_node.key <= n:
            l_node = l_node.next
        while f_node is not None and f_node.key > n:
            f_node = f_node.next
        # swap nodes and maintain two list
        copy_node = f_node

        if l_node.pre is not None:
            l_node.pre.next = f_node
        else:
            L.head = f_node
        if l_node.next is not None:
            l_node.next.pre = f_node

        if copy_node.pre is not None:
            copy_node.pre.next = l_node
        else:
            F.head = l_node
        if copy_node.next is not None:
            copy_node.next.pre = l_node
    return L, F


class TestSolution(unittest.TestCase):
    def test_linked_list(self):
        examples = (
            (([3, 5, 1, 23, 5, 1], ('search', 1), ('search', 100), ('insert', Node(50)), ('delete', 5)),
             (1, None, [50, 3, 5, 1, 23, 5, 1], [50, 3, 1, 23, 5, 1])),
        )
        for first, second in examples:
            self.assert_linked_list(first, second)

    def assert_linked_list(self, first, second):
        data, *action = first
        linked_list = LinkedList()
        for num in data[::-1]:
            node = Node(num)
            linked_list.insert(node)

        for act, res in zip(action, second):
            func, para = act

            if func == 'delete':
                # search the node and then delete it
                node = linked_list.search(para)
                linked_list.delete(node)
                self.assertEqual(linked_list.get_valid_list(), res,
                                 msg="first: {}; second: {}".format(first, second))
            else:
                result = getattr(linked_list, func)(para)

                if func == 'search':
                    self.assertEqual(getattr(result, 'key', None), res,
                                     msg="first: {}; second: {}".format(first, second))
                else:
                    self.assertEqual(linked_list.get_valid_list(), res,
                                     msg="first: {}; second: {}".format(first, second))

    def test_stack(self):
        examples = (
            (([2, 8], 5, ('push', 1), ('pop',), ('empty',)), ([2, 8, 1], [2, 8], False)),
            (([], 5, ('empty',), ('push', 1),), (True, [1])),
        )
        for first, second in examples:
            self.assert_stack(first, second)

    def assert_stack(self, first, second):
        data, size, *action = first
        stack = StackList(data)
        for act, res in zip(action, second):
            func, *para = act
            if isinstance(res, type):
                with self.assertRaises(res, msg="first: {}; second: {}".format(first, second)):
                    getattr(stack, func)(*para)
                continue
            else:
                result = getattr(stack, func)(*para)

            if func == 'empty':
                self.assertEqual(result, res,
                                 msg="first: {}; second: {}".format(first, second))
            else:
                self.assertEqual(stack.get_valid_stack(), res,
                                 msg="first: {}; second: {}".format(first, second))

    def test_queue(self):
        examples = (
            (([2, 8], 3, ('dequeue',), ('enqueue', 1), ('enqueue', 5), ('dequeue',)), (2, [8, 1], [8, 1, 5], 8)),
            (([], 2, ('enqueue', 1), ('enqueue', 5)), ([1], [1, 5])),
        )
        for first, second in examples:
            self.assert_queue(first, second)

    def assert_queue(self, first, second):
        data, size, *action = first
        queue = QueueList(data)
        for act, res in zip(action, second):
            func, *para = act
            if isinstance(res, type):
                with self.assertRaises(res, msg="first: {}; second: {}".format(first, second)):
                    getattr(queue, func)(*para)
                continue
            else:
                result = getattr(queue, func)(*para)

            if func == 'dequeue':
                self.assertEqual(result, res,
                                 msg="first: {}; second: {}".format(first, second))
            else:
                self.assertEqual(queue.get_valid_queue(), res,
                                 msg="first: {}; second: {}".format(first, second))


unittest.main()
