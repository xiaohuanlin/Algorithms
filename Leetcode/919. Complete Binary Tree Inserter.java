import java.util.*;

// A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.

// Design an algorithm to insert a new node to a complete binary tree keeping it complete after the insertion.

// Implement the CBTInserter class:

// CBTInserter(TreeNode root) Initializes the data structure with the root of the complete binary tree.
// int insert(int v) Inserts a TreeNode into the tree with value Node.val == val so that the tree remains complete, and returns the value of the parent of the inserted TreeNode.
// TreeNode get_root() Returns the root node of the tree.
 

// Example 1:


// Input
// ["CBTInserter", "insert", "insert", "get_root"]
// [[[1, 2]], [3], [4], []]
// Output
// [null, 1, 2, [1, 2, 3, 4]]

// Explanation
// CBTInserter cBTInserter = new CBTInserter([1, 2]);
// cBTInserter.insert(3);  // return 1
// cBTInserter.insert(4);  // return 2
// cBTInserter.get_root(); // return [1, 2, 3, 4]
 

// Constraints:

// The number of nodes in the tree will be in the range [1, 1000].
// 0 <= Node.val <= 5000
// root is a complete binary tree.
// 0 <= val <= 5000
// At most 104 calls will be made to insert and get_root.

class CBTInserter {
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

    private TreeNode root;
    private Queue<TreeNode> leaves = new LinkedList<>();

    public CBTInserter(TreeNode root) {
        this.root = root;
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);
        while (!q.isEmpty()) {
            TreeNode n = q.poll();
            if (n == null) {
                continue;
            }
            if (!(n.left != null && n.right != null)) {
                leaves.offer(n);
            }
            q.offer(n.left);
            q.offer(n.right);
        }
    }
    
    public int insert(int val) {
        TreeNode n = leaves.peek();
        if (n.left == null) {
            n.left = new TreeNode(val);
            leaves.offer(n.left);
        } else {
            leaves.poll();
            n.right = new TreeNode(val);
            leaves.offer(n.right);
        }
        return n.val;
    }
    
    public TreeNode get_root() {
        return this.root;
    }
}

class Driver1110 {
    public static void main(String[] args) {
    }
}