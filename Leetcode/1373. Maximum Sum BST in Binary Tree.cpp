#include <vector>
#include <set>
#include <algorithm>
#include <iostream>
#include <tuple>
#include <assert.h>
using namespace std;


// Given a binary tree root, return the maximum sum of all keys of any sub-tree which is also a Binary Search Tree (BST).

// Assume a BST is defined as follows:

// The left subtree of a node contains only nodes with keys less than the node's key.
// The right subtree of a node contains only nodes with keys greater than the node's key.
// Both the left and right subtrees must also be binary search trees.
 

// Example 1:



// Input: root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
// Output: 20
// Explanation: Maximum sum in a valid Binary search tree is obtained in root node with key equal to 3.
// Example 2:



// Input: root = [4,3,null,1,2]
// Output: 2
// Explanation: Maximum sum in a valid Binary search tree is obtained in a single root node with key equal to 2.
// Example 3:

// Input: root = [-4,-2,-5]
// Output: 0
// Explanation: All values are negatives. Return an empty BST.
// Example 4:

// Input: root = [2,1,3]
// Output: 6
// Example 5:

// Input: root = [5,4,8,3,null,6,3]
// Output: 7
 

// Constraints:

// The number of nodes in the tree is in the range [1, 4 * 10^4].
// -4 * 10^4 <= Node.val <= 4 * 10^4


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
    struct Result {
        int min;
        int max;
        int sum;
        bool valid;
    };

    int maxSumBST(TreeNode* root) {
        int max_v = 0;
        iter(root, max_v);
        return max_v;
    }

    Result iter(TreeNode* root, int& max_v) {
        if (root == nullptr) {
            return {INT32_MAX, INT32_MIN, 0, true};
        }
        auto left = iter(root->left, max_v);
        auto right = iter(root->right, max_v);
        if (left.max < root->val && root->val < right.min && left.valid && right.valid) {
            int sum = left.sum + right.sum + root->val;
            if (sum > max_v) {
                max_v = sum;
            }
            return {min(left.min, root->val), max(right.max, root->val), sum, true};
        }
        return {0, 0, 0, false};
    }
};


int main() {
}