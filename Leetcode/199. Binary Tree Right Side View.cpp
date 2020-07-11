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


// Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

// Example:

// Input: [1,2,3,null,5,null,4]
// Output: [1, 3, 4]
// Explanation:

//    1            <---
//  /   \
// 2     3         <---
//  \     \
//   5     4       <---

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
    vector<int> rightSideView(TreeNode* root) {
        stack<pair<TreeNode*, int>> candidates;
        candidates.push(make_pair(root, 0));
        int max_level = -1;

        vector<int> res;
        while (!candidates.empty()) {
            auto item = candidates.top();
            candidates.pop();

            if (!item.first) {
                continue;
            }

            if (item.second > max_level) {
                res.push_back(item.first->val);
                max_level ++;
            }

            candidates.push(make_pair(item.first->left, item.second + 1));
            candidates.push(make_pair(item.first->right, item.second + 1));
        }
        reverse(res.begin(), res.end());
        return res;
    }
};


int main() {
}