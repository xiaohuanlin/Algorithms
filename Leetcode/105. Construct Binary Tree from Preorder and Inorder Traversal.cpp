#include <math.h>
#include <utility>
#include <stack>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;


// Given preorder and inorder traversal of a tree, construct the binary tree.

// Note:
// You may assume that duplicates do not exist in the tree.

// For example, given

// preorder = [3,9,20,15,7]
// inorder = [9,3,15,20,7]
// Return the following binary tree:

//     3
//    / \
//   9  20
//     /  \
//    15   7

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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        return _buildTree(preorder, 0, preorder.size(), inorder, 0, inorder.size());
    }

    TreeNode* _buildTree(vector<int>& preorder, int p_start, int p_end, 
                        vector<int>& inorder, int i_start, int i_end) {
        if (p_start >= p_end) {
            return nullptr;
        }

        TreeNode* root = new TreeNode(preorder[p_start]);
        auto iter = find(inorder.begin() + i_start, inorder.begin() + i_end, preorder[p_start]);
        int root_index = iter - inorder.begin() - i_start;

        root->left = _buildTree(preorder, p_start+1, p_start+root_index+1, inorder, i_start, i_start+root_index);
        root->right = _buildTree(preorder, p_start+root_index+1, p_end, inorder, i_start+root_index+1, i_end);
        return root;
    }
};

int main() {
}