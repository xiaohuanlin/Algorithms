#include <math.h>
#include <utility>
#include <stack>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;


// Given a binary tree, determine if it is a valid binary search tree (BST).

// Assume a BST is defined as follows:

// The left subtree of a node contains only nodes with keys less than the node's key.
// The right subtree of a node contains only nodes with keys greater than the node's key.
// Both the left and right subtrees must also be binary search trees.
 

// Example 1:

//     2
//    / \
//   1   3

// Input: [2,1,3]
// Output: true
// Example 2:

//     5
//    / \
//   1   4
//      / \
//     3   6

// Input: [5,1,4,null,null,3,6]
// Output: false
// Explanation: The root node's value is 5 but its right child's value is 4.

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
    bool isValidBST(TreeNode* root) {
        if (root == nullptr) {
            return true;
        }
        int l_min, r_max;
        return isValid(root, l_min, r_max);
    }

    bool isValid(TreeNode *root, int &left_min, int &right_max) {
        if (root->left == nullptr && root->right == nullptr) {
            left_min = right_max = root->val;
            return true;
        }

        int l_min, r_max;
        
        if (root->left != nullptr) {
            bool left = isValid(root->left, l_min, r_max);
            left_min = l_min;
            right_max = root->val;

            if (!left || r_max >= root->val) {
                return false;
            }
        }

        if (root->right != nullptr) {
            bool right = isValid(root->right, l_min, r_max);
            if (root->left == nullptr) {
                left_min = root->val;
            }
            right_max = r_max;

            if (!right || l_min <= root->val) {
                return false;
            }
        }

        return true;

    }
};


int main() {
}