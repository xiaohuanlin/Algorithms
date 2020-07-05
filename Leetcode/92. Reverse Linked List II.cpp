#include <math.h>
#include <utility>
#include <stack>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;

// Reverse a linked list from position m to n. Do it in one-pass.

// Note: 1 ≤ m ≤ n ≤ length of list.

// Example:

// Input: 1->2->3->4->5->NULL, m = 2, n = 4
// Output: 1->4->3->2->5->NULL


  struct ListNode {
      int val;
      ListNode *next;
      ListNode() : val(0), next(nullptr) {}
      ListNode(int x) : val(x), next(nullptr) {}
      ListNode(int x, ListNode *next) : val(x), next(next) {}
  };
  

class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int m, int n) {
        if (head == nullptr) {
            return head;
        }

        ListNode *iter = head;
        ListNode *left_last = nullptr, *middle_first, *middle_last, *right_first, *tmp;
        int count = 0;
        while (iter != nullptr && count < m - 1) {
            left_last = iter;
            iter = iter->next;
            count ++;
        }

        if (iter == nullptr) {
            return head;
        }

        // do reverse for middle part
        middle_last = middle_first = iter;
        while (iter != nullptr && count < n) {
            tmp = iter->next;
            iter->next = middle_first;
            middle_first = iter;
            iter = tmp;
            count ++;
        }

        middle_last->next = iter;
        if (left_last != nullptr) {
            left_last->next = middle_first;
        } else {
            head = middle_first;
        }
        return head;
    }
};

int main() {
}