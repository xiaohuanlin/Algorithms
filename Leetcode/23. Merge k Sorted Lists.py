'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
'''

from lib2to3.pytree import Node
from typing import *

import unittest
from queue import PriorityQueue

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        mem = {}
        pq = PriorityQueue()
        for node in lists:
            if node is None:
                continue
            pq.put(node.val)
            mem.setdefault(node.val, []).append(node)
        
        iter = dummy = ListNode()
        while not pq.empty():
            node = pq.get()
            iter.next = ListNode(node)
            iter = iter.next
            next_ = mem[node].pop().next
            if next_:
                pq.put(next_.val)
                mem[next_.val] = next_
        return dummy.next

