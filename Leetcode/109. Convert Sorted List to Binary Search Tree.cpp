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


// Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

// For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

// Example:

// Given the sorted linked list: [-10,-3,0,5,9],

// One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

//       0
//      / \
//    -3   9
//    /   /
//  -10  5

  struct ListNode {
      int val;
      ListNode *next;
      ListNode() : val(0), next(nullptr) {}
      ListNode(int x) : val(x), next(nullptr) {}
      ListNode(int x, ListNode *next) : val(x), next(next) {}
  };
  
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
    TreeNode* sortedListToBST(ListNode* head) {
        vector<int> nodes;
        while (head != nullptr) {
            nodes.push_back(head->val);
            head = head->next;
        }
        return buildTree(nodes, 0, nodes.size());
    }

    TreeNode* buildTree(vector<int> &nodes, int start, int end) {
        if (start >= end) {
            return nullptr;
        }
        int middle = start + (end - start) / 2;
        TreeNode * root = new TreeNode(nodes[middle]);
        root->left = buildTree(nodes, start, middle);
        root->right = buildTree(nodes, middle+1, end);
        return root;
    }
};

int main() {
}