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
using namespace std;


// Given a singly linked list L: L0→L1→…→Ln-1→Ln,
// reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

// You may not modify the values in the list's nodes, only nodes itself may be changed.

// Example 1:

// Given 1->2->3->4, reorder it to 1->4->2->3.
// Example 2:

// Given 1->2->3->4->5, reorder it to 1->5->2->4->3.


  struct ListNode {
      int val;
      ListNode *next;
      ListNode() : val(0), next(nullptr) {}
      ListNode(int x) : val(x), next(nullptr) {}
      ListNode(int x, ListNode *next) : val(x), next(next) {}
  };

class Solution {
public:
    void reorderList(ListNode* head) {
        ListNode *slow = head, *fast = head, *tail=head;
        while (fast && fast->next) {
            slow = slow->next;
            tail = fast->next;
            fast = fast->next->next;
        }
        
        if (fast) {
            tail = fast;
        }

        // reverse half
        ListNode *tmp, *parent = nullptr;

        while (slow) {
            tmp = slow->next;
            slow->next = parent;
            parent = slow;
            slow = tmp;
        }

        slow = head;
        while (slow) {
            tmp = slow->next;
            slow->next = tail;
            slow = tmp;
            
            if(slow == tail) {
                break;
            }

            tmp = tail->next;
            tail->next = slow;
            tail = tmp;
        }
    }
};

int main() {
}