#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;
// Given a linked list, remove the n-th node from the end of list and return its head.

// Example:

// Given linked list: 1->2->3->4->5, and n = 2.

// After removing the second node from the end, the linked list becomes 1->2->3->5.
// Note:

// Given n will always be valid.

// Follow up:

// Could you do this in one pass?

 struct ListNode {
      int val;
      ListNode *next;
      ListNode() : val(0), next(nullptr) {}
      ListNode(int x) : val(x), next(nullptr) {}
      ListNode(int x, ListNode *next) : val(x), next(next) {}
  };
 

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if (head == nullptr) {
            return nullptr;
        }

        ListNode* pFirst = head;
        ListNode* pSecond = head;

        int count = 0;
        while (count++ < n) {
            pFirst = pFirst->next;
        }

        ListNode* pParent = nullptr;
        while (pFirst != nullptr) {
            pFirst = pFirst->next;
            pSecond = pSecond->next;

            if (pParent == nullptr) {
                pParent = head;
            } else {
                pParent = pParent->next;
            }
        }

        if (pParent == nullptr) {
            return pSecond->next;
        }

        pParent->next = pSecond->next;
        return head;
    }
};


int main() {
}