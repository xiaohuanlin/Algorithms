'''
Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.

Implement the AllOne class:

AllOne() Initializes the object of the data structure.
inc(String key) Increments the count of the string key by 1. If key does not exist in the data structure, insert it with count 1.
dec(String key) Decrements the count of the string key by 1. If the count of key is 0 after the decrement, remove it from the data structure. It is guaranteed that key exists in the data structure before the decrement.
getMaxKey() Returns one of the keys with the maximal count. If no element exists, return an empty string "".
getMinKey() Returns one of the keys with the minimum count. If no element exists, return an empty string "".
Note that each function must run in O(1) average time complexity.

 

Example 1:

Input
["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
[[], ["hello"], ["hello"], [], [], ["leet"], [], []]
Output
[null, null, null, "hello", "hello", null, "hello", "leet"]

Explanation
AllOne allOne = new AllOne();
allOne.inc("hello");
allOne.inc("hello");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "hello"
allOne.inc("leet");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "leet"
 

Constraints:

1 <= key.length <= 10
key consists of lowercase English letters.
It is guaranteed that for each call to dec, key is existing in the data structure.
At most 5 * 104 calls will be made to inc, dec, getMaxKey, and getMinKey.
'''

from typing import *

import unittest


class ListNode:
    def __init__(self, value = 0, prev = None, next = None):
        self.keys = set()
        self.val = value
        self.prev = prev
        self.next = next
        
    def insert(self, node):
        next_ele = node.next
        
        node.next = self
        self.prev = node
        
        self.next = next_ele
        next_ele.prev = self
    
    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev
    
    
class AllOne:

    def __init__(self):
        self.maps = {} 
        self.list_head = ListNode()
        self.list_tail = ListNode()
        self.list_head.next = self.list_tail
        self.list_tail.prev = self.list_head
        
    def inc(self, key: str) -> None:
        if key in self.maps:
            node = self.maps[key]
            node.keys.remove(key)
        else:
            node = self.list_head
        
        node_next = node.next
        if not node_next or node_next.val != node.val + 1:
            node_next = ListNode(node.val + 1)
            node_next.insert(node)
        
        if not node.keys and node != self.list_head:
            node.remove()
            
        node_next.keys.add(key)
        self.maps[key] = node_next


    def dec(self, key: str) -> None:
        node = self.maps[key]
        node.keys.remove(key)
        
        node_prev = node.prev
        if not node_prev or node_prev.val != node.val - 1:
            node_prev = ListNode(node.val - 1)
            node_prev.insert(node.prev)
            
        if not node.keys:
            node.remove()

        if node.val == 1:
            del self.maps[key]
            return
        
        node_prev.keys.add(key)
        self.maps[key] = node_prev

    def getMaxKey(self) -> str:
        if not self.list_tail.prev.keys:
            return ""
        item = self.list_tail.prev.keys.pop()
        self.list_tail.prev.keys.add(item)
        return item
        
    def getMinKey(self) -> str:
        if not self.list_head.next.keys:
            return ""
        item = self.list_head.next.keys.pop()
        self.list_head.next.keys.add(item)
        return item

