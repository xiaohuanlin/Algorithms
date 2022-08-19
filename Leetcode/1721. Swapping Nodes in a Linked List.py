'''
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]
Example 2:

Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]
 

Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 105
0 <= Node.val <= 100
'''

from typing import *

import unittest


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = fast = head
        slow_parent = fast_parent = dummy
        
        count = 1
        
        first = first_parent = None
        while fast:
            if count == k:
                first = fast
                first_parent = fast_parent
                
            if count > k:
                slow = slow.next
                slow_parent = slow_parent.next
            count += 1
            fast = fast.next
            fast_parent = fast_parent.next
        
        # same node
        if slow == first:
            return dummy.next
        
        # neighbor node
        if slow.next == first:
            slow.next = first.next
            first.next = slow
            slow_parent.next = first
            return dummy.next
            
        if first.next == slow:
            first.next = slow.next
            slow.next = first
            first_parent.next = slow
            return dummy.next
        
        slow_next = slow.next
        slow.next = first.next
        first_parent.next = slow
        
        first.next = slow_next
        slow_parent.next = first
        return dummy.next

