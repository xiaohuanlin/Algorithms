#include <unordered_set>
#include <unordered_map>
#include <math.h>
#include <utility>
#include <stack>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;


// Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

// Only one letter can be changed at a time.
// Each transformed word must exist in the word list.
// Note:

// Return 0 if there is no such transformation sequence.
// All words have the same length.
// All words contain only lowercase alphabetic characters.
// You may assume no duplicates in the word list.
// You may assume beginWord and endWord are non-empty and are not the same.
// Example 1:

// Input:
// beginWord = "hit",
// endWord = "cog",
// wordList = ["hot","dot","dog","lot","log","cog"]

// Output: 5

// Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
// return its length 5.
// Example 2:

// Input:
// beginWord = "hit"
// endWord = "cog"
// wordList = ["hot","dot","dog","lot","log"]

// Output: 0

// Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.


class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> word_list(wordList.begin(), wordList.end()), head, tail, *phead, *ptail;
        // we need judge endword exist in the wordlist, because we will use it to iterate
        if (word_list.find(endWord) == word_list.end()) {
            return 0;
        }

        // we use set as data structure, because we can find element faster.
        head.insert(beginWord);
        tail.insert(endWord);
        int count = 1;
        while (!head.empty() && !tail.empty()) {
            // everytime we deal with the smaller set first
            if (head.size() < tail.size()) {
                phead = &head;
                ptail = &tail;
            } else {
                phead = &tail;
                ptail = &head;
            }

            // because we use set, so we can't add element when we iterate; change it to swap
            unordered_set<string> tmp_set;
            for (auto iter = phead->begin(); iter != phead->end(); iter++) {
                string item = *iter;
                for (int j = 0; j < item.length(); j ++) {
                    for (int i = 0; i < 26; i++) {
                        if (item[j] == 'a' + i) {
                            continue;
                        }
                        char tmp = item[j];
                        item[j] = 'a' + i;
                        if (ptail->find(item) != ptail->end()) {
                            return count+1;
                        }
                        if (word_list.find(item) != word_list.end()) {
                            tmp_set.insert(item);
                            word_list.erase(item);
                        }
                        item[j] = tmp;
                    }
                }
            }
            count++;
            phead->swap(tmp_set);
        }

        return 0;
    }

};


int main() {
    Solution s;
    vector<string> array = {
        "hot","dot","dog","lot","log", "cog"
    };
    cout << s.ladderLength("hit", "cog", array);
}