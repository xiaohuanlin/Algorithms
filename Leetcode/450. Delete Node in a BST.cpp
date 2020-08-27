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
                while (true) {
                    TreeNode* deleted;
                    if ((deleted = findpre(iter, &parent, &left))) {
                        iter->val = deleted->val;
                        iter = deleted;
                    } else if ((deleted = findnext(iter, &parent, &left))) {
                        iter->val = deleted->val;
                        iter = deleted;
                    } else {
                        break;
                    }
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

    TreeNode* findpre(TreeNode* node, TreeNode** parent, bool* left) {
        if (!node || !node->left) {
            return nullptr;
        }
        
        TreeNode* iter = node->left;
        *left = true;
        *parent = node;
        while (iter && iter->right) {
            *parent = iter;
            *left = false;
            iter = iter->right;
        }
        return iter;
    }

    TreeNode* findnext(TreeNode* node, TreeNode** parent, bool* left) {
        if (!node || !node->right) {
            return nullptr;
        }
        
        TreeNode* iter = node->right;
        *left = false;
        *parent = node;
        while (iter && iter->left) {
            *parent = iter;
            *left = true;
            iter = iter->left;
        }
        return iter;
    }
};

int main() {
    TreeNode n2(2);
    TreeNode n4(4);
    TreeNode n7(7);
    TreeNode n3(3, &n2, &n4);
    TreeNode n6(6, nullptr, &n7);
    TreeNode n5(5, &n3, &n6);
    Solution s;
    auto node = s.deleteNode(&n5, 3);
}