#include <math.h>
#include <utility>
#include <stack>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;


// Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

// Example:

// Input: 3
// Output:
// [
//   [1,null,3,2],
//   [3,2,null,1],
//   [3,1,null,null,2],
//   [2,1,3],
//   [1,null,2,null,3]
// ]
// Explanation:
// The above output corresponds to the 5 unique BST's shown below:

//    1         3     3      2      1
//     \       /     /      / \      \
//      3     2     1      1   3      2
//     /     /       \                 \
//    2     1         2                 3

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
    vector<TreeNode*> generateTrees(int n) {
        vector<vector<vector<TreeNode*>>> dp(n+1, vector<vector<TreeNode*>>(n+1, vector<TreeNode*>()));

        if (n == 0) {
            return vector<TreeNode*>();
        }

        for (int end = 0; end < n+1; end++) {
            for (int start = end; start >= 0; start--) {
                if (start == end) {
                    dp[start][end].push_back(nullptr);
                    continue;
                }
                for (int i = start; i < end; i++) {
                    auto left = dp[start][i];
                    auto right = dp[i+1][end];
                    for (int j = 0; j < left.size(); j++) {
                        for (int k = 0; k < right.size(); k++) {
                            TreeNode* root = new TreeNode(i+1, left[j], right[k]);
                            dp[start][end].push_back(root);
                        }
                    }
                }
            }
        }
        return dp[0][n];
    }
};


int main() {
    Solution s;
    s.generateTrees(1);
}