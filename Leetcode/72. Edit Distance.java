// Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

// You have the following three operations permitted on a word:

// Insert a character
// Delete a character
// Replace a character
 

// Example 1:

// Input: word1 = "horse", word2 = "ros"
// Output: 3
// Explanation: 
// horse -> rorse (replace 'h' with 'r')
// rorse -> rose (remove 'r')
// rose -> ros (remove 'e')
// Example 2:

// Input: word1 = "intention", word2 = "execution"
// Output: 5
// Explanation: 
// intention -> inention (remove 't')
// inention -> enention (replace 'i' with 'e')
// enention -> exention (replace 'n' with 'x')
// exention -> exection (replace 'n' with 'c')
// exection -> execution (insert 'u')
 

// Constraints:

// 0 <= word1.length, word2.length <= 500
// word1 and word2 consist of lowercase English letters.


class Solution72 {
    public int minDistance(String word1, String word2) {
        int row = word1.length();
        int col = word2.length();
        int[][] dp = new int[row + 1][col + 1];
        
        for (int j = 0; j < col + 1; j++) {
            dp[0][j] = j;
        }

        for (int i = 0; i < row + 1; i++) {
            dp[i][0] = i;
        }


        for (int i = 1; i < row + 1; i++) {
            for (int j = 1; j < col + 1; j++) {
                if (word1.charAt(i-1) == word2.charAt(j-1)) {
                    dp[i][j] = dp[i-1][j-1];
                } else {
                    dp[i][j] = Math.min(Math.min(dp[i-1][j-1], dp[i-1][j]), dp[i][j-1]) + 1;
                }
            }
        }
        return dp[row][col];
    }
}

class Driver72 {
    public static void main(String[] args) {
        Solution72 solution = new Solution72();

        String p1 = "horse";
        String p2 = "ros";
        System.out.println(solution.minDistance(p1, p2));
    }
}