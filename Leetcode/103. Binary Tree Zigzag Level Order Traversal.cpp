#include <math.h>
#include <utility>
#include <stack>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;


// Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

// For example:
// Given binary tree [3,9,20,null,null,15,7],
//     3
//    / \
//   9  20
//     /  \
//    15   7
// return its zigzag level order traversal as:
// [
//   [3],
//   [20,9],
//   [15,7]
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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        stack<TreeNode*> candidates;
        candidates.push(root);
        vector<vector<int>> res;
        bool flag = true;

        while (!candidates.empty()) {
            int size = candidates.size();
            vector<int> unit_res;
            stack<TreeNode*> new_candidates;

            for (int i = 0; i < size; i++) {
                auto item = candidates.top();
                candidates.pop();

                if (item != nullptr) {
                    unit_res.push_back(item->val);
                    if (flag) {
                        new_candidates.push(item->right);
                        new_candidates.push(item->left);
                    } else {
                        new_candidates.push(item->left);
                        new_candidates.push(item->right);
                    }
                }
            }

            if (unit_res.empty()) {
                continue;
            }
            res.push_back(unit_res);
            candidates = new_candidates;
            flag = !flag;
        }
        return res;
    }
};

int main() {
    TreeNode third(3);
    TreeNode second(2, nullptr, &third);
    TreeNode first(1, &second, &second);
    Solution s;
    auto res = s.zigzagLevelOrder(&first);
    for (auto e : res) {
        for (auto l: e) {
            cout << l << ',';
        }
        cout << endl;
    }
}