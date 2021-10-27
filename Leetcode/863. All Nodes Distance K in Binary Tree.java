import java.util.*;

import javax.security.auth.login.CredentialException;

// Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

// You can return the answer in any order.

 

// Example 1:


// Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
// Output: [7,4,1]
// Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
// Example 2:

// Input: root = [1], target = 1, k = 3
// Output: []
 

// Constraints:

// The number of nodes in the tree is in the range [1, 500].
// 0 <= Node.val <= 500
// All the values Node.val are unique.
// target is the value of one of the nodes in the tree.
// 0 <= k <= 1000

class Solution863 {
    /**
     * Definition for a binary tree node.
     */
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }

    public List<Integer> distanceK(TreeNode root, TreeNode target, int k) {
        // generate parent node mapping
        Map<Integer, TreeNode> mapping = new HashMap<>();
        getParentsMapping(root.left, root, mapping);
        getParentsMapping(root.right, root, mapping);

        // find all node that its distances in this set
        List<Integer> res = new ArrayList<>();
        Set<Integer> visited = new HashSet<>();
        Queue<TreeNode> q = new LinkedList<>();
        int steps = 0;
        q.offer(target);

        while (!q.isEmpty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                TreeNode current = q.poll();
                if (current == null) {
                    continue;
                }
                if (visited.contains(current.val)) {
                    continue;
                }
                if (steps == k) {
                    res.add(current.val);
                }
                visited.add(current.val);
                q.offer(current.left);
                q.offer(current.right);
                q.offer(mapping.get(current.val));
            }
            steps++;
        }
        return res;
    }

    public void getParentsMapping(TreeNode current, TreeNode parent, Map<Integer, TreeNode> res) {
        if (current == null) {
            return;
        }

        res.put(current.val, parent);
        getParentsMapping(current.left, current, res);
        getParentsMapping(current.right, current, res);
    }
}

class Driver863 {
    public static void main(String[] args) {
    }
}