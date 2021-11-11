import java.util.*;

// Given the root of a binary tree and an integer distance. A pair of two different leaf nodes of a binary tree is said to be good if the length of the shortest path between them is less than or equal to distance.

// Return the number of good leaf node pairs in the tree.

 

// Example 1:


// Input: root = [1,2,3,null,4], distance = 3
// Output: 1
// Explanation: The leaf nodes of the tree are 3 and 4 and the length of the shortest path between them is 3. This is the only good pair.
// Example 2:


// Input: root = [1,2,3,4,5,6,7], distance = 3
// Output: 2
// Explanation: The good pairs are [4,5] and [6,7] with shortest path = 2. The pair [4,6] is not good because the length of ther shortest path between them is 4.
// Example 3:

// Input: root = [7,1,4,6,null,5,3,null,null,null,null,null,2], distance = 3
// Output: 1
// Explanation: The only good pair is [2,5].
// Example 4:

// Input: root = [100], distance = 1
// Output: 0
// Example 5:

// Input: root = [1,1,1], distance = 2
// Output: 1
 

// Constraints:

// The number of nodes in the tree is in the range [1, 2^10].
// Each node's value is between [1, 100].
// 1 <= distance <= 10


class Solution1530 {
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

    public class Result {
        Map<Integer, Integer> maps;
        int count;
        Result(Map<Integer, Integer> maps, int count) {
            this.maps = maps;
            this.count = count;
        }
    }

    public int countPairs(TreeNode root, int distance) {
        Result res = recur(root, distance);
        return res.count;
    }

    public Result recur(TreeNode root, int distance) {
        Map<Integer, Integer> res = new HashMap<>();
        if (root == null) {
            return new Result(res, 0);
        }
        if (root.left == null && root.right == null) {
            res.put(0, 1);
        }
        
        Result left = recur(root.left, distance);
        Result right = recur(root.right, distance);
        for (Map.Entry<Integer, Integer> entry: left.maps.entrySet()) {
            res.put(entry.getKey() + 1, entry.getValue() + res.getOrDefault(entry.getKey() + 1, 0));
        }
        for (Map.Entry<Integer, Integer> entry: right.maps.entrySet()) {
            res.put(entry.getKey() + 1, entry.getValue() + res.getOrDefault(entry.getKey() + 1, 0));
        }

        int count = 0;
        for (Map.Entry<Integer, Integer> entry: left.maps.entrySet()) {
            Integer key = entry.getKey();
            for (Map.Entry<Integer, Integer> rightEntry: right.maps.entrySet()) {
                if (key + 1 + rightEntry.getKey() + 1 <= distance) {
                    count += entry.getValue() * rightEntry.getValue();
                }
            }
        }
        return new Result(res, left.count + right.count + count);
    }
}

class Driver1530 {
    public static void main(String[] args) {
    }
}