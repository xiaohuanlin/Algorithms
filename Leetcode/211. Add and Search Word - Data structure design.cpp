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


// 211. Add and Search Word - Data structure design
// Medium

// 1772

// 89

// Add to List

// Share
// Design a data structure that supports the following two operations:

// void addWord(word)
// bool search(word)
// search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

// Example:

// addWord("bad")
// addWord("dad")
// addWord("mad")
// search("pad") -> false
// search("bad") -> true
// search(".ad") -> true
// search("b..") -> true
// Note:
// You may assume that all words are consist of lowercase letters a-z.


class WordDictionary {
    struct Node {
        char value;
        bool exist;
        vector<Node*> nexts;
        Node(): value(0), exist(false), nexts(26, nullptr) {};
        Node(char n): value(n), exist(false), nexts(26, nullptr) {};
    };
    Node *root;

public:
    /** Initialize your data structure here. */
    WordDictionary() {
        root = new Node();
    }
    
    /** Adds a word into the data structure. */
    void addWord(string word) {
        auto start = word.begin();
        Node *iter = root, *tmp;
        while (start != word.end()) {
            auto res = iter->nexts[(*start) - 'a'];
            if (!res) {
                tmp = new Node(*start);
                iter->nexts[(*start) - 'a'] = tmp;
            } else {
                tmp = res;
            }
            iter = tmp;
            start ++;
        }
        tmp->exist = true;
    }
    
    /** Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. */
    bool search(string word) {
        return core_search(word, 0, root);
    }

    bool core_search(string &word, int start, Node* iter) {
        if (start == word.length() || !iter) {
            return false;
        }

        char w =word[start];
        if (w == '.') {
            for (int i = 0; i < 26; i++) {
                if (start == word.length() - 1 && iter->nexts[i] && iter->nexts[i]->exist) {
                    return true;
                }
                if (core_search(word, start+1, iter->nexts[i])) {
                    return true;
                }
            }
        } else {
            if (start == word.length() - 1 && iter->nexts[w-'a'] && iter->nexts[w - 'a']->exist) {
                return true;
            }
            if (core_search(word, start+1, iter->nexts[w - 'a'])) {
                return true;
            }

        }

        return false;
    }
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */

int main() {
    WordDictionary* obj = new WordDictionary();
    obj->addWord("abc");
    cout << obj->search("ab.");
}
