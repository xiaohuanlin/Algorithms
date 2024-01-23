'''
Design the CombinationIterator class:

CombinationIterator(string characters, int combinationLength) Initializes the object with a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
next() Returns the next combination of length combinationLength in lexicographical order.
hasNext() Returns true if and only if there exists a next combination.
 

Example 1:

Input
["CombinationIterator", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[["abc", 2], [], [], [], [], [], []]
Output
[null, "ab", true, "ac", true, "bc", false]

Explanation
CombinationIterator itr = new CombinationIterator("abc", 2);
itr.next();    // return "ab"
itr.hasNext(); // return True
itr.next();    // return "ac"
itr.hasNext(); // return True
itr.next();    // return "bc"
itr.hasNext(); // return False
 

Constraints:

1 <= combinationLength <= characters.length <= 15
All the characters of characters are unique.
At most 104 calls will be made to next and hasNext.
It is guaranteed that all calls of the function next are valid.
'''

from typing import *
import unittest


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.s = characters
        self.l = combinationLength
        self.c = 0
        self.all = self.get_all_com()
    
    def get_all_com(self):
        res = []
        for i in range(2 ** len(self.s)):
            bin_i = bin(i)[2:].zfill(len(self.s))
            if bin_i.count('1') == self.l:
                s = []
                for j in range(len(bin_i)):
                    if bin_i[j] == '1':
                        s.append(self.s[j])
                res.append(''.join(s))
        return res[::-1]
                

    def next(self) -> str:
        res = self.all[self.c]
        self.c += 1
        return res

    def hasNext(self) -> bool:
        return self.c < len(self.all)


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()