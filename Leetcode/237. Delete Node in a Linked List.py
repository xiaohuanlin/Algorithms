'''
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Given linked list -- head = [4,5,1,9], which looks like following:

    4 -> 5 -> 1 -> 9
Example 1:

Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list
             should become 4 -> 1 -> 9 after calling your function.
Example 2:

Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list
             should become 4 -> 5 -> 9 after calling your function.
Note:

The linked list will have at least two elements.
All of the nodes' values will be unique.
The given node will not be the tail and it will always be a valid node of the linked list.
Do not return anything from your function.

'''
import unittest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


class TestSolution(unittest.TestCase):
    def to_interval(self, num_list):
        tmp = ori = ListNode(num_list[0])
        for i in num_list[1:]:
            tmp.next = ListNode(i)
            tmp = tmp.next
        return ori
    
    def test_deleteNode(self):
        examples = (
            (self.to_interval([4,5,1,9]), 4),
            (self.to_interval([4,5,1,9]), 4),
        )
        for first,second in examples:
            self.assert_function(first, second)
        
    def assert_function(self, first, second):
        self.assertEqual(Solution().deleteNode(*first), second)

unittest.main()