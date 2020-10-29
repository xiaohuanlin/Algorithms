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


// Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

 

 

// Example 1:


// Input: root = [1,3,2,5,3,null,9]
// Output: [1,3,9]
// Example 2:

// Input: root = [1,2,3]
// Output: [1,3]
// Example 3:

// Input: root = [1]
// Output: [1]
// Example 4:

// Input: root = [1,null,2]
// Output: [1,2]
// Example 5:

// Input: root = []
// Output: []
 

// Constraints:

// The number of nodes in the tree will be in the range [0, 104].
// -231 <= Node.val <= 231 - 1

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
    vector<int> largestValues(TreeNode* root) {
        deque<TreeNode*> current {root}, next;        
        vector<int> result;
        if (!root) {
            return result;
        }

        while (!current.empty()) {
            int max_v = INT32_MIN;
            while (!current.empty()) {
                TreeNode* node = current.front();
                current.pop_front();
                max_v = max(max_v, node->val);
                if (node->left) {
                    next.push_back(node->left);
                }
                if (node->right) {
                    next.push_back(node->right);
                }
            }
            current = next;
            next.clear();
            result.push_back(max_v);
        }
        return result;
    }
};


int main() {
}