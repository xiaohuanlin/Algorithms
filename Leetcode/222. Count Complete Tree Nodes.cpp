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


// Given a complete binary tree, count the number of nodes.

// Note:

// Definition of a complete binary tree from Wikipedia:
// In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

// Example:

// Input: 
//     1
//    / \
//   2   3
//  / \  /
// 4  5 6

// Output: 6


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
    int countNodes(TreeNode* root) {
        deque<TreeNode*> candidates;
        candidates.push_back(root);

        int count = 0;
        while (!candidates.empty()) {
            auto item = candidates.front();
            candidates.pop_front();

            if (!item) {
                continue;
            }
            count++;
            candidates.push_back(item->left);
            candidates.push_back(item->right);
        }
        return count;
    }

    int countNodesNew(TreeNode* root) {
        if (!root) {
            return 0;
        }

        TreeNode* iter = root;
        int length = 0;
        while (iter && iter->left) {
            iter = iter->left;
            length++;
        }

        int total = 0;
        while (root) {
            int left_length = 0;
            iter = root->left;
            if (iter) {
                left_length++;
            }
            while (iter && iter->right) {
                iter = iter->right; 
                left_length++;
            }
            if (left_length < length) {
                total += pow(2, --length);
                root = root->left;
            } else {
                total += pow(2, length--);
                root = root->right;
            }
        }
        return total;
    }
};


int main() {
}
