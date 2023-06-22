'''
Given a string s represents the serialization of a nested list, implement a parser to deserialize it and return the deserialized NestedInteger.

Each element is either an integer or a list whose elements may also be integers or other lists.



Example 1:

Input: s = "324"
Output: 324
Explanation: You should return a NestedInteger object which contains a single integer 324.
Example 2:

Input: s = "[123,[456,[789]]]"
Output: [123,[456,[789]]]
Explanation: Return a NestedInteger object containing a nested list with 2 elements:
1. An integer containing value 123.
2. A nested list containing two elements:
    i.  An integer containing value 456.
    ii. A nested list with one element:
         a. An integer containing value 789


Constraints:

1 <= s.length <= 5 * 104
s consists of digits, square brackets "[]", negative sign '-', and commas ','.
s is the serialization of valid NestedInteger.
All the values in the input are in the range [-106, 106].
'''
import unittest

from typing import *


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        root = cur = NestedInteger()
        stack = [cur]
        i = 0
        while i < len(s):
            if s[i] == '[':
                new_element = NestedInteger()
                stack.append(new_element)
                cur.getList().append(new_element)
                cur = new_element
            elif s[i] == ']':
                stack.pop()
                cur = stack[-1]
            elif s[i] == ',':
                pass
            else:
                j = i
                while j < len(s) and (s[j].isdigit() or s[j] == '-'):
                    j += 1
                v = int(s[i:j])
                if j == len(s):
                    cur.setInteger(v)
                else:
                    cur.getList().append(NestedInteger(v))
                i = j - 1
            i += 1
        return root.getList()[0] if not root.isInteger() else root
