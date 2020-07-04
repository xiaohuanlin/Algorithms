#include <utility>
#include <stack>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;

// Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

// You should preserve the original relative order of the nodes in each of the two partitions.

// Example:

// Input: head = 1->4->3->2->5->2, x = 3
// Output: 1->2->2->4->3->5
  struct ListNode {
      int val;
      ListNode *next;
      ListNode() : val(0), next(nullptr) {}
      ListNode(int x) : val(x), next(nullptr) {}
      ListNode(int x, ListNode *next) : val(x), next(next) {}
  };

class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        ListNode *less = nullptr, *bigger = nullptr, *l_begin=nullptr, *b_begin=nullptr, *iter=head;

        while (iter != nullptr) {
            if (iter->val < x) {
                if (l_begin == nullptr) {
                    l_begin = iter;
                }
                if (less == nullptr) {
                    less = iter;
                } else {
                    less->next = iter;
                    less = iter;
                }
            } else {
                if (b_begin == nullptr) {
                    b_begin = iter;
                }
                if (bigger == nullptr) {
                    bigger = iter;
                } else {
                    bigger->next = iter;
                    bigger = iter;
                }
            }
            iter = iter->next;
        }

        if (l_begin == nullptr) {
            l_begin = b_begin;
        } else {
            less->next = b_begin;
        }

        if (bigger != nullptr) {
            bigger->next = nullptr;
        }
        return l_begin;
    }
};

int main() {
    Solution s;
    ListNode third(3);
    ListNode second_2(2, &third);
    ListNode second(2, &second_2);
    ListNode first(1, &second);
    auto res = s.partition(&first, 2);

    while (res != nullptr) {
        cout << res->val << "->";
        res = res->next;
    }
    cout << endl;

}