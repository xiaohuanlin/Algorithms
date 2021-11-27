import java.util.*;

// You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

// Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

// Example 1:

// Input: s = "ABAB", k = 2
// Output: 4
// Explanation: Replace the two 'A's with two 'B's or vice versa.
// Example 2:

// Input: s = "AABABBA", k = 1
// Output: 4
// Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
// The substring "BBBB" has the longest repeating letters, which is 4.
 

// Constraints:

// 1 <= s.length <= 105
// s consists of only uppercase English letters.
// 0 <= k <= s.length

class Solution424 {
    public int characterReplacement(String s, int k) {
        int begin = 0;
        int end = 0;
        int[] freq = new int[26];
        int maxFreq = 0;
        int res = 0;
        while (end < s.length()) {
            freq[s.charAt(end) - 'A']++;
            for (int i = 0; i < 26; i++) {
                maxFreq = Math.max(maxFreq, freq[i]);
            }

            while (end - begin + 1 - maxFreq > k) {
                freq[s.charAt(begin) - 'A']--;
                begin++;
                for (int i = 0; i < 26; i++) {
                    maxFreq = Math.max(maxFreq, freq[i]);
                }
            }

            res = Math.max(res, end - begin + 1);
            end++;
        }
        return res;
    }
}

class Driver424 {
    public static void main(String[] args) {
        Solution424 solution = new Solution424();

        String s = "ABAB";
        int k = 2;
        System.out.println(solution.characterReplacement(s, k));
    }
}