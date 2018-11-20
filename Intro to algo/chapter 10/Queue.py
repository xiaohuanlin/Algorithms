import unittest


class Queue:

    def __init__(self, data=None, size=10):
        self._queue = [0] * size
        self.size = size
        if data is not None:
            # initial data
            for index, num in enumerate(data):
                self._queue[index] = num
        else:
            data = []
        self.head = 0
        self.tail = len(data)

    def enqueue(self, x):
        # todo： check why can't realize the overflow check, because the condition of overflow and underflow seems exactly same
        # if self.tail == self.head:
        #     raise ValueError('overflow')
        self._queue[self.tail] = x
        self.tail += 1
        if self.tail >= self.size:
            # when tail large than length, we put the point to the first element
            self.tail = 0

    def dequeue(self):
        # todo： check why can't realize the overflow check
        # if self.head == self.tail:
        #     raise ValueError('underflow')
        x = self._queue[self.head]
        self.head += 1
        if self.head >= self.size:
            # when head large than length, we put the point to the first element
            self.head = 0
        return x

    def get_valid_queue(self):
        if self.head < self.tail:
            return self._queue[self.head:self.tail]
        else:
            return self._queue[self.head:] + self._queue[:self.tail]


class StackQueue:

    def __init__(self, data=None, size=10):
        self._master_queue = Queue(data, size)
        self._slave_queue = Queue()

    def empty(self):
        if self._master_queue.head == self._master_queue.tail:
            return True
        return False

    def push(self, x):
        self._master_queue.enqueue(x)

    def pop(self):
        # enqueue the dequeue element of _master_queue until only left one element
        if self.empty():
            raise ValueError('underflow')
        while self._master_queue.head + 1 != self._master_queue.tail:
            value = self._master_queue.dequeue()
            self._slave_queue.enqueue(value)
        pop_value = self._master_queue.dequeue()

        while self._slave_queue.head != self._slave_queue.tail:
            value = self._slave_queue.dequeue()
            self._master_queue.enqueue(value)
        return pop_value

    def get_valid_stack(self):
        return self._master_queue.get_valid_queue()


class TestSolution(unittest.TestCase):

    def test_stack(self):
        examples = (
            (([2, 8], 5, ('push', 1), ('pop',), ('empty',)), ([2, 8, 1], [2, 8], False)),
        )
        for first, second in examples:
            self.assert_stack(first, second)

    def assert_stack(self, first, second):
        data, size, *action = first
        stack = StackQueue(data, size)
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
            (([], 2, ('enqueue', 1), ('enqueue', 5), ('enqueue', 5),), ([1], [1, 5], [5])),
        )
        for first, second in examples:
            self.assert_queue(first, second)

    def assert_queue(self, first, second):
        data, size, *action = first
        queue = Queue(data, size)
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
