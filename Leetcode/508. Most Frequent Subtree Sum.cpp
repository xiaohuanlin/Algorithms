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
#include <queue>
using namespace std;


// Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.

// Examples 1
// Input:

//   5
//  /  \
// 2   -3
// return [2, -3, 4], since all the values happen only once, return all of them in any order.
// Examples 2
// Input:

//   5
//  /  \
// 2   -5
// return [2], since 2 happens twice, however -5 only occur once.
// Note: You may assume the sum of values in any subtree is in the range of 32-bit signed integer.


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
    vector<int> findFrequentTreeSum(TreeNode* root) {
      unordered_map<int,int> res;
      vector<int> ans;
      int max_value = 0;
      core(res, root, max_value);

      for (const auto &item: res) {
        if (item.second == max_value) {
          ans.push_back(item.first);
        }
      }
      return ans;
    }

    int core(unordered_map<int, int> &res, TreeNode* root, int& max_count) {
      if (!root) {
        return 0;
      }

      int total = root->val;
      total += core(res, root->left, max_count);
      total += core(res, root->right, max_count);
      res[total]++;
      max_count = max(max_count, res[total]);
      return total;
    }
};

int main() {
}
