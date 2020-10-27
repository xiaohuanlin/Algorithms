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


//  Given a binary tree, find the leftmost value in the last row of the tree.

// Example 1:

// Input:

//     2
//    / \
//   1   3

// Output:
// 1

// Example 2:

// Input:

//         1
//        / \
//       2   3
//      /   / \
//     4   5   6
//        /
//       7

// Output:
// 7

// Note: You may assume the tree (i.e., the given root node) is not NULL. 

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
    int findBottomLeftValue(TreeNode* root) {
        deque<TreeNode*> current {root};
        deque<TreeNode*> next;
        int result;
        while (!current.empty()) {
            bool init = false;
            while (!current.empty()) {
                TreeNode* node = current.front();
                current.pop_front();

                if (node) {
                    if (!init) {
                        result = node->val;
                        init = true;
                    }
                    next.push_back(node->left);
                    next.push_back(node->right);
                }
            }
            current = next;
            next.clear();
        }
        return result;
    }
};

int main() {
}