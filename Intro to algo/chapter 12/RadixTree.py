import unittest


def radix_tree_sort():
    # todo:check it
    pass


class TestSolution(unittest.TestCase):

    def test_stack(self):
        examples = (
            (([2, 8], 5, ('push', 1), ('pop',), ('empty',)), ([2, 8, 1], [2, 8], False)),
            (([], 5, ('empty',), ('pop',), ('push', 1),), (True, ValueError, [1])),
        )
        for first, second in examples:
            self.assert_stack(first, second)

    def assert_stack(self, first, second):
        data, size, *action = first
        stack = Stack(data, size)
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
            (([], 2, ('dequeue',), ('enqueue', 1), ('enqueue', 5)), (ValueError, [1], [1, 5])),
        )
        for first, second in examples:
            self.assert_queue(first, second)

    def assert_queue(self, first, second):
        data, size, *action = first
        queue = QueueStack(data, size)
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
