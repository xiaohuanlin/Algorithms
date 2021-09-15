#include <vector>
#include <set>
#include <algorithm>
#include <iostream>
#include <tuple>
#include <assert.h>
using namespace std;


// Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

// k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

// You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

// Example 1:


// Input: head = [1,2,3,4,5], k = 2
// Output: [2,1,4,3,5]
// Example 2:


// Input: head = [1,2,3,4,5], k = 3
// Output: [3,2,1,4,5]
// Example 3:

// Input: head = [1,2,3,4,5], k = 1
// Output: [1,2,3,4,5]
// Example 4:

// Input: head = [1], k = 1
// Output: [1]
 

// Constraints:

// The number of nodes in the list is in the range sz.
// 1 <= sz <= 5000
// 0 <= Node.val <= 1000
// 1 <= k <= sz
 

// Follow-up: Can you solve the problem in O(1) extra memory space?


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
    ListNode* reverseKGroup(ListNode* head, int k) {
        int length = getLength(head);
        int revert_times = length / k;
        ListNode dummy;

        ListNode* iter = head;
        ListNode* prev = &dummy;
        for (int i = 0; i < revert_times; i++) {
            auto item = reverse(iter, prev, k);
            prev = get<0>(item);
            iter = get<1>(item);
        }

        prev->next = iter;
        return dummy.next;
    }

    int getLength(ListNode* head) {
        int count = 0;
        while (head != nullptr) {
            head = head->next;
            count++;
        }
        return count;
    }

    tuple<ListNode*, ListNode*> reverse(ListNode* current, ListNode* last_tail, int length) {
        int count = 0;
        ListNode* tail = current;
        ListNode* prev = nullptr;

        while (count++ < length) {
            ListNode* next = current->next;
            current->next = prev;
            prev = current;
            current = next;
        }

        // link the node
        last_tail->next = prev;
        return {tail, current};
    }
};

int main() {
}