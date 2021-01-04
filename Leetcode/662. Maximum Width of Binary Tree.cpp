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


// Given a binary tree, write a function to get the maximum width of the given tree. The maximum width of a tree is the maximum width among all levels.

// The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

// It is guaranteed that the answer will in the range of 32-bit signed integer.

// Example 1:

// Input: 

//            1
//          /   \
//         3     2
//        / \     \  
//       5   3     9 

// Output: 4
// Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
// Example 2:

// Input: 

//           1
//          /  
//         3    
//        / \       
//       5   3     

// Output: 2
// Explanation: The maximum width existing in the third level with the length 2 (5,3).
// Example 3:

// Input: 

//           1
//          / \
//         3   2 
//        /        
//       5      

// Output: 2
// Explanation: The maximum width existing in the second level with the length 2 (3,2).
// Example 4:

// Input: 

//           1
//          / \
//         3   2
//        /     \  
//       5       9 
//      /         \
//     6           7
// Output: 8
// Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).
 

// Constraints:

// The given binary tree will have between 1 and 3000 nodes.

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

    int widthOfBinaryTree(TreeNode* root) {
        int max_width = 0;
        deque<pair<int64_t, TreeNode*>> cur, next;
        cur = {{0, root}};
        while (!cur.empty()) {
            int64_t start = (cur.front()).first;
            int64_t end = (cur.back()).first;
            int64_t width = end - start + 1;
            while (!cur.empty()) {
                auto v = cur.front();
                cur.pop_front(); 
                int64_t level = v.first;
                TreeNode *node = v.second;

                if (node->left) {
                    next.push_back({(level - start) * 2, node->left});
                }
                if (node->right) {
                    next.push_back({(level - start) * 2 + 1, node->right});
                }
            }
            cur = next;
            next.clear();
            if (width > max_width) {
                max_width = width;
            }
        }
        return max_width;
    }
};

};

int main() {
}