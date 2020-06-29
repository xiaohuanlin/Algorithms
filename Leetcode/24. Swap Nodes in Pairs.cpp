#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;

// Given a linked list, swap every two adjacent nodes and return its head.

// You may not modify the values in the list's nodes, only nodes itself may be changed.

 

// Example:

// Given 1->2->3->4, you should return the list as 2->1->4->3.

  struct ListNode {
      int val;
      ListNode *next;
      ListNode() : val(0), next(nullptr) {}
      ListNode(int x) : val(x), next(nullptr) {}
      ListNode(int x, ListNode *next) : val(x), next(next) {}
  };
 

class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        if (head == nullptr) {
            return head;
        }

        ListNode* parent = nullptr;
        ListNode* first = head;
        ListNode* second= head->next;

        while (first != nullptr && second != nullptr) {
            first->next = second->next;
            if (parent != nullptr) {
                parent->next = second;
            } else {
                head = second;
            }
            second->next = first;

            parent = first;
            first = first->next;
            if (first == nullptr) {
                break;
            }
            second = first->next;
        }
        return head;
    }
};


int main() {
    Solution s;
    ListNode head(5);
    ListNode second(3);
    ListNode third(6);
    ListNode forth(9);
    
    head.next = &second;
    second.next = &third;
    third.next = &forth;

    auto res = s.swapPairs(&head);
    while (res != nullptr) {
        cout << res->val << ',';
        res = res->next;
    }
}