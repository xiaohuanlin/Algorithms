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


// Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

// Follow up:
// What if the linked list is extremely large and its length is unknown to you? Could you solve this efficiently without using extra space?

// Example:

// // Init a singly linked list [1,2,3].
// ListNode head = new ListNode(1);
// head.next = new ListNode(2);
// head.next.next = new ListNode(3);
// Solution solution = new Solution(head);

// // getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
// solution.getRandom();


  struct ListNode {
      int val;
      ListNode *next;
      ListNode() : val(0), next(nullptr) {}
      ListNode(int x) : val(x), next(nullptr) {}
      ListNode(int x, ListNode *next) : val(x), next(next) {}
  };

class Solution {
    ListNode *node;
    int size = 0;
public:
    /** @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node. */
    Solution(ListNode* head): node(head) {
    }
    
    /** Returns a random node's value. */
    int getRandom() {
        int random = rand();
        int count = 0;
        ListNode *tmp = node;
        for (int i = 0; i < random; ++i) {
            tmp = tmp->next;
            ++count;
            if (!tmp) {
                size = count;
                tmp = node;
                random %= size;
                i -= size;
            }
        }
        return tmp->val;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(head);
 * int param_1 = obj->getRandom();
 */

int main() {
    ListNode *head = new ListNode(10);
    head->next = new ListNode(11);
    head->next->next = new ListNode(12);
    head->next->next->next = new ListNode(13);
    Solution s(head);
    for (int i = 0; i < 10; ++i) {
        cout << s.getRandom() << '/' << endl;
    }
    cout << endl;
}