'''
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example 1:


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:


Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.
'''
from operator import ne
from typing import *

import unittest



class Solution:
    words_num = 0
    
    class TrieTreeNode:
        def __init__(self, char, end = False) -> None:
            self.char = char
            self.end = end
            self.children = {}

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = set()
        root = self.buildTrieTree(words)
        self.words_num = len(words)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if len(res) == self.words_num:
                    break

                self.backtrace(board, i, j, "", root.children.get(board[i][j]), res)
        return list(res)
    
    def buildTrieTree(self, words) -> TrieTreeNode:
        root = self.TrieTreeNode("")
        for word in words:
            iter = root
            for c in word:
                if c not in iter.children:
                    iter.children[c] = self.TrieTreeNode(c)
                iter = iter.children[c]
            iter.end = True
        return root
        
    def backtrace(self, board: List[List[str]], i: int, j: int, word: str, node: TrieTreeNode, res: Set[str]):
        if len(res) == self.words_num:
            return
        
        if node is None:
            return

        if board[i][j] != node.char:
            return
        
        if node.end:
            res.add(word + board[i][j])
            node.end = False
        
        tmp = board[i][j]
        board[i][j] = '#'

        word += tmp
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        for x_del, y_del in directions:
            if len(res) == self.words_num:
                return
            next_i = i + x_del
            next_j = j + y_del
            if next_i < 0 or next_i >= len(board) or next_j < 0 or next_j >= len(board[0]):
                continue

            self.backtrace(board, next_i, next_j, word, node.children.get(board[next_i][next_j]), res)
        
        board[i][j] = tmp
        
        

    
class TestSolution(unittest.TestCase):
    def test_case(self):
        examples = (
            (([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"]), ["oath", "eat"]),
            (([["a","b"],["c","d"]], ["abcb"]), []),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().findWords(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

