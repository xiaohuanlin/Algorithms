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


// Given inorder and postorder traversal of a tree, construct the binary tree.

// Note:
// You may assume that duplicates do not exist in the tree.

// For example, given

// inorder = [9,3,15,20,7]
// postorder = [9,15,7,20,3]
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
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        unordered_map <int, int> maps;
        for (int i = 0; i < inorder.size(); i++) {
            maps[inorder[i]] = i;
        }
        return _buildTree(postorder, 0, postorder.size(), inorder, 0, inorder.size(), maps);
    }

    TreeNode* _buildTree(vector<int>& post_order, int p_start, int p_end, 
                        vector<int>& inorder, int i_start, int i_end, unordered_map<int, int> &maps) {
        if (p_start >= p_end) {
            return nullptr;
        }

        TreeNode* root = new TreeNode(post_order[p_end - 1]);
        int root_index = maps[post_order[p_end - 1]] - i_start;

        root->left = _buildTree(post_order, p_start, p_start+root_index, inorder, i_start, i_start+root_index, maps);
        root->right = _buildTree(post_order, p_start+root_index, p_end - 1, inorder, i_start+root_index+1, i_end, maps);
        return root;
    }
};

int main() {
}