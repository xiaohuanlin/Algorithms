#include <vector>
#include <stack>
#include <deque>
#include <algorithm>
#include <iostream>
#include <tuple>
#include <assert.h>
using namespace std;


// Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

// A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.

 

// Example 1:


// Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
// Output: 7
// Explanation: We have various ancestor-node differences, some of which are given below :
// |8 - 3| = 5
// |3 - 7| = 4
// |8 - 1| = 7
// |10 - 13| = 3
// Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
// Example 2:


// Input: root = [1,null,2,null,0,3]
// Output: 3
 

// Constraints:

// The number of nodes in the tree is in the range [2, 5000].
// 0 <= Node.val <= 10^5

/**
 * Definition for a binary tree node.
 */
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
    int maxAncestorDiff(TreeNode* root) {
        auto res = iter(root);
        return get<2>(res);
    }

    tuple<int, int, int> iter(TreeNode* root) {
        int min_left = INT32_MAX;
        int max_left = INT32_MIN;
        int max_diff1 = INT32_MIN;
        if (root->left) {
            auto res1 = iter(root->left);
            min_left = get<0>(res1);
            max_left = get<1>(res1);
            max_diff1 = get<2>(res1);
        }

        int min_right = INT32_MAX;
        int max_right = INT32_MIN;
        int max_diff2 = INT32_MIN;
        if (root->right) {
            auto res2 = iter(root->right);
            min_right = get<0>(res2);
            max_right = get<1>(res2);
            max_diff2 = get<2>(res2);
        }

        int min_v = min(min(min_left, min_right), root->val);
        int max_v = max(max(max_left, max_right), root->val);
        int max_diff = INT32_MIN;

        if (root->left != nullptr && root->right != nullptr) {
            int max_left_diff = max(abs(root->val - min_left), abs(root->val - max_left));
            int max_right_diff = max(abs(root->val - min_right), abs(root->val - max_right));
            int max_diff_child = max(max_diff1, max_diff2);
            max_diff = max(max(max_left_diff, max_right_diff), max_diff_child);
        } else if (root->left != nullptr) {
            max_diff = max(max(abs(root->val - min_left), abs(root->val - max_left)), max_diff1);
        } else if (root->right != nullptr) {
            max_diff = max(max(abs(root->val - min_right), abs(root->val - max_right)), max_diff2);
        }

        return {min_v, max_v, max_diff};
    }
};

int main() {
}