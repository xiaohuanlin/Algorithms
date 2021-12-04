import java.util.*;

// Given an array arr of positive integers, consider all binary trees such that:

// Each node has either 0 or 2 children;
// The values of arr correspond to the values of each leaf in an in-order traversal of the tree.
// The value of each non-leaf node is equal to the product of the largest leaf value in its left and right subtree, respectively.
// Among all possible binary trees considered, return the smallest possible sum of the values of each non-leaf node. It is guaranteed this sum fits into a 32-bit integer.

// A node is a leaf if and only if it has zero children.

 

// Example 1:


// Input: arr = [6,2,4]
// Output: 32
// Explanation: There are two possible trees shown.
// The first has a non-leaf node sum 36, and the second has non-leaf node sum 32.
// Example 2:


// Input: arr = [4,11]
// Output: 44
 

// Constraints:

// 2 <= arr.length <= 40
// 1 <= arr[i] <= 15
// It is guaranteed that the answer fits into a 32-bit signed integer (i.e., it is less than 231).


class Solution1130 {
    public int mctFromLeafValues(int[] arr) {
        int length = arr.length;
        int[][][] dp = new int[length][length][2];
        for (int i = 0; i < length; i++) {
            // min sum
            dp[i][i][0] = arr[i];
            // max left node
            dp[i][i][1] = arr[i];
        }

        for (int size = 1; size < length; size++) {
            for (int i = 0; i + size < length; i++) {
                dp[i][i + size][0] = Integer.MAX_VALUE;
                for (int split = 0; split < size; split++) {
                    int sum = dp[i][i + split][0] + dp[i + split + 1][i + size][0] + 
                                dp[i][i + split][1] * dp[i + split + 1][i + size][1];
                    if (sum < dp[i][i + size][0]) {
                        dp[i][i + size][0] = sum;
                        dp[i][i + size][1] = Math.max(dp[i][i + split][1], dp[i + split + 1][i + size][1]);
                    }
                }
            }
        }

        int sum = 0;
        for (int v: arr) {
            sum += v;
        }
        return dp[0][length - 1][0] - sum;
    }
}

class Driver1130 {
    public static void main(String[] args) {
        int[] arr = {6, 2, 4};
        System.out.println((new Solution1130()).mctFromLeafValues(arr));
    }
}