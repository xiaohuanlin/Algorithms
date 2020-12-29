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


// Given the root of a binary tree, return all duplicate subtrees.

// For each kind of duplicate subtrees, you only need to return the root node of any one of them.

// Two trees are duplicate if they have the same structure with the same node values.

 

// Example 1:


// Input: root = [1,2,3,4,null,2,4,null,null,4]
// Output: [[2,4],[4]]
// Example 2:


// Input: root = [2,1,1]
// Output: [[1]]
// Example 3:


// Input: root = [2,2,2,3,null,3,null]
// Output: [[2,3],[3]]
 

// Constraints:

// The number of the nodes in the tree will be in the range [1, 10^4]
// -200 <= Node.val <= 200


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
    vector<TreeNode*> findDuplicateSubtrees(TreeNode* root) {
        // try to consider hashmap
        vector<TreeNode*> res;
        unordered_map<string, int> sets;
        iter(root, sets, res);
        return res;
    }

    string iter(TreeNode* root, unordered_map<string, int> &sets, vector<TreeNode*> &res) {
        if (root == nullptr) {
            return "#";
        }

        string ans = to_string(root->val) + "/" + iter(root->left, sets, res) + "/" + iter(root->right, sets, res);
        sets[ans]++;
        if (sets[ans] == 2) {
            res.push_back(root);
        }
        return ans;
    }
};


int main() {
}
