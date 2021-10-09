import java.util.HashMap;

// The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.

// Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken into on the same night.

// Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.

 

// Example 1:


// Input: root = [3,2,3,null,3,null,1]
// Output: 7
// Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
// Example 2:


// Input: root = [3,4,5,1,3,null,1]
// Output: 9
// Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
 

// Constraints:

// The number of nodes in the tree is in the range [1, 104].
// 0 <= Node.val <= 10^4

/**
 * Definition for a binary tree node.
 */
class TreeNode {
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


class Solution337 {
    private HashMap<TreeNode, Integer> maps = new HashMap<>();
    public int rob(TreeNode root) {
        if (root == null) {
            return 0;
        }
        if (maps.containsKey(root)) {
            return maps.get(root);
        }

        int noUseRootRes = rob(root.left) + rob(root.right);
        int useRootRes = root.val;
        if (root.left != null) {
            useRootRes += rob(root.left.left);
            useRootRes += rob(root.left.right);
        }
        if (root.right != null) {
            useRootRes += rob(root.right.left);
            useRootRes += rob(root.right.right);
        }
        int res = Math.max(useRootRes, noUseRootRes);
        maps.put(root, res);
        return res;
    }
}

class Driver337 {
    public static void main(String[] args) {
        Solution337 solution = new Solution337();

        TreeNode t = new TreeNode();
        System.out.println(solution.rob(t));
    }
}