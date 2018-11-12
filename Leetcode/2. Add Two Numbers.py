'''

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

'''
import unittest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # car = 0
        # pre_node = ori_node = ListNode(None)
        #
        # while l1 is not None or l2 is not None or car > 0:
        #     l1_val = l1.val if l1 is not None else 0
        #     l2_val = l2.val if l2 is not None else 0
        #
        #     dig = (l1_val + l2_val + car) % 10
        #     if l1_val + l2_val + car > 9:
        #         car = 1
        #     else:
        #         car = 0
        #     node = ListNode(dig)
        #     pre_node.next = node
        #     pre_node = node
        #
        #     l1 = l1.next if l1 is not None else l1
        #     l2 = l2.next if l2 is not None else l2
        #
        # return ori_node.next

        l1_num = []
        l2_num = []
        while l1:
            l1_num.append(l1.val)
            l1 = l1.next
        while l2:
            l2_num.append(l2.val)
            l2 = l2.next
        result = int(''.join(str(i) for i in l1_num[::-1])) + int(''.join(str(i) for i in l2_num[::-1]))
        pre_node = ori_node = ListNode(None)
        if result == 0:
            return ListNode(0)
        while result > 0:
            result, res = result // 10, result % 10
            node = ListNode(res)
            pre_node.next = node
            pre_node = node
        return ori_node.next

l1 = ListNode(0)
l2 = ListNode(0)
print(Solution().addTwoNumbers(l1, l2))


