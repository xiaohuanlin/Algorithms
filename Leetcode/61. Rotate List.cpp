#include <stack>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;

// Given a linked list, rotate the list to the right by k places, where k is non-negative.

// Example 1:

// Input: 1->2->3->4->5->NULL, k = 2
// Output: 4->5->1->2->3->NULL
// Explanation:
// rotate 1 steps to the right: 5->1->2->3->4->NULL
// rotate 2 steps to the right: 4->5->1->2->3->NULL
// Example 2:

// Input: 0->1->2->NULL, k = 4
// Output: 2->0->1->NULL
// Explanation:
// rotate 1 steps to the right: 2->0->1->NULL
// rotate 2 steps to the right: 1->2->0->NULL
// rotate 3 steps to the right: 0->1->2->NULL
// rotate 4 steps to the right: 2->0->1->NULL


  struct ListNode {
      int val;
      ListNode *next;
      ListNode() : val(0), next(nullptr) {}
      ListNode(int x) : val(x), next(nullptr) {}
      ListNode(int x, ListNode *next) : val(x), next(next) {}
  };
 

class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if (head == nullptr) {
            return head;
        }
        ListNode* search = head;
        ListNode* tail;
        int list_size = 1;
        while (search != nullptr && search->next != nullptr) {
            search = search->next;
            list_size++;
        }

        search->next = head;
        tail = search;

        search = head;
        k = k % list_size;
        for (int i = 0; i < k; i++) {
            search = search->next;
        }

        ListNode* new_search = head;
        while (search != tail) {
            new_search = new_search->next;
            search = search->next;
        }

        head = new_search->next;
        new_search->next = nullptr;
        return head; 
    }
};

int main() {
}
