import java.util.*;

// Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.

 

// Example 1:

// Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
// Output: 3
// Explanation: The repeated subarray with maximum length is [3,2,1].
// Example 2:

// Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
// Output: 5
 

// Constraints:

// 1 <= nums1.length, nums2.length <= 1000
// 0 <= nums1[i], nums2[i] <= 100

class Solution718 {
    public int findLength(int[] nums1, int[] nums2) {
        int row = nums1.length;
        int col = nums2.length;

        // dp[i][j][0] -> max length dp[i][j][1] -> same tail length
        int[][][] dp = new int[row + 1][col + 1][2];

        for (int i = 1; i <= row; i++) {
            for (int j = 1; j <= col; j++) {
                if (nums1[i - 1] == nums2[j - 1]) {
                    dp[i][j][1] = dp[i - 1][j - 1][1] + 1;
                } else {
                    dp[i][j][1] = 0;
                }
                dp[i][j][0] = Math.max(Math.max(dp[i - 1][j][0], dp[i][j - 1][0]), dp[i][j][1]);
            }
        }
        return dp[row][col][0];
    }
}

class Driver718 {
    public static void main(String[] args) {
        int[] nums1 = {1, 2, 3, 2, 1};
        int[] nums2 = {3, 2, 1, 4, 7};
        System.out.println(new Solution718().findLength(nums1, nums2));
    }
}