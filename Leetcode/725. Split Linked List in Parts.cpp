#include <vector>
#include <array>
#include <tuple>
#include <assert.h>
#include <algorithm>
using namespace std;

// Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.

// The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.

// The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.

// Return an array of the k parts.

 

// Example 1:


// Input: head = [1,2,3], k = 5
// Output: [[1],[2],[3],[],[]]
// Explanation:
// The first element output[0] has output[0].val = 1, output[0].next = null.
// The last element output[4] is null, but its string representation as a ListNode is [].
// Example 2:


// Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
// Output: [[1,2,3,4],[5,6,7],[8,9,10]]
// Explanation:
// The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.
 

// Constraints:

// The number of nodes in the list is in the range [0, 1000].
// 0 <= Node.val <= 1000
// 1 <= k <= 50

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
    vector<ListNode*> splitListToParts(ListNode* head, int k) {
        ListNode *iter = head;
        int count = 0;
        while (iter != nullptr) {
            count++;
            iter = iter->next;
        }

        int over_count = count % k;
        int size = count / k;

        vector<ListNode*> res;
        int current_over_count = 0;
        int current_size = 0;
        ListNode *current_node = nullptr, *previous;
        iter = head;
        while (iter != nullptr) {
            if (current_node == nullptr) {
                current_node = iter;
            }

            previous = iter;
            iter = iter->next;
            if (++current_size == size + (current_over_count < over_count ? 1 : 0)) {
                previous->next = nullptr;
                res.push_back(current_node);
                current_node = nullptr;
                ++current_over_count;
                current_size = 0;
            }
        }

        while (res.size() < k) {
            res.push_back(nullptr);
        }
        return res;
    }
};

int main() {
    Solution s;
    ListNode a, b, c;
    a.next = &b;
    b.next = &c;
    auto res = s.splitListToParts(&a, 5);
    vector<ListNode*> checks = {&a, &b, &c, nullptr, nullptr};
    assert(res == checks);
}