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


// Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

// According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

// Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]


 

// Example 1:

// Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
// Output: 3
// Explanation: The LCA of nodes 5 and 1 is 3.
// Example 2:

// Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
// Output: 5
// Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
 

// Note:

// All of the nodes' values will be unique.
// p and q are different and both values will exist in the binary tree.

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
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (!root) {
            return root;
        }

        if (p == q) {
            return q;
        }
        vector<TreeNode*> path, p_res, q_res;

        path.push_back(root);
        backtrace(path, p_res, q_res, root, p, q);

        int count = 0;
        while (count < p_res.size() && count < q_res.size()) {
            if (p_res[count] == q_res[count]) {
                count++;
            } else {
                break;
            }
        }
        return p_res[count-1];
    }

    void backtrace(vector<TreeNode*> &path, vector<TreeNode*> &p_res, vector<TreeNode*> &q_res, TreeNode* root, TreeNode* p, TreeNode* q) {
        if (!root) {
            return;
        }
        if (!p_res.empty() && !q_res.empty()) {
            return;
        }

        if (root == p && p_res.empty()) {
            p_res = path;
        }
        if (root == q && q_res.empty()) {
            q_res = path;
        }

        path.push_back(root->left);
        backtrace(path, p_res, q_res, root->left, p, q);
        path.pop_back();

        path.push_back(root->right);
        backtrace(path, p_res, q_res, root->right, p, q);
        path.pop_back();
    }

};

int main() {
}