import java.util.*;

// You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.

// Return the minimum number of steps to make t an anagram of s.

// An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

 

// Example 1:

// Input: s = "bab", t = "aba"
// Output: 1
// Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.
// Example 2:

// Input: s = "leetcode", t = "practice"
// Output: 5
// Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.
// Example 3:

// Input: s = "anagram", t = "mangaar"
// Output: 0
// Explanation: "anagram" and "mangaar" are anagrams. 
 

// Constraints:

// 1 <= s.length <= 5 * 104
// s.length == t.length
// s and t consist of lowercase English letters only.

class Solution1347 {
    public int minSteps(String s, String t) {
        int[] counts = new int[26];
        for (Character c: s.toCharArray()) {
            counts[c - 'a']++;
        }

        for (Character c: t.toCharArray()) {
            counts[c - 'a']--;
        }

        int res = 0;
        for (int count: counts) {
            if (count > 0) {
                res += count;
            }
        }
        return res;
    }
}

class Driver1347 {
    public static void main(String[] args) {
        String s = "leetcode";
        String t = "practice";
        System.out.println(new Solution1347().minSteps(s, t));
    }
}