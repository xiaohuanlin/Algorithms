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


// Sort a linked list in O(n log n) time using constant space complexity.

// Example 1:

// Input: 4->2->1->3
// Output: 1->2->3->4
// Example 2:

// Input: -1->5->3->4->0
// Output: -1->0->3->4->5
 
  struct ListNode {
      int val;
      ListNode *next;
      ListNode() : val(0), next(nullptr) {}
      ListNode(int x) : val(x), next(nullptr) {}
      ListNode(int x, ListNode *next) : val(x), next(next) {}
  };
 
class Solution {
public:
    ListNode* sortList(ListNode* head) {
        if (!head) {
            return head;
        }

        ListNode *iter, *res;

        iter = res = head;
        while (iter && iter->next) {
            iter = iter->next;
        }

        partition(res, head, iter, true);
        return res;
    }

    void partition(ListNode* &res, ListNode* head, ListNode* tail, bool change) {
        if (!head || !tail) {
            return;
        }

        if (head == tail) {
            return;
        }
        ListNode *iter, *left_tail, *right_tail;

        iter = head;
        left_tail = nullptr;
        right_tail = tail;
        while (iter && iter != tail) {
            if (iter->val <= tail->val) {
                left_tail = iter;
                iter = iter->next;
            } else {
                if (!left_tail) {
                    head = iter->next;
                } else {
                    left_tail->next = iter->next;
                }
                iter->next = right_tail->next;
                right_tail->next = iter;
                right_tail = iter;

                if (!left_tail) {
                    iter = head;
                } else {
                    iter = left_tail->next;
                }
            }
        }

        if (change && head) {
            res = head;
        }

        partition(res, head, left_tail, change);
        partition(res, tail, right_tail, false);
    }
};


int main() {
    Solution s;
    ListNode forth(3);
    ListNode third(1, &forth);
    ListNode second(2, &third);
    ListNode first(4, &second);

    s.sortList(&first);
}