#include <vector>
#include <deque>
#include <iostream>
#include <tuple>
#include <assert.h>
using namespace std;


// Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

// Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

 

// Example 1:


// Input: root = [1,7,0,7,-8,null,null]
// Output: 2
// Explanation: 
// Level 1 sum = 1.
// Level 2 sum = 7 + 0 = 7.
// Level 3 sum = 7 + -8 = -1.
// So we return the level with the maximum sum which is level 2.
// Example 2:

// Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
// Output: 2
 

// Constraints:

// The number of nodes in the tree is in the range [1, 104].
// -10^5 <= Node.val <= 10^5


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
    int maxLevelSum(TreeNode* root) {
        deque<TreeNode*> candidates, current;
        candidates.push_back(root);

        int res = 0;
        int max_level = INT32_MIN;
        int count = 1;
        while (!candidates.empty()) {
            int sum_level = 0;
            while (!candidates.empty()) {
                auto node = candidates.front();
                candidates.pop_front();
                sum_level += node->val;

                if (node->left) {
                    current.push_back(node->left);
                }

                if (node->right) {
                    current.push_back(node->right);
                }
            }

            if (max_level < sum_level) {
                res = count;
                max_level = sum_level;
            }

            count++;
            candidates = current;
            current = {};
        }
        return res;
    }
};

int main() {
}