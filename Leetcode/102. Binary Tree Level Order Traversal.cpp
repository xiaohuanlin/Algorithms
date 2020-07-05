#include <math.h>
#include <utility>
#include <stack>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;


// Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

// For example:
// Given binary tree [3,9,20,null,null,15,7],
//     3
//    / \
//   9  20
//     /  \
//    15   7
// return its level order traversal as:
// [
//   [3],
//   [9,20],
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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> res;
        deque<TreeNode*> array = {root};       
        vector<int> unit_res;

        while (!array.empty()) {
            int size = array.size();
            for (int i = 0; i < size; i++) {
                auto item = array.front();
                array.pop_front();
                if (item == nullptr) {
                    continue;
                }

                unit_res.push_back(item->val);
                array.push_back(item->left);
                array.push_back(item->right);
            }
            if (unit_res.empty()) {
                continue;
            }
            res.push_back(unit_res);
            unit_res.clear();
        }
        return res;
    }
};

int main() {
    TreeNode third(3);
    TreeNode second(2, nullptr, &third);
    TreeNode first(1, &second, nullptr);
    Solution s;
    auto res = s.levelOrder(&first);
    for (auto e : res) {
        for (auto l: e) {
            cout << l << ',';
        }
        cout << endl;
    }
}