'''
Design a map that allows you to do the following:

Maps a string key to a given value.
Returns the sum of the values that have a key with a prefix equal to a given string.
Implement the MapSum class:

MapSum() Initializes the MapSum object.
void insert(String key, int val) Inserts the key-val pair into the map. If the key already existed, the original key-value pair will be overridden to the new one.
int sum(string prefix) Returns the sum of all the pairs' value whose key starts with the prefix.
 

Example 1:

Input
["MapSum", "insert", "sum", "insert", "sum"]
[[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
Output
[null, null, 3, null, 5]

Explanation
MapSum mapSum = new MapSum();
mapSum.insert("apple", 3);  
mapSum.sum("ap");           // return 3 (apple = 3)
mapSum.insert("app", 2);    
mapSum.sum("ap");           // return 5 (apple + app = 3 + 2 = 5)
 

Constraints:

1 <= key.length, prefix.length <= 50
key and prefix consist of only lowercase English letters.
1 <= val <= 1000
At most 50 calls will be made to insert and sum.
'''
import unittest

from typing import *


class Node:
    def __init__(self, key):
        self.children = {}
        self.char = key
        self.value = None
        self.end = False


class MapSum:

    def __init__(self):
        self.root = Node("")

    def insert(self, key: str, val: int) -> None:
        root = self.root
        for c in key:
            if c not in root.children:
                root.children[c] = Node(c)
            root = root.children[c]

        root.end = True
        root.value = val

    def sum(self, prefix: str) -> int:
        res = 0
        def dfs(node, index):
            if node is None:
                return
            if index < len(prefix):
                if node.char != prefix[index]:
                    return
            if index >= len(prefix) - 1:
                if node.end:
                    nonlocal res
                    res += node.value
                
            for n in node.children.values():
                dfs(n, index+1)

            return
        
        for n in self.root.children.values():
            dfs(n, 0)
        return res


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)

