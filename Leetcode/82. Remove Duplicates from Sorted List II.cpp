#include <utility>
#include <stack>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
using namespace std;

// Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

// Return the linked list sorted as well.

// Example 1:

// Input: 1->2->3->3->4->4->5
// Output: 1->2->5
// Example 2:

// Input: 1->1->1->2->3
// Output: 2->3

  struct ListNode {
      int val;
      ListNode *next;
      ListNode() : val(0), next(nullptr) {}
      ListNode(int x) : val(x), next(nullptr) {}
      ListNode(int x, ListNode *next) : val(x), next(next) {}
  };

class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if (head == nullptr || head->next == nullptr) {
            return head;
        }

        ListNode *pprevious = nullptr, *previous = head, *iter= head->next;
        while (iter != nullptr) {
            
            if (iter->val != previous->val) {
                previous->next = iter;
                pprevious = previous;
                previous = iter;
            } else {
                while (iter != nullptr && iter->val == previous->val) {
                    iter = iter->next;
                }

                previous = iter;
                if (pprevious != nullptr) {
                    pprevious->next = iter;
                } else {
                    head = previous;
                }
            }
            if (iter != nullptr) {
                iter = iter->next;
            }
        }
        return head;
    }
};

int main() {
    Solution s;
    ListNode third(3);
    ListNode second_2(2, &third);
    ListNode second(2, &second_2);
    ListNode first(1, &second);
    auto res = s.deleteDuplicates(&first);

    while (!res) {
        cout << res->val << "->";
    }
    cout << endl;

}