'''
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
Credits:
Special thanks to @stellari for adding this problem and creating all test cases.
'''
import unittest

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # if headA is None or headB is None:
        #     return None
        # # get the length of headA, headB
        # headA_len = headB_len = 0
        # origin_headA, origin_headB = headA, headB
        # while headA:
        #     headA = headA.next
        #     headA_len += 1
        # while headB:
        #     headB = headB.next
        #     headB_len += 1
        # # cut the trival node
        # headA, headB = origin_headA, origin_headB 
        # differ = headA_len - headB_len
        # for _ in range(differ):
        #     if differ > 0:
        #         headA = headA.next
        #     else:
        #         headB = headB.next
        # # compare the head
        # while headA and headB:
        #     if headA == headB:
        #         return headA
        #     headA = headA.next
        #     headB = headB.next 
        # --------------------------------
        if headA is None or headB is None:
            return None
        origin_headA, origin_headB = headA, headB
        while headA or headB:
            if headA is None:
                headA = origin_headB
            if headB is None:
                headB = origin_headA
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None


class TestSolution(unittest.TestCase):

    def test_getIntersectionNode(self):
        ex_1, ex_2 = ListNode(2), ListNode(3)
        ex_1.next = ex_2
        examples = (
            ((ex_2, ex_1), ex_2),
        )
        for first,second in examples:
            self.assert_function(first, second)
        
    def assert_function(self, first, second):
        self.assertEqual(Solution().getIntersectionNode(*first), second)

unittest.main()