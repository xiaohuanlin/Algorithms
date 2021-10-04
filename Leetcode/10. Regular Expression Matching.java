// Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

// '.' Matches any single character.​​​​
// '*' Matches zero or more of the preceding element.
// The matching should cover the entire input string (not partial).

 

// Example 1:

// Input: s = "aa", p = "a"
// Output: false
// Explanation: "a" does not match the entire string "aa".
// Example 2:

// Input: s = "aa", p = "a*"
// Output: true
// Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
// Example 3:

// Input: s = "ab", p = ".*"
// Output: true
// Explanation: ".*" means "zero or more (*) of any character (.)".
// Example 4:

// Input: s = "aab", p = "c*a*b"
// Output: true
// Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
// Example 5:

// Input: s = "mississippi", p = "mis*is*p*."
// Output: false
 

// Constraints:

// 1 <= s.length <= 20
// 1 <= p.length <= 30
// s contains only lowercase English letters.
// p contains only lowercase English letters, '.', and '*'.
// It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.


class Solution10 {
    public boolean isMatch(String s, String p) {
        int row = s.length() + 1;
        int col = p.length() + 1;
        boolean[][] dp = new boolean[row][col];

        dp[row - 1][col - 1] = true;
        for (int i = 0; i < row - 1; i++) {
            dp[i][col - 1] = false;
        }
        for (int j = col - 2; j >= 0; j--) {
            // some line could be true if pattern like 'a*'
            if (j + 1 < p.length() && p.charAt(j + 1) == '*') {
                dp[row - 1][j] = dp[row - 1][j + 2];
            } else {
                dp[row - 1][j] = false;
            }
        }

        for (int i = row - 2; i >= 0; i--) {
            for (int j = col - 2; j >= 0; j--) {
                if (p.charAt(j) == '*') {
                    continue;
                }

                if (equal(s.charAt(i), p.charAt(j))) {
                    if (j + 1 < p.length() && p.charAt(j + 1) == '*') {
                        // can use it or not
                        if (j + 2 < col) {
                            dp[i][j] = dp[i + 1][j + 2] || dp[i + 1][j] || dp[i][j + 2];
                        } else {
                            dp[i][j] = dp[i + 1][j];
                        }
                    } else {
                        // must use this char
                        dp[i][j] = dp[i + 1][j + 1];
                    }
                } else {
                    if (j + 1 < p.length() && p.charAt(j + 1) == '*') {
                        // remove it
                        dp[i][j] = dp[i][j + 2];
                    } else {
                        dp[i][j] = false;
                    }
                }
            }
        }
        return dp[0][0];
    }

    private boolean equal(char a, char b) {
        return a == b || b == '.';
    }
}

class Driver10 {
    public static void main(String[] args) {
        Solution10 solution = new Solution10();

        String s = "bbbba";
        String p = ".*a*a";
        System.out.println(solution.isMatch(s, p));
    }
}