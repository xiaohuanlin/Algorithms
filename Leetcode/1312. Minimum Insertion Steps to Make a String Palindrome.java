// Given a string s. In one step you can insert any character at any index of the string.

// Return the minimum number of steps to make s palindrome.

// A Palindrome String is one that reads the same backward as well as forward.

 

// Example 1:

// Input: s = "zzazz"
// Output: 0
// Explanation: The string "zzazz" is already palindrome we don't need any insertions.
// Example 2:

// Input: s = "mbadm"
// Output: 2
// Explanation: String can be "mbdadbm" or "mdbabdm".
// Example 3:

// Input: s = "leetcode"
// Output: 5
// Explanation: Inserting 5 characters the string becomes "leetcodocteel".
// Example 4:

// Input: s = "g"
// Output: 0
// Example 5:

// Input: s = "no"
// Output: 1
 

// Constraints:

// 1 <= s.length <= 500
// All characters of s are lower case English letters.


class Solution1312 {
    public int minInsertions(String s) {
        int[][] dp = new int[s.length()][s.length()];

        for (int j = 1; j < s.length(); j++) {
            for (int k = 0; j + k < s.length(); k++) {
                if (s.charAt(k) == s.charAt(j+k)) {
                    dp[k][j+k] = dp[k+1][j+k-1];
                } else {
                    dp[k][j+k] = Math.min(dp[k+1][j+k], dp[k][j+k-1]) + 1;
                }
            }
        }
        return dp[0][s.length() - 1];
    }
}

class Driver1312 {
    public static void main(String[] args) {
        Solution1312 solution = new Solution1312();

        String s = "leetcode";
        System.out.println(solution.minInsertions(s));
    }
}