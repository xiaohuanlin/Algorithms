#include <math.h>
#include <utility>
#include <stack>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;


// Given a binary tree, return the inorder traversal of its nodes' values.

// Example:

// Input: [1,null,2,3]
//    1
//     \
//      2
//     /
//    3

// Output: [1,3,2]
// Follow up: Recursive solution is trivial, could you do it iteratively?


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
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res;
        stack<TreeNode*> candidates;
        stack<int> values;
        candidates.push(root);

        while (!candidates.empty()) {
            auto item = candidates.top();
            candidates.pop();

            if (item == nullptr) {
                if (!values.empty()) {
                    res.push_back(values.top());
                    values.pop();
                }
                continue;
            }

            values.push(item->val);
            candidates.push(item->right);
            candidates.push(item->left);
        }
        return res;
    }


    vector<int> MorriInorderTraversal(TreeNode* root) {
        TreeNode *current = root;
        vector<int> res;

        while (current != nullptr) {
            if (current->left == nullptr) {
                res.push_back(current->val);
                current = current->right;
            } else {
                // find the precessor
                TreeNode *iter = current->left;
                while (iter != nullptr && iter->right != nullptr && iter->right != current) {
                    iter = iter->right;
                }
                if (iter->right == nullptr) {
                    iter->right = current;
                    current = current->left;
                } else {
                    iter->right = nullptr;
                    res.push_back(current->val);
                    current = current->right;
                }
            }
        }
        return res;
    }
};

int main() {
    TreeNode third(3);
    TreeNode second(2, nullptr, &third);
    TreeNode first(1, &second, nullptr);
    Solution s;
    auto res = s.MorriInorderTraversal(&first);
    for (auto e : res) {
        cout << e << ',';
    }
    cout << endl;
}