#include <vector>
#include <stack>
#include <deque>
#include <algorithm>
#include <iostream>
#include <tuple>
#include <assert.h>
using namespace std;

// You are given the root of a binary tree where each node has a value in the range [0, 25] representing the letters 'a' to 'z'.

// Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

// As a reminder, any shorter prefix of a string is lexicographically smaller.

// For example, "ab" is lexicographically smaller than "aba".
// A leaf of a node is a node that has no children.

 

// Example 1:


// Input: root = [0,1,2,3,4,3,4]
// Output: "dba"
// Example 2:


// Input: root = [25,1,3,1,3,0,2]
// Output: "adz"
// Example 3:


// Input: root = [2,2,1,null,1,0,null,0]
// Output: "abc"
 

// Constraints:

// The number of nodes in the tree is in the range [1, 8500].
// 0 <= Node.val <= 25

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
    string smallestFromLeaf(TreeNode* root) {
        deque<char> tmp, result;
        dfs(tmp, result, root);
        return {result.begin(), result.end()};
    }

    void dfs(deque<char>& tmp, deque<char>& result, TreeNode* item) {
        if (item == nullptr) {
            return;
        }

        tmp.push_front(item->val + 'a');

        if (item->left == nullptr && item->right == nullptr) {
            // it is the end
            if (result.empty() || isSmall(tmp, result)) {
                result = tmp;
            }
            tmp.pop_front();
            return;
        }

        dfs(tmp, result, item->left);
        dfs(tmp, result, item->right);
        tmp.pop_front();
    }

    bool isSmall(deque<char>& a, deque<char>& b) {
        for (int i = 0; i < a.size() && i < b.size(); i++) {
            if (a[i] < b[i]) {
                return true;
            } else if (a[i] > b[i]) {
                return false;
            }
        }
        return a.size() < b.size() ? true : false;
    }
};


int main() {
}