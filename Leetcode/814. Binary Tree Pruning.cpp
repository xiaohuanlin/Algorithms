#include <vector>
#include <stack>
#include <iostream>
#include <tuple>
#include <assert.h>
using namespace std;


// Given the root of a binary tree, return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

// A subtree of a node node is node plus every node that is a descendant of node.

 

// Example 1:


// Input: root = [1,null,0,0,1]
// Output: [1,null,0,null,1]
// Explanation: 
// Only the red nodes satisfy the property "every subtree not containing a 1".
// The diagram on the right represents the answer.
// Example 2:


// Input: root = [1,0,1,0,0,0,1]
// Output: [1,null,1,null,1]
// Example 3:


// Input: root = [1,1,0,1,1,0,1,0]
// Output: [1,1,0,1,1,null,1]

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
    struct Wrapper {
        TreeNode* node;
        TreeNode* parent;
        bool is_left;
        bool access;
    };

    TreeNode* pruneTree(TreeNode* root) {
        stack<Wrapper> candidates;
        candidates.push({root, nullptr, false, false});
        while (!candidates.empty()) {
            auto wrapper = candidates.top();
            candidates.pop();
            // push value to stack
            if (!wrapper.access) {
                candidates.push({wrapper.node, wrapper.parent, wrapper.is_left, true});
                if (wrapper.node->right != nullptr) {
                    candidates.push({wrapper.node->right, wrapper.node, false, false});
                }
                if (wrapper.node->left != nullptr) {
                    candidates.push({wrapper.node->left, wrapper.node, true, false});
                }
            }

            // remove 0 node
            if (wrapper.access && wrapper.node->val == 0
                && wrapper.node->left == nullptr && wrapper.node->right == nullptr) {
                if (wrapper.parent != nullptr) {
                    if (wrapper.is_left) {
                        wrapper.parent->left = nullptr;
                    } else {
                        wrapper.parent->right = nullptr;
                    }
                } else {
                    root = nullptr;
                }
            }
        }
        return root;
    }
};


int main() {
    Solution s;
}