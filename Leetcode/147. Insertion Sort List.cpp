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


// Sort a linked list using insertion sort.


// A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
// With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list
 

// Algorithm of Insertion Sort:

// Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
// At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
// It repeats until no input elements remain.

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
    ListNode* insertionSortList(ListNode* head) {
        ListNode *res = nullptr, *temp, *iter, *iter_parent;

        while (head) {
            temp = head;
            head = head->next;        
            temp->next = nullptr;

            if (!res) {
                res = temp;
            } else {
                iter = res;
                iter_parent = nullptr;
                while (iter && iter->val < temp->val) {
                    iter_parent = iter;
                    iter = iter->next; 
                }

                if (!iter_parent) {
                    res = temp;
                    temp->next = iter;
                } else {
                    iter_parent->next = temp;
                    temp->next = iter;
                }

            }
        }
        return res;
    }
};


int main() {

}