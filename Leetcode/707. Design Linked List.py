'''

Design your implementation of the linked list. You can choose to use the singly linked list or the doubly linked list. A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node. If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement these functions in your linked list class:

get(index) : Get the value of the index-th node in the linked list. If the index is invalid, return -1.
addAtHead(val) : Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
addAtTail(val) : Append a node of value val to the last element of the linked list.
addAtIndex(index, val) : Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
deleteAtIndex(index) : Delete the index-th node in the linked list, if the index is valid.
Example:

MyLinkedList linkedList = new MyLinkedList();
linkedList.addAtHead(1);
linkedList.addAtTail(3);
linkedList.addAtIndex(1, 2);  // linked list becomes 1->2->3
linkedList.get(1);            // returns 2
linkedList.deleteAtIndex(1);  // now the linked list is 1->3
linkedList.get(1);            // returns 3
Note:

All values will be in the range of [1, 1000].
The number of operations will be in the range of [1, 1000].
Please do not use the built-in LinkedList library.

'''

class Node:
    def __init__(self, val, pre):
        self.val = val
        self.pre = pre

    def __repr__(self):
        return '{}'.format(self.val)

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = []


    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if 0 <= index < len(self.list):
            return self.list[index].val
        return -1

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        node = Node(val, None)
        if len(self.list) > 0:
            self.list[0].pre = node
        self.list.insert(0, node)

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        if len(self.list) > 0:
            node = Node(val, self.list[-1])
        else:
            node = Node(val, None)
        self.list.append(node)

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index < len(self.list):
            pre_node = self.list[index-1]
            cur_node = self.list[index]
            node = Node(val, pre_node)
            cur_node.pre = node
            self.list.insert(index, node)
        elif index == len(self.list):
            self.addAtTail(val)

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if index == 0:
            self.list[1].pre = None
        elif index < len(self.list) - 1:
            pre_node = self.list[index-1]
            nex_node = self.list[index+1]
            nex_node.pre = pre_node
        if index < len(self.list):
            self.list.pop(index)

# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()

obj.addAtHead(1)
print(obj.list)
# obj.addAtTail(2)
# print(obj.list)
obj.addAtIndex(1, 2)
# obj.addAtIndex(5, 5)
print(obj.list)
# obj.deleteAtIndex(1)
# print(obj.list)

# param_1 = obj.get(2)
# print(param_1)