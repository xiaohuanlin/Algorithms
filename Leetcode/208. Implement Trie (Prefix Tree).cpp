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


// Implement a trie with insert, search, and startsWith methods.

// Example:

// Trie trie = new Trie();

// trie.insert("apple");
// trie.search("apple");   // returns true
// trie.search("app");     // returns false
// trie.startsWith("app"); // returns true
// trie.insert("app");   
// trie.search("app");     // returns true
// Note:

// You may assume that all inputs are consist of lowercase letters a-z.
// All inputs are guaranteed to be non-empty strings.


class Trie {
    struct Node {
        char value;
        bool exist;
        vector<Node*> nexts;
        Node(): value(0), exist(false), nexts() {};
        Node(char n): value(n), exist(false), nexts() {};
        Node* search(char w) {
            for (int i = 0; i < nexts.size(); i++) {
                if (nexts[i]->value == w) {
                    return nexts[i];
                }
            }
            return nullptr;
        };
    };
    Node *root;

public:
    /** Initialize your data structure here. */
    Trie() {
        root = new Node();
    }
    
    /** Inserts a word into the trie. */
    void insert(string word) {
        auto start = word.begin();
        Node *iter = root, *tmp;
        while (start != word.end()) {
            tmp = iter->search(*start);
            if (tmp == nullptr) {
                tmp = new Node(*start);
                iter->nexts.push_back(tmp);
            }
            iter = tmp;
            start ++;
        }
        tmp->exist = true;
    }
    
    /** Returns if the word is in the trie. */
    bool search(string word) {
        auto start = word.begin();
        Node *iter = root;
        while (start != word.end()) {
            iter = iter->search(*start);
            if (iter == nullptr) {
                return false;
            }
            start ++;
        } 

        return iter->exist;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        auto start = prefix.begin();
        Node *iter = root;
        while (start != prefix.end()) {
            iter = iter->search(*start);
            if (iter == nullptr) {
                return false;
            }
            start ++;
        } 
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */

int main() {
    Trie* obj = new Trie();
    obj->insert("abc");
    cout << obj->search("ab") << endl;
    cout << obj->startsWith("a") << endl;
}