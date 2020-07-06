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


// Given a binary tree, flatten it to a linked list in-place.

// For example, given the following tree:

//     1
//    / \
//   2   5
//  / \   \
// 3   4   6
// The flattened tree should look like:

// 1
//  \
//   2
//    \
//     3
//      \
//       4
//        \
//         5
//          \
//           6

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
    void flatten(TreeNode* root) {
        stack<TreeNode*> nodes;
        nodes.push(root);

        TreeNode* previous = root;
        while (!nodes.empty()) {
            auto item = nodes.top();
            nodes.pop();

            if (item != nullptr) {
                nodes.push(item->right);
                nodes.push(item->left);
                previous->right = item;
                previous = item;
                item->left = nullptr;
                item->right = nullptr;
            }
        }
    }

    void flattenNew(TreeNode* root) {
        while (root != nullptr) {
            TreeNode* predecessor = root->left;
            while (predecessor != nullptr && predecessor->right != nullptr) {
                predecessor = predecessor->right;
            }

            if (predecessor != nullptr) {
                predecessor->right = root->right;
                root->right = root->left;
                root->left = nullptr;
            }

            root = root->right;
        }
    }
};

int main() {
}