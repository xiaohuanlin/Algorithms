import java.util.*;

// Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

// A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

 

// Example 1:


// Input: root = [1,null,2,null,3,null,4,null,null]
// Output: [2,1,3,null,null,null,4]
// Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.
// Example 2:


// Input: root = [2,1,3]
// Output: [2,1,3]
 

// Constraints:

// The number of nodes in the tree is in the range [1, 104].
// 1 <= Node.val <= 10^5

class Solution1382 {
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

    public TreeNode balanceBST(TreeNode root) {
        List<Integer> values = new ArrayList<>();
        getValues(root, values);
        return formBST(values, 0, values.size());
    }

    public void getValues(TreeNode root, List<Integer> values) {
        if (root == null) {
            return;
        }
        getValues(root.left, values);
        values.add(root.val);
        getValues(root.right, values);
    }

    public TreeNode formBST(List<Integer> values, int start, int end) {
        if (start == end) {
            return null;
        }
        int middle = (end - start) / 2 + start;
        return new TreeNode(values.get(middle), formBST(values, start, middle), formBST(values, middle + 1, end));
    }
}

class Driver1382 {
    public static void main(String[] args) {
    }
}