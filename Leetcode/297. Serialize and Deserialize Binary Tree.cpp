#include <vector>
#include <set>
#include <algorithm>
#include <iostream>
#include <tuple>
#include <assert.h>
using namespace std;


// Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

// Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

// Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

 

// Example 1:


// Input: root = [1,2,3,null,null,4,5]
// Output: [1,2,3,null,null,4,5]
// Example 2:

// Input: root = []
// Output: []
// Example 3:

// Input: root = [1]
// Output: [1]
// Example 4:

// Input: root = [1,2]
// Output: [1,2]
 

// Constraints:

// The number of nodes in the tree is in the range [0, 104].
// -1000 <= Node.val <= 1000


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
 

class Codec {
public:
    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        if (root == nullptr) {
            return "";
        }

        auto left = serialize(root->left);
        auto right = serialize(root->right);

        return to_string(root->val) + "/" + to_string(left.length()) + "/" + left + right;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        if (data == "") {
            return nullptr;
        }
        auto first = data.find_first_of('/');
        auto second = data.find_first_of('/', first + 1);
        int val = stoi(data.substr(0, first));
        int left_length = stoi(data.substr(first + 1, second - first - 1));
        
        auto left = deserialize(data.substr(second + 1, left_length));
        auto right = deserialize(data.substr(second + 1 + left_length));
        return new TreeNode(val, left, right);
    }
};


int main() {
    TreeNode a{1}, b{2}, c{3};
    a.left = &b;
    a.right = &c;

    Codec code;
    auto res = code.serialize(&a);

    code.deserialize(res);
}