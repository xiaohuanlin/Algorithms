import java.util.*;

// Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.

 

// Example 1:

// Input: s1 = "sea", s2 = "eat"
// Output: 231
// Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
// Deleting "t" from "eat" adds 116 to the sum.
// At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
// Example 2:

// Input: s1 = "delete", s2 = "leet"
// Output: 403
// Explanation: Deleting "dee" from "delete" to turn the string into "let",
// adds 100[d] + 101[e] + 101[e] to the sum.
// Deleting "e" from "leet" adds 101[e] to the sum.
// At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
// If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
 

// Constraints:

// 1 <= s1.length, s2.length <= 1000
// s1 and s2 consist of lowercase English letters.

class Solution712 {
    public int minimumDeleteSum(String s1, String s2) {
        int row = s1.length();
        int col = s2.length();
        int[][] dp = new int[row+1][col+1];

        for (int total = 2; total <= row + col; total++) {
            for (int j = 1, i = total - j; i >= 1; j++, i--) {
                if (i > row || j > col) {
                    continue;
                }
                dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
                if (s1.charAt(i - 1) == s2.charAt(j - 1)) {
                    dp[i][j] = Math.max(dp[i][j], dp[i-1][j-1] + s1.charAt(i - 1));
                }
            }
        }
        for (int[] rows: dp) {
            System.out.println(Arrays.toString(rows));
        }

        int sum = 0;
        for (int i = 0; i < row; i++) {
            sum += s1.charAt(i);
        }
        for (int i = 0; i < col; i++) {
            sum += s2.charAt(i);
        }
        return sum - dp[row][col] * 2;
    }
}

class Driver712 {
    public static void main(String[] args) {
        Solution712 solution = new Solution712();

        String s1 = "sea";
        String s2 = "eat";
        System.out.println(solution.minimumDeleteSum(s1, s2));
    }
}