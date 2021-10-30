import java.util.*;

// Given the root of a binary tree, each node in the tree has a distinct value.

// After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

// Return the roots of the trees in the remaining forest. You may return the result in any order.

 

// Example 1:


// Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
// Output: [[1,2,null,4],[6],[7]]
// Example 2:

// Input: root = [1,2,4,null,3], to_delete = [3]
// Output: [[1,2,4]]
 

// Constraints:

// The number of nodes in the given tree is at most 1000.
// Each node has a distinct value between 1 and 1000.
// to_delete.length <= 1000
// to_delete contains distinct values between 1 and 1000.

class Solution1110 {
    /**
     * Definition for a binary tree node.
     */
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode() {}
        TreeNode(int val) { this.val = val; }
        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public List<TreeNode> delNodes(TreeNode root, int[] to_delete) {
        TreeNode dumNode = new TreeNode(1001, root, null);
        TreeNode dumParentNode = new TreeNode(1002, dumNode, null);

        Set<Integer> deleteSet = new HashSet<>();
        for (int i: to_delete) {
            deleteSet.add(i);
        }
        deleteSet.add(dumNode.val);

        List<TreeNode> res = new LinkedList<>();
        iter(dumNode, dumParentNode, true, deleteSet, res);
        return res;
    }

    public void iter(TreeNode current, TreeNode parent, Boolean left, Set<Integer> to_delete, List<TreeNode> res) {
        if (current == null) {
            return;
        }

        if (to_delete.contains(current.val)) {
            if (left) {
                parent.left = null;
            } else {
                parent.right = null;
            }

            if (current.left != null && !to_delete.contains(current.left.val)) {
                res.add(current.left);
            }

            if (current.right != null && !to_delete.contains(current.right.val)) {
                res.add(current.right);
            }
        }
        iter(current.left, current, true, to_delete, res);
        iter(current.right, current, false, to_delete, res);
    }
}

class Driver1110 {
    public static void main(String[] args) {
    }
}