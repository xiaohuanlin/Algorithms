import java.util.*;

// You are given the head of a linked list with n nodes.

// For each node in the list, find the value of the next greater node. That is, for each node, find the value of the first node that is next to it and has a strictly larger value than it.

// Return an integer array answer where answer[i] is the value of the next greater node of the ith node (1-indexed). If the ith node does not have a next greater node, set answer[i] = 0.

 

// Example 1:


// Input: head = [2,1,5]
// Output: [5,5,0]
// Example 2:


// Input: head = [2,7,4,3,5]
// Output: [7,0,5,5,0]
 

// Constraints:

// The number of nodes in the list is n.
// 1 <= n <= 104
// 1 <= Node.val <= 109


class Solution863 {
    /**
     * Definition for a binary tree node.
     */
    public class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

    public int[] nextLargerNodes(ListNode head) {
        List<Integer> list = new ArrayList<>();
        while (head != null) {
            list.add(head.val);
            head = head.next;
        }

        int[] res = new int[list.size()];
        Stack<Integer> s = new Stack<>();
        for (int i = list.size() - 1; i >= 0; i--) {
            while (!s.empty()) {
                int v = s.pop();
                if (v > list.get(i)) {
                    s.add(v);
                    res[i] = v;
                    break;
                }
            }
            s.push(list.get(i));
        }
        return res;
    }
}

class Driver863 {
    public static void main(String[] args) {
    }
}