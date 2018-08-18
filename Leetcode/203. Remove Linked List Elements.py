'''
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
'''
import unittest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return []

        dummy_header = ListNode(None)
        dummy_header.next = head
        head = dummy_header

        while dummy_header and dummy_header.next:
            if dummy_header.next.val == val:
                dummy_header.next = dummy_header.next.next
            else:
                dummy_header = dummy_header.next
        
        return head.next



class TestSolution(unittest.TestCase):

    def test_removeElements(self):
        ex_1 = ListNode(1)
        examples = (
            ((ex_1, 1),ex_1),
        )
        for first,second in examples:
            self.assert_function(first, second)
        
    def assert_function(self, first, second):
        self.assertEqual(Solution().removeElements(*first), second)

unittest.main()