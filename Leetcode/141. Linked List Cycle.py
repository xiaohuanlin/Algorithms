'''

Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
'''

import unittest

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # node_list = []
        # while head:
        #     if id(head) not in node_list:
        #         node_list.append(id(head))
        #     else:
        #         return True
        #     head = head.next
        # return False
        # ------------------------------------
        # Fast and Slow point
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


class TestSolution(unittest.TestCase):

    def test_hasCycle(self):
        examples = (
            ([2,2,1], 1),
            ([4,1,2,1,2], 4),
        )
        for first,second in examples:
            self.assert_function(first, second)
        
    def assert_function(self, first, second):
        self.assertEqual(Solution().hasCycle(first), second)

unittest.main()