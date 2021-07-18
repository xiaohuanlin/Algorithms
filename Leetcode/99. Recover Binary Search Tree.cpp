#include <vector>
#include <stack>
#include <iostream>
#include <tuple>
#include <assert.h>
using namespace std;

// You are given the root of a binary search tree (BST), where exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

// Follow up: A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

 

// Example 1:


// Input: root = [1,3,null,null,2]
// Output: [3,1,null,null,2]
// Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.
// Example 2:


// Input: root = [3,1,4,null,null,2]
// Output: [2,1,4,null,null,3]
// Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.
 

// Constraints:

// The number of nodes in the tree is in the range [2, 1000].
// -2^31 <= Node.val <= 2^31 - 1

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
    void recoverTree(TreeNode* root) {
        TreeNode *current = root, *candidate = nullptr, *first = nullptr, *second = nullptr;
        while (current) {
            TreeNode* prev = current->left;
            if (prev) {
                while (prev->right && prev->right != current) {
                    prev = prev->right;
                }

                if (prev->right == current) {
                    // remove it
                    prev->right = nullptr;
                    if (candidate && candidate->val > current->val) {
                        // recode the result
                        if (!first) {
                            first = candidate;
                        }
                        second = current;
                    }
                    candidate = current;
                    current = current->right;
                } else {
                    // add it 
                    prev->right = current;
                    current = current->left;
                }
            } else {
                if (candidate && candidate->val > current->val) {
                    // recode the result
                    if (!first) {
                        first = candidate;
                    }
                    second = current;
                }
                candidate = current;
                current = current->right;
            }
        }

        // swap two node
        int tmp = first->val;
        first->val = second->val;
        second->val = tmp;
        return;
    }
};

int main() {
    // Morris traversal
    Solution s;
    TreeNode second(2);
    TreeNode third(3, nullptr, &second);
    TreeNode first(1, &third, nullptr);
    s.recoverTree(&first);
    assert(first.val == 3);
    assert(first.left->val == 1);
    assert(first.left->right->val == 2);

    TreeNode first_node(1);
    TreeNode second_node(2);
    TreeNode fourth_node(4, &second_node, nullptr);
    TreeNode third_node(3, &first_node, &fourth_node);
    s.recoverTree(&third_node);
    assert(third_node.val == 2);
    assert(second_node.val == 3);
}