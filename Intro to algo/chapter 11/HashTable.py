import unittest


class Slot:
    def __init__(self, key=None, satellite=None):
        self.key = key or None
        self.satellite = satellite or None

    @property
    def empty(self):
        return self.key is None

    def __repr__(self):
        return 'Slot({}, {})'.format(self.key, self.satellite)

    def __eq__(self, other):
        if other is None:
            return self.key is None and self.satellite is None
        if isinstance(other, Slot):
            return self.key == other.key and self.satellite == other.satellite
        else:
            raise NotImplemented


class SlotNode(Slot):

    def __init__(self, key, satellite):
        super().__init__(key, satellite)
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

    def insert(self, x: SlotNode):
        # complexity: O(1)
        # consider this kind of point have two direction
        x.next = self.head
        if self.head is not None:
            self.head.pre = x
        # revise the list head to x
        self.head = x
        x.pre = None

    def delete(self, x: SlotNode):
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

    def __eq__(self, other):
        if isinstance(other, LinkedList):
            return self.get_valid_list() == other.get_valid_list()
        else:
            return self.get_valid_list() == other

    def __repr__(self):
        x = self.head
        result = []
        while x is not None:
            result.append(x)
            x = x.next
        return result.__repr__()


class DirectAddressTable:

    def __init__(self, data, size=10):
        self.size = size
        self._slots = [None] * size
        for index, data_pair, in enumerate(data):
            self._slots[index] = Slot(*data_pair)

    def search(self, k):
        assert k < self.size, 'k mush less than table size'
        return self._slots[k]

    def insert(self, x: Slot):
        self._slots[x.key] = x

    def delete(self, x: Slot):
        self._slots[x.key] = None

    def get_valid_table(self):
        return self._slots


class ChainedHashTable:
    '''
    it is very similar to Secondary hash table, which have better performance on search speed
    '''

    def __init__(self, data, size=10):
        self.size = size
        self._slots = [[] for _ in range(size)]

        for index, list_data_pair, in enumerate(data):
            linked_list = LinkedList()
            for data_pair in list_data_pair:
                linked_list.insert(SlotNode(*data_pair))
            self._slots[index] = linked_list

    def hash(self, x):
        return x % self.size

    def search(self, k):
        slot_num = self.hash(k)
        slot_list = self._slots[slot_num]
        return slot_list.search(k)

    def insert(self, x: Slot):
        self._slots[self.hash(x.key)].insert(x)

    def delete(self, x: Slot):
        slot_num = self.hash(x.key)
        slot_list = self._slots[slot_num]
        # slot list can be []
        slot_list.delete(x)

    def get_valid_table(self):
        return self._slots


class TestSolution(unittest.TestCase):
    def test_direct_address_table(self):
        examples = (
            (([(), (), (2, 5), (), (), (5, 1)], 6,
              ('search', 1),
              ('search', 2),
              ('insert', Slot(1, 3)),
              ('delete', 5)),
             (Slot(None, None),
              Slot(2, 5),
              [None, Slot(1, 3), Slot(2, 5), None, None, Slot(5, 1)],
              [None, Slot(1, 3), Slot(2, 5), None, None, None])),
        )
        for first, second in examples:
            self.assert_direct_address_table(first, second)

    def assert_direct_address_table(self, first, second):
        data, size, *action = first
        direct_address_table = DirectAddressTable(data=data, size=size)

        for act, res in zip(action, second):
            func, para = act
            if func == 'delete':
                # search the node and then delete it
                slot = direct_address_table.search(para)
                direct_address_table.delete(slot)
                self.assertEqual(direct_address_table.get_valid_table(), res,
                                 msg="first: {}; second: {}".format(first, second))
            else:
                result = getattr(direct_address_table, func)(para)

                if func == 'search':
                    self.assertEqual(result, res,
                                     msg="first: {}; second: {}".format(first, second))
                else:
                    self.assertEqual(direct_address_table.get_valid_table(), res,
                                     msg="first: {}; second: {}".format(first, second))

    def test_chained_hash_table(self):
        examples = (
            (([(), (), [(2, 5), (8, 7)], (), (), [(5, 1), (11, 3)]], 6,
              ('search', 1),
              ('search', 2),
              ('insert', Slot(1, 3)),
              ('insert', Slot(14, 8)),
              ('delete', 8)),
             (None,
              Slot(2, 5),
              [[], [Slot(1, 3)], [Slot(2, 5), Slot(8, 7)], [], [], [Slot(5, 1), Slot(11, 3)]],
              [[], [Slot(1, 3)], [Slot(2, 5), Slot(8, 7), Slot(14, 8)], [], [], [Slot(5, 1), Slot(11, 3)]],
              [[], [Slot(1, 3)], [Slot(2, 5), Slot(14, 8)], [], [], [Slot(5, 1), Slot(11, 3)]],
              )),
        )
        for first, second in examples:
            self.assert_chained_hash_table(first, second)

    def assert_chained_hash_table(self, first, second):
        data, size, *action = first
        chained_hash_table = ChainedHashTable(data=data, size=size)

        for act, res in zip(action, second):
            #deal with res data
            if isinstance(res, list):
                for index in range(len(res)):
                    linked_list = LinkedList()
                    for slot in res[index]:
                        linked_list.insert(slot)
                    res[index] = linked_list

            func, para = act

            if func == 'delete':
                # search the node and then delete it
                slot = chained_hash_table.search(para)
                chained_hash_table.delete(slot)
                self.assertEqual(chained_hash_table.get_valid_table(), res,
                                 msg="first: {}; second: {}".format(first, second))
            else:
                result = getattr(chained_hash_table, func)(para)

                if func == 'search':
                    self.assertEqual(result, res,
                                     msg="first: {}; second: {}".format(first, second))
                else:
                    self.assertEqual(chained_hash_table.get_valid_table(), res,
                                     msg="first: {}; second: {}".format(first, second))


unittest.main()
