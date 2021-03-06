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

// Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

// You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

// Example 1:

// Input: 1->2->3->4->5->NULL
// Output: 1->3->5->2->4->NULL
// Example 2:

// Input: 2->1->3->5->6->4->7->NULL
// Output: 2->3->6->7->1->5->4->NULL
 

// Constraints:

// The relative order inside both the even and odd groups should remain as it was in the input.
// The first node is considered odd, the second node even and so on ...
// The length of the linked list is between [0, 10^4].


  struct ListNode {
      int val;
      ListNode *next;
      ListNode() : val(0), next(nullptr) {}
      ListNode(int x) : val(x), next(nullptr) {}
      ListNode(int x, ListNode *next) : val(x), next(next) {}
  };

class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {
		if (!head) {
			return head;
		}
		ListNode* odd = head, *even = head->next, *tmp, *tail=nullptr;
		int count = 0;
		while (head && head->next) {
			if (count % 2 == 0) {
				tail = head;
			}
			tmp = head->next;
			head->next = head->next->next;
			head = tmp;
			count++;
		}

		if (tail) {
			if (tail->next) {
				tail->next->next = even;
			} else {
				tail->next = even;
			}
		}
		return odd;
    }
};


int main() {
}