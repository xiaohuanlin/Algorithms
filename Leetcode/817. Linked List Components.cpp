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


// You are given the head of a linked list containing unique integer values and an integer array nums that is a subset of the linked list values.

// Return the number of connected components in nums where two values are connected if they appear consecutively in the linked list.

 

// Example 1:


// Input: head = [0,1,2,3], nums = [0,1,3]
// Output: 2
// Explanation: 0 and 1 are connected, so [0, 1] and [3] are the two connected components.
// Example 2:


// Input: head = [0,1,2,3,4], nums = [0,3,1,4]
// Output: 2
// Explanation: 0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the two connected components.
 

// Constraints:

// The number of nodes in the linked list is n.
// 1 <= n <= 10^4
// 0 <= Node.val < n
// All the values Node.val are unique.
// 1 <= nums.length <= n
// 0 <= nums[i] <= n
// All the values of nums are unique.

/**
 * Definition for singly-linked list.
 */
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    int numComponents(ListNode* head, vector<int>& nums) {
        // we make map for the whole list to reduce the searching time
        unordered_map<int, ListNode*> maps;
        while (head != nullptr) {
            maps[head->val] = head;
            head = head->next;
        }

        unordered_set<int> nums_set(nums.begin(), nums.end());
        unordered_set<int> access_set;

        for (auto& num : nums) {
            auto node = maps[num];
            while (node->next && nums_set.find(node->next->val) != nums_set.end()
                && access_set.find(node->next->val) == access_set.end()) {
                access_set.insert(node->next->val);
                node = node->next;
            }
        }
        return nums.size() - access_set.size();
    }
};


int main() {
}
