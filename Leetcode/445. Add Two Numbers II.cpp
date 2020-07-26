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


// You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

// You may assume the two numbers do not contain any leading zero, except the number 0 itself.

// Follow up:
// What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

// Example:

// Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
// Output: 7 -> 8 -> 0 -> 7


  struct ListNode {
      int val;
      ListNode *next;
      ListNode() : val(0), next(nullptr) {}
      ListNode(int x) : val(x), next(nullptr) {}
      ListNode(int x, ListNode *next) : val(x), next(next) {}
  };

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int left_count = 0;
        int right_count = 0;
        ListNode *iter = l1;
        while (iter) {
            left_count++;
            iter = iter->next;
        }

        iter = l2;
        while (iter) {
            right_count++;
            iter = iter->next;
        }

        ListNode *longer, *shorter;
        if (left_count > right_count) {
            longer = l1;
            shorter = l2;
        } else {
            longer = l2;
            shorter = l1;
        }

        int length = max(left_count, right_count);
        ListNode *add_v = new ListNode(0), *carry = nullptr;
        ListNode *add_head = add_v, *carry_head = carry;
        int count = 0;

        bool need_next = false;
        while (count < length) {
            int left = longer->val;
            int right = 0;
            if (count >= length - min(left_count, right_count)) {
                right = shorter->val; 
                shorter = shorter->next;
            }
            int add_v_d = (left + right) % 10;
            int carry_d = (left + right) / 10;
            if (carry_d > 0) {
                need_next = true;
            }
            longer = longer->next;

            iter = new ListNode(add_v_d);
            add_v->next = iter;
            add_v = iter;

            iter = new ListNode(carry_d);
            if (carry) {
                carry->next = iter;
            } else {
                carry_head = iter;
            }
            carry = iter;
            count++;
        }

        iter = new ListNode(0);
        if (carry) {
            carry->next = iter;
        } else {
            carry_head = iter;
            carry = iter;
        }

        if (need_next) {
            return addTwoNumbers(add_head, carry_head);
        }

        while (add_head && add_head->val == 0 && add_head->next) {
            add_head = add_head->next;
        }

        return add_head;
    }
};

int main() {
}