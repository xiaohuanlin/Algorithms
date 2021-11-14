
// Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

// Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

// A palindrome is a string that reads the same forwards and backwards.

// A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

// For example, "ace" is a subsequence of "abcde".
 

// Example 1:

// Input: s = "aabca"
// Output: 3
// Explanation: The 3 palindromic subsequences of length 3 are:
// - "aba" (subsequence of "aabca")
// - "aaa" (subsequence of "aabca")
// - "aca" (subsequence of "aabca")
// Example 2:

// Input: s = "adc"
// Output: 0
// Explanation: There are no palindromic subsequences of length 3 in "adc".
// Example 3:

// Input: s = "bbcbaba"
// Output: 4
// Explanation: The 4 palindromic subsequences of length 3 are:
// - "bbb" (subsequence of "bbcbaba")
// - "bcb" (subsequence of "bbcbaba")
// - "bab" (subsequence of "bbcbaba")
// - "aba" (subsequence of "bbcbaba")
 

// Constraints:

// 3 <= s.length <= 105
// s consists of only lowercase English letters.


class Solution1930 {
    public int countPalindromicSubsequence(String s) {
        int[][] dp = new int[s.length() + 1][26];
        int[] first = new int[26];
        int[] last = new int[26];

        for (int i = 1; i <= s.length(); i++) {
            int pos = s.charAt(i - 1) - 'a';
            dp[i] = dp[i - 1].clone();
            dp[i][pos]++;
            if (dp[i][pos] == 1) {
                first[pos] = i;
            }
            last[pos] = i;
        }

        int count = 0;

        for (int i = 0; i < 26; i++) {
            // case 2 'aba'
            if (dp[s.length()][i] > 1) {
                if (first[i] < last[i] - 1) {
                    for (int j = 0; j < 26; j++) {
                        if (dp[first[i]][j] != dp[last[i] - 1][j]) {
                            count++;
                        }
                    }
                }
            }
        }
        return count;
    }
}

class Driver1930 {
    public static void main(String[] args) {
        Solution1930 solution = new Solution1930();

        String s = "adc";
        System.out.println(solution.countPalindromicSubsequence(s));
    }
}