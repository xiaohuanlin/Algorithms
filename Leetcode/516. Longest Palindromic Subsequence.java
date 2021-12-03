import java.util.*;

// Given a string s, find the longest palindromic subsequence's length in s.

// A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

 

// Example 1:

// Input: s = "bbbab"
// Output: 4
// Explanation: One possible longest palindromic subsequence is "bbbb".
// Example 2:

// Input: s = "cbbd"
// Output: 2
// Explanation: One possible longest palindromic subsequence is "bb".
 

// Constraints:

// 1 <= s.length <= 1000
// s consists only of lowercase English letters.


class Solution516 {
    public int longestPalindromeSubseq(String s) {
        int length = s.length();
        int[][] dp = new int[length][length];
        for (int i = 0; i < length; i++) {
            dp[i][i] = 1;
        }

        for (int size = 1; size < length; size++) {
            for (int i = 0; i + size < length; i++) {
                int inner = 0;
                if (s.charAt(i) == s.charAt(i + size)) {
                    inner = dp[i + 1][i + size - 1] + 2;
                }
                dp[i][i + size] = Math.max(Math.max(dp[i][i + size - 1], dp[i + 1][i + size]), inner);
            }
        }
        return dp[0][length - 1];
    }
}

class Driver516 {
    public static void main(String[] args) {
        String s = "bbbab";
        System.out.println((new Solution516()).longestPalindromeSubseq(s));
    }
}