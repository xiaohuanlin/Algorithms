'''

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
'''
import unittest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def __str__(self):
        return str(self.val)

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # def reverse(parent, child):
        #     if child is None:
        #         return parent
        #     tmp = child.next
        #     child.next = parent
        #     return reverse(child, tmp)
        # return reverse(None, head)
        # ------------------------------
        parent, child = None, head
        while True:
            if child is None:
                return parent
            tmp = child.next
            child.next = parent
            parent, child = child, tmp


class TestSolution(unittest.TestCase):
    
    def to_interval(self, num_list):
        tmp = ori = ListNode(num_list[0])
        for i in num_list[1:]:
            tmp.next = ListNode(i)
            tmp = tmp.next
        return ori

    def test_reverseList(self):
        ex_1, ex_2, ex_3, ex_4 = ListNode(1), ListNode(2), ListNode(3), ListNode(4)
        ex_1.next = ex_2
        ex_2.next = ex_3
        ex_3.next = ex_4
        examples = (
            (ex_1, ex_4),
        )
        for first,second in examples:
            self.assert_function(first, second)
        
    def assert_function(self, first, second):
        self.assertEqual(Solution().reverseList(first), second)

unittest.main()