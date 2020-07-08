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


// A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

// Return a deep copy of the list.

// The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

// val: an integer representing Node.val
// random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.
 

// Example 1:


// Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
// Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
// Example 2:


// Input: head = [[1,1],[2,1]]
// Output: [[1,1],[2,1]]
// Example 3:



// Input: head = [[3,null],[3,0],[3,null]]
// Output: [[3,null],[3,0],[3,null]]
// Example 4:

// Input: head = []
// Output: []
// Explanation: Given linked list is empty (null pointer), so return null.


class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (head == nullptr) {
            return head;
        }

        unordered_map<Node*, Node*> maps;

        Node *origin = head, *iter = head;
        while (iter != nullptr) {
            Node* clone_node = new Node(iter->val);
            maps[iter] = clone_node;
            iter = iter->next;
        }

        while (origin != nullptr) {
            auto node = maps[origin];
            if (origin->random) {
                node->random = maps[origin->random];
            }
            if (origin->next) {
                node->next= maps[origin->next];
            }
            origin = origin->next;
        }
        return maps[head];
    }

    Node* copyRandomListNew(Node* head) {
        Node* iter = head, *res = nullptr;
        while (iter != nullptr) {
            auto node = new Node(iter->val);
            node->next = iter->next;
            iter->next = node;
            iter = iter->next->next;
        }

        iter = head;
        while (iter != nullptr) {
            if (iter->random) {
                iter->next->random = iter->random->next;
            }
            iter = iter->next->next;
        }

        iter = head;
        while (iter != nullptr) {
            if (res == nullptr) {
                res = iter->next;
            }
            Node* new_node = iter->next;
            iter->next = iter->next->next;
            if (new_node->next != nullptr) {
                new_node->next = new_node->next->next;
            }

            iter = iter->next;
        }
        return res;
    }
};

int main() {
}