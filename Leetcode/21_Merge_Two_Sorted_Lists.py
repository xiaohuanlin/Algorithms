# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

'''
import unittest

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(-1)
        copy = result
        while l1 and l2:
            if l1.val < l2.val:
                result.next = l1
                l1 = l1.next
            else:
                result.next = l2
                l2 = l2.next
            result = result.next

        if l1:
            result.next = l1

        if l2:
            result.next = l2

        return copy.next


class TestSolution(unittest.TestCase):

    def test_longest(self):
        examples = ((["flower","flow","flight"], 'fl'),
                    (["dog","racecar","car"], ''),
                    (["flow","flower","flight"], 'fl')
        )
        for first,second in examples:
            self.assert_function(first, second)
        
    def assert_function(self, first, second):
        self.assertEqual(Solution().longestCommonPrefix(first), second)
