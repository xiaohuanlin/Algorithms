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


// Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

// Note: A leaf is a node with no children.

// Example:

// Given the below binary tree and sum = 22,

//       5
//      / \
//     4   8
//    /   / \
//   11  13  4
//  /  \    / \
// 7    2  5   1
// Return:

// [
//    [5,4,11,2],
//    [5,8,4,5]
// ]

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
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        vector<vector<int>> res;
        vector<int> path;
        if (root == nullptr) {
            return res;
        }

        path.push_back(root->val);
        getPath(res, path, root->val, sum, root);
        return res;
    }

    void getPath(vector<vector<int>> &res, vector<int> &path, int sum, int target, TreeNode* node) {
        if (node->left == nullptr && node->right == nullptr) {
            if (sum == target) {
                res.push_back(path);
            }
            return;
        }

        if (node->left != nullptr) {
            path.push_back(node->left->val);
            getPath(res, path, sum+node->left->val, target, node->left);
            path.pop_back();
        }

        if (node->right != nullptr) {
            path.push_back(node->right->val);
            getPath(res, path, sum+node->right->val, target, node->right);
            path.pop_back();
        }
    }
};

int main() {
}