'''
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Explanation: There are 2 shortest transformation sequences:
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: []
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 

Constraints:

1 <= beginWord.length <= 5
endWord.length == beginWord.length
1 <= wordList.length <= 1000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
'''
import collections
from typing import *

from collections import deque
import unittest


class Solution:
    min_length = float('+inf')

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        maps = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                maps[word[:i] + '*' + word[i + 1:]].append(word)

        q = deque()
        q.append([beginWord])
        ans = []
        visit = {beginWord}
        while q:
            size = len(q)
            current_visit = set()

            for _ in range(size):
                path = q.popleft()
                if path[-1] == endWord:
                    if len(path) < self.min_length:
                        self.min_length = len(path)
                        ans = [path]
                    elif len(path) == self.min_length:
                        ans.append(path)
                    continue

                word = path[-1]
                for i in range(len(word)):
                    for next_word in maps[word[:i] + '*' + word[i + 1:]]:
                        if next_word not in visit:
                            current_visit.add(next_word)
                            q.append(path + [next_word])

            visit |= current_visit
        return ans


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("hit", "cog", ["hot","dot","dog","lot","log","cog"]), [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().findLadders(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
