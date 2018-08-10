'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
'''
import unittest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not hasattr(head, 'next'):
            return head

        copy = head
        while head.next is not None:
            
            if head.next.val == head.val:
                head.next = head.next.next
                continue

            head = head.next
                            
            if not hasattr(head, 'next'):
                break

        return copy


class TestSolution(unittest.TestCase):

    def test_deleteDuplicates(self):
        e_1, e_2, e_3 = ListNode(1), ListNode(1), ListNode(2)
        e_1.next = e_2
        e_2.next = e_3
        examples = (
            (e_1, '1'),
        )
        for first,second in examples:
            self.assert_function(first, second)
        
    def assert_function(self, first, second):
        self.assertEqual(Solution().deleteDuplicates(first), second)

unittest.main()