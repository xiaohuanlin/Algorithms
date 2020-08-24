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


// Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

// Basically, the deletion can be divided into two stages:

// Search for a node to remove.
// If the node is found, delete the node.
// Note: Time complexity should be O(height of tree).

// Example:

// root = [5,3,6,2,4,null,7]
// key = 3

//     5
//    / \
//   3   6
//  / \   \
// 2   4   7

// Given key to delete is 3. So we find the node with value 3 and delete it.

// One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

//     5
//    / \
//   4   6
//  /     \
// 2       7

// Another valid answer is [5,2,6,null,4,null,7].

//     5
//    / \
//   2   6
//    \   \
//     4   7

  struct TreeNode {
      int val;
      TreeNode *left;
      TreeNode *right;
      TreeNode() : val(0), left(nullptr), right(nullptr) {}
      TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
      TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
  };

class Solution {
public:
    TreeNode* deleteNode(TreeNode* root, int key) {
        TreeNode *iter = root, *parent = nullptr;
        bool left = false;
        while (iter) {
            if (iter->val > key) {
                parent = iter;
                iter = iter->left;
                left = true;
            } else if (iter->val < key) {
                parent = iter;
                iter = iter->right;
                left = false;
            } else {
                // delete it and change it
                TreeNode* deleted;
                if (deleted = findpre(iter)) {
                    iter->val = deleted->val;
                    break;
                }

                if (deleted = findnext(iter)) {
                    iter->val = deleted->val;
                    break;
                }

                if (!parent) {
                    return nullptr;
                }

                if (left) {
                    parent->left = nullptr;
                } else {
                    parent->right = nullptr;
                }
                break;
            }
        }
        return root;
        
    }

    TreeNode* findpre(TreeNode* node) {
        if (!node || !node->left) {
            return nullptr;
        }
        
        TreeNode* parent = nullptr, *iter = node->left;
        while (iter && iter->right) {
            parent = iter;
            iter = iter->right;
        }
        if (parent) {
            parent->right = nullptr;
        } else {
            iter = node->left;
            node->left = node->left->left;
        }
        return iter;
    }

    TreeNode* findnext(TreeNode* node) {
        if (!node || !node->right) {
            return nullptr;
        }
        
        TreeNode* parent = nullptr, *iter = node->right;
        while (iter && iter->left) {
            parent = iter;
            iter = iter->left;
        }
        if (parent) {
            parent->left= nullptr;
        } else {
            iter = node->right;
            node->right= node->right->right;
        }
        return iter;
    }
};

int main() {
}