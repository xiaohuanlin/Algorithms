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


// Given a binary tree

// struct Node {
//   int val;
//   Node *left;
//   Node *right;
//   Node *next;
// }
// Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

// Initially, all next pointers are set to NULL.

 

// Follow up:

// You may only use constant extra space.
// Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
 

// Example 1:



// Input: root = [1,2,3,4,5,null,7]
// Output: [1,#,2,3,#,4,5,7,#]
// Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};

class Solution {
public:
    Node* connect(Node* root) {
        Node *current = root, *level_start = root;
        while (level_start) {
            current = level_start;
            while (current) {
                if (current->left || current->right) {
                    // finish inner connect
                    if (current->left && current->right) {
                        current->left->next = current->right;
                    }

                    Node *previous = current;

                    // finish outer connect
                    while (current->next && !current->next->left && !current->next->right) {
                        current = current->next;
                    }

                    if (current->next) {
                        if (current->next->left) {
                            if (!previous->right) {
                                previous->left->next = current->next->left;
                            } else {
                                previous->right->next = current->next->left;
                            }
                        } else {
                            if (!previous->right) {
                                previous->left->next = current->next->right;
                            } else {
                                previous->right->next = current->next->right;
                            }
                        }
                    }
                }

                current = current->next;
            }

            // find next level start point
            while (level_start) {
                if (level_start->left) {
                    level_start = level_start->left;
                    break;
                }

                if (level_start->right) {
                    level_start = level_start->right;
                    break;
                }

                level_start = level_start->next;
            }
        }
        return root;
    }
};

int main() {
}