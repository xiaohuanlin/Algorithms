'''
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
'''
import unittest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """


class TestSolution(unittest.TestCase):
    def to_interval(self, num_list):
        tmp = ori = ListNode(num_list[0])
        for i in num_list[1:]:
            tmp.next = ListNode(i)
            tmp = tmp.next
        return ori
    
    def test_isPalindrome(self):
        examples = (
            (self.to_interval([1,2]), False),
            (self.to_interval([1,2,2,1]), True),
        )
        for first,second in examples:
            self.assert_function(first, second)
        
    def assert_function(self, first, second):
        self.assertEqual(Solution().isPalindrome(first), second)

unittest.main()